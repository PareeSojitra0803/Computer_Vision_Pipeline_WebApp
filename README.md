# Computer Vision Pipeline WebApp

Streamlit deployment app for the **Home Safety Sound Detector**, using a Teachable Machine audio model in the browser through TensorFlow.js.

## Classes
- Alarm
- Background Noise
- Door Knock
- Glass Break
- Siren

## Required files

Copy `model.json`, `metadata.json`, and `weights.bin` from your main project's `data/models/home_safety_audio/` folder into this repository:

```text
Computer_Vision_Pipeline_WebApp/
├── app.py
├── requirements.txt
├── README.md
├── .streamlit/
│   └── config.toml
└── static/
    └── models/
        └── home_safety_audio/
            ├── model.json
            ├── metadata.json
            └── weights.bin
```

Keep the three model filenames unchanged.

## Install and run

Python 3.11 is recommended for consistency.

```powershell
py -3.11 -m pip install -r requirements.txt
py -3.11 -m streamlit run app.py
```

Open the local URL printed in the terminal (usually `http://localhost:8501`), click **Start listening**, and allow microphone access.

## Static file configuration

Create `.streamlit/config.toml` with:

```toml
[server]
enableStaticServing = true
```

This enables the app to serve model files from `static/`.

## Deploy to Streamlit Community Cloud

1. Push `app.py`, `requirements.txt`, `README.md`, `.streamlit/config.toml`, and `static/` to GitHub.
2. Create an app in Streamlit Community Cloud from the repository.
3. Set the main file path to `app.py`, then deploy.
4. Open the HTTPS URL and allow microphone access.

The app loads TensorFlow.js and the Speech Commands library from public CDNs, so the browser needs internet access.

## Troubleshooting
- **Model files missing:** confirm all three files are in `static/models/home_safety_audio/`.
- **Model fails to load:** ensure `model.json` points to the expected weights file and the files were copied together.
- **Microphone blocked:** allow microphone access and reload. Deployed apps require HTTPS.
- **Low confidence:** noise, microphone quality, and training sample variety affect results.

Image and pose detection can be added to this app later when those pipelines are ready.
