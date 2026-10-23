# 🎙️ Home Safety Sound Detector — Web App

A Streamlit deployment interface for a Teachable Machine audio-classification model. It detects five audio classes:

- **Alarm**
- **Background Noise**
- **Door Knock**
- **Glass Break**
- **Siren**

## 🌐 Live Demo

**Live app:** https://home-safety-detection.streamlit.app/

## 🧠 Model files

This model was trained using [Google Teachable Machine](https://teachablemachine.withgoogle.com/) and uses the TensorFlow.js Speech Commands format. It is **not** a Keras `.h5` model and should not be loaded using `keras.load_model()`.

Keep these files together in `static/models/home_safety_audio/`:

- `model.json`
- `metadata.json`
- `weights.bin`

## 🚀 Run locally

1. Clone the repository:

   ```bash
   git clone https://github.com/PareeSojitra0803/Home_Safety_Detection_WebApp.git
   cd Home_Safety_Detection_WebApp
   ```

2. (Optional) Create a virtual environment:

   **Windows PowerShell**
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:

   ```bash
   streamlit run app.py
   ```

## 🎧 Using the detector

1. Open the app in a modern browser.
2. Click **Start listening** and allow microphone access.
3. Keep the page open while audio is classified.
4. Click **Stop** to finish.

Prediction quality depends on microphone quality, background conditions, and training examples. This is a demonstration project, not a certified emergency-monitoring system.

## 📁 Repository structure

```text
Home_Safety_Detection_WebApp/
├── .streamlit/
│   └── config.toml
├── static/
│   └── models/
│       └── home_safety_audio/
│           ├── model.json
│           ├── metadata.json
│           └── weights.bin
├── app.py
├── requirements.txt
└── README.md
```

## 🛠️ Technologies

- Python
- Streamlit
- TensorFlow.js
- TensorFlow.js Speech Commands
- Teachable Machine

## 🔗 Main project

The image classification project is maintained in the main repository:

[Smart_Prediction_Suite_Using_CNN](https://github.com/PareeSojitra0803/Smart_Prediction_Suite_Using_CNN)

## 👩‍💻 Author

**Paree G. Sojitra**

- GitHub: https://github.com/PareeSojitra0803
- LinkedIn: https://www.linkedin.com/in/pareesojitra/
