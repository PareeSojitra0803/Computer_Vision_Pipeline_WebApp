from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

APP_DIR = Path(__file__).resolve().parent
MODEL_DIR = APP_DIR / "static" / "models" / "home_safety_audio"
MODEL_FILES = [MODEL_DIR / "model.json", MODEL_DIR / "metadata.json", MODEL_DIR / "weights.bin"]

st.set_page_config(page_title="Home Safety Sound Detector", page_icon="🎙️", layout="wide")
st.markdown("""
<style>
.block-container{max-width:1100px;padding-top:2rem}
.hero{padding:1.5rem 1.7rem;border-radius:18px;background:linear-gradient(120deg,#14233b,#182d36);border:1px solid rgba(255,255,255,.12);margin-bottom:1rem}
.hero h1{margin:0;font-size:2.15rem}.hero p{margin:.5rem 0 0;color:#d0d9e6}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<div class="hero"><h1>🎙️ Home Safety Sound Detector</h1>
<p>Live detection of alarms, door knocks, glass breaks, sirens, and background noise.</p></div>
""", unsafe_allow_html=True)

with st.expander("About this project"):
    st.write("This app runs the Teachable Machine audio model in the browser using TensorFlow.js.")
    st.caption("Allow microphone access when prompted. Deployed apps require HTTPS.")

missing = [p.name for p in MODEL_FILES if not p.is_file()]
if missing:
    st.error("Model files are missing: " + ", ".join(missing))
    st.markdown("""
**Copy these three files from your main project's `data/models/home_safety_audio/` folder** into this deployment repository:

```text
static/
└── models/
    └── home_safety_audio/
        ├── model.json
        ├── metadata.json
        └── weights.bin
```
""")
    st.stop()

model_url = "/app/static/models/home_safety_audio/model.json"
metadata_url = "/app/static/models/home_safety_audio/metadata.json"

html = r"""<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<style>
body{margin:0;font-family:Arial,sans-serif;color:#edf2f7;background:transparent}
.panel{border:1px solid #344254;border-radius:16px;padding:18px;background:#111923}
.controls{display:flex;flex-wrap:wrap;gap:10px;margin:12px 0 16px}
button{border:0;border-radius:10px;padding:11px 16px;font-weight:700;cursor:pointer}
#start{background:#38bdf8;color:#07131d}#stop{background:#334155;color:white}
button:disabled{opacity:.45;cursor:not-allowed}
#status{color:#b9c8d8;font-size:14px;margin:8px 0 14px}
.prediction{margin:14px 0}.label{display:flex;justify-content:space-between;gap:10px;margin-bottom:6px;font-size:14px}
.track{height:12px;border-radius:99px;background:#273444;overflow:hidden}
.bar{height:100%;width:0%;background:linear-gradient(90deg,#38bdf8,#34d399);transition:width .15s ease}
#top{font-size:1.35rem;font-weight:700;margin:8px 0}#error{color:#fca5a5;white-space:pre-wrap;font-size:13px}
.note{color:#94a3b8;font-size:12px;margin-top:14px;line-height:1.5}
</style></head><body><div class="panel"><strong>Live audio classification</strong>
<div id="status">Loading model…</div><div class="controls"><button id="start" disabled>🎙️ Start listening</button><button id="stop" disabled>Stop</button></div>
<div id="top">Waiting for audio</div><div id="predictions"></div><div id="error"></div>
<div class="note">Keep this tab open while listening. Results depend on microphone quality and training examples.</div></div>
<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@1.3.1/dist/tf.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@tensorflow-models/speech-commands@0.4.0/dist/speech-commands.min.js"></script>
<script>
(async()=>{
const modelURL=__MODEL_URL__,metadataURL=__METADATA_URL__;
const status=document.getElementById('status'),startBtn=document.getElementById('start'),stopBtn=document.getElementById('stop');
const topEl=document.getElementById('top'),predEl=document.getElementById('predictions'),errorEl=document.getElementById('error');
let recognizer=null,labels=[];
function fail(msg){errorEl.textContent=msg;status.textContent='Could not start detector.'}
try{
 if(!window.isSecureContext&&location.hostname!=='localhost')throw new Error('Microphone access requires HTTPS.');
 recognizer=speechCommands.create('BROWSER_FFT',undefined,modelURL,metadataURL);
 await recognizer.ensureModelLoaded();labels=recognizer.wordLabels();
 predEl.innerHTML=labels.map((label,i)=>`<div class="prediction"><div class="label"><span>${label}</span><span id="pct-${i}">0%</span></div><div class="track"><div class="bar" id="bar-${i}"></div></div></div>`).join('');
 status.textContent='Model loaded. Click Start listening and allow microphone access.';startBtn.disabled=false;
}catch(e){fail(String(e&&e.message?e.message:e));return}
startBtn.addEventListener('click',async()=>{
 try{errorEl.textContent='';startBtn.disabled=true;
 await recognizer.listen(result=>{
  const scores=Array.from(result.scores),best=scores.indexOf(Math.max(...scores)),confidence=scores[best]||0;
  topEl.textContent=`${labels[best]||'Unknown'} (${(confidence*100).toFixed(1)}%)`;
  scores.forEach((score,i)=>{const pct=Math.max(0,Math.min(100,score*100)),bar=document.getElementById(`bar-${i}`),txt=document.getElementById(`pct-${i}`);if(bar)bar.style.width=pct.toFixed(1)+'%';if(txt)txt.textContent=pct.toFixed(1)+'%'});
 },{includeSpectrogram:false,probabilityThreshold:0.25,invokeCallbackOnNoiseAndUnknown:true,overlapFactor:0.5});
 status.textContent='Listening live…';stopBtn.disabled=false;
 }catch(e){startBtn.disabled=false;fail(String(e&&e.message?e.message:e))}
});
stopBtn.addEventListener('click',async()=>{try{await recognizer.stopListening()}catch(_){}stopBtn.disabled=true;startBtn.disabled=false;status.textContent='Stopped. Click Start listening to resume.'});
})();
</script></body></html>"""
html = html.replace("__MODEL_URL__", '"' + model_url + '"').replace("__METADATA_URL__", '"' + metadata_url + '"')
components.html(html, height=650, scrolling=True)
