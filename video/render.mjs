// Render the explainer: step render.html through every frame and pipe JPEG frames into ffmpeg with the narration.
// usage: node video/render.mjs [out.mp4] [--fps 30] [--only t1,t2,...  (writes PNG stills instead)]
import { chromium } from "playwright";
import { spawn } from "node:child_process";
import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));
const build = path.join(here, "build");
const args = process.argv.slice(2);
const out = args.find(a => a.endsWith(".mp4")) || path.join(build, "explainer.mp4");
const fps = Number((args[args.indexOf("--fps") + 1]) || 30) || 30;
const only = args.includes("--only") ? args[args.indexOf("--only") + 1].split(",").map(Number) : null;
const exe = process.env.CHROME || "/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell";

const viz = readFileSync(path.join(build, "vizdata.json"), "utf8");
const tl = JSON.parse(readFileSync(path.join(build, "timeline.json"), "utf8"));

const browser = await chromium.launch({ executablePath: exe });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
const errors = [];
page.on("pageerror", e => errors.push(String(e)));
page.on("console", m => { if (m.type() === "error") errors.push(m.text()); });
await page.addInitScript(`window.VIZ = ${viz}; window.TL = ${JSON.stringify(tl)};`);
await page.goto("file://" + path.join(here, "render.html"), { waitUntil: "networkidle" });
await page.evaluate(() => window.setup());
const canvas = await page.$("#c");

if (only) {
  mkdirSync(path.join(build, "stills"), { recursive: true });
  for (const t of only) {
    await page.evaluate(t => window.renderAt(t), t);
    await canvas.screenshot({ path: path.join(build, "stills", `t${String(t).padStart(6, "0")}.png`) });
  }
  console.log("stills written", only.length, "errors:", errors.slice(0, 5));
  await browser.close();
  process.exit(0);
}

const n = Math.ceil(tl.total * fps);
const ff = spawn("ffmpeg", ["-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", String(fps), "-c:v", "mjpeg", "-i", "-",
  "-i", path.join(build, "voice.wav"), "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p",
  "-r", String(fps), "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-shortest", "-movflags", "+faststart", out],
  { stdio: ["pipe", "inherit", "inherit"] });
const t0 = Date.now();
for (let i = 0; i < n; i++) {
  await page.evaluate(t => window.renderAt(t), i / fps);
  const buf = await canvas.screenshot({ type: "jpeg", quality: 93 });
  if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once("drain", r));
  if (i % 300 === 0) console.log(`frame ${i}/${n}  ${((Date.now() - t0) / 1000).toFixed(0)}s`);
}
ff.stdin.end();
await new Promise(r => ff.on("close", r));
await browser.close();
writeFileSync(path.join(build, "render_errors.json"), JSON.stringify(errors, null, 1));
console.log("wrote", out, "frames", n, "errors", errors.length);
