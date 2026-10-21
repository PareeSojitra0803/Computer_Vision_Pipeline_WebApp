import streamlit as st

st.set_page_config(
    page_title="Computer Vision Pipeline",
    page_icon="🔎",
    layout="wide",
)

st.title("🔎 Computer Vision Pipeline")
st.caption("Image • Audio • Pose | AI-powered detection dashboard")

st.info(
    "The deployment dashboard is being set up. The audio model was trained in "
    "Teachable Machine and currently runs as a TensorFlow.js browser model. "
    "This starter app prepares the Streamlit interface; audio integration will "
    "be added next."
)

st.subheader("Choose a project")

project = st.selectbox(
    "Project",
    ["Audio Event Detection", "Image Detection", "Pose Detection"],
)

if project == "Audio Event Detection":
    st.markdown("### 🎙️ Audio Event Detection")
    st.write(
        "Planned classes: Alarm, Background Noise, Door Knock, Glass Break, Siren."
    )
    st.warning(
        "The Teachable Machine audio model is not directly loadable with "
        "`keras.load_model()`. We need to connect its TensorFlow.js browser "
        "inference correctly before this page can make predictions."
    )
elif project == "Image Detection":
    st.markdown("### 🖼️ Image Detection")
    st.write("This section will be connected when the image pipeline is ready.")
elif project == "Pose Detection":
    st.markdown("### 🧍 Pose Detection")
    st.write("This section will be connected when the pose pipeline is ready.")

st.divider()
st.caption("Computer_Vision_Pipeline_WebApp • Development version")
