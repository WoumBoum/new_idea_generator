"""Narration track + timeline for the explainer video.

Reads video/script.json, speaks every sentence with Kokoro (local, open-weights TTS), joins them with short
pauses and writes:
  video/build/voice.wav        the narration
  video/build/timeline.json    scene start/end times and one caption per sentence (exact, from the audio)
  video/build/captions.srt     the same captions as a subtitle file
"""
import json
from pathlib import Path

import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro

ROOT = Path(__file__).resolve().parents[1]
V = ROOT / "video"
B = V / "build"
LEAD_IN, SENTENCE_GAP, SCENE_GAP, TAIL = 0.4, 0.2, 0.42, 1.6


def srt_time(t):
    h, rem = divmod(t, 3600)
    m, s = divmod(rem, 60)
    return f"{int(h):02d}:{int(m):02d}:{int(s):02d},{int(round((s - int(s)) * 1000)):03d}"


def main():
    B.mkdir(parents=True, exist_ok=True)
    script = json.loads((V / "script.json").read_text())
    tts = Kokoro(str(ROOT / "data/tts/kokoro-v1.0.onnx"), str(ROOT / "data/tts/voices-v1.0.bin"))
    sr = 24000
    pieces = [np.zeros(int(LEAD_IN * sr), dtype=np.float32)]
    t = LEAD_IN
    scenes, captions = [], []
    for si, seg in enumerate(script["segments"]):
        start = t
        for k, sentence in enumerate(seg["say"]):
            audio, sr_ = tts.create(sentence, voice=script["voice"], speed=script["speed"], lang="en-us")
            assert sr_ == sr
            audio = audio.astype(np.float32)
            nz = np.where(np.abs(audio) > 0.004)[0]  # trim TTS edge silence so captions sit on the speech
            if len(nz):
                audio = audio[max(0, nz[0] - 240): nz[-1] + 480]
            dur = len(audio) / sr
            captions.append({"text": sentence, "start": round(t, 3), "end": round(t + dur, 3), "scene": seg["scene"]})
            pieces.append(audio)
            t += dur
            gap = SENTENCE_GAP if k < len(seg["say"]) - 1 else (SCENE_GAP if si < len(script["segments"]) - 1 else TAIL)
            pieces.append(np.zeros(int(gap * sr), dtype=np.float32))
            t += gap
        scenes.append({"scene": seg["scene"], "start": round(start, 3), "end": round(t, 3)})
    voice = np.concatenate(pieces)
    peak = np.abs(voice).max()
    voice = voice / peak * 0.89
    sf.write(B / "voice.wav", voice, sr)
    total = len(voice) / sr
    (B / "timeline.json").write_text(json.dumps({"total": round(total, 3), "scenes": scenes, "captions": captions}, indent=1))
    (B / "captions.srt").write_text("\n".join(f"{i}\n{srt_time(c['start'])} --> {srt_time(c['end'])}\n{c['text']}\n"
                                              for i, c in enumerate(captions, 1)))
    print(f"narration {total:.1f}s, {len(captions)} captions, {len(scenes)} scenes")
    for s in scenes:
        print(f"  {s['scene']:10s} {s['start']:6.1f} -> {s['end']:6.1f}  ({s['end'] - s['start']:.1f}s)")


if __name__ == "__main__":
    main()
