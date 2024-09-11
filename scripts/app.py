
import streamlit as st
import replicate
import os

# Sidebar for API key input
st.sidebar.title("AI Pipeline Builder")
api_key = st.sidebar.text_input("Enter your Replicate API key:", type="password")
if api_key:
    os.environ["REPLICATE_API_TOKEN"] = api_key
    st.sidebar.success("API key set successfully.")

# Defining Categories and Models
categories = {
    'Image': ['Upscale Image', 'Remove Background', 'Super Resolution'],
    'Video': ['Image to Video', 'Text to Video'],
    'Audio': ['Text to Music', 'Voice Generation', 'Audio Enhancement'],
    'Text': ['LLaMA (Text Generation)', 'Summarization', 'Sentiment Analysis']
}

# Sidebar for selecting category and model
st.sidebar.title("Model Categories")
selected_category = st.sidebar.selectbox("Select a category", list(categories.keys()))
selected_model = st.sidebar.selectbox("Select a model", categories[selected_category])

# Display selected model and its input options
st.title(f"{selected_category} - {selected_model}")
if selected_model == 'Upscale Image':
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    if uploaded_image and st.button("Run Upscale"):
        model = replicate.models.get("stability-ai/stable-diffusion")
        output = model.predict(image=uploaded_image, scale=2)
        st.image(output, caption="Upscaled Image")

elif selected_model == 'Remove Background':
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    if uploaded_image and st.button("Remove Background"):
        model = replicate.models.get("rembg/rembg")
        output = model.predict(image=uploaded_image)
        st.image(output, caption="Image without Background")

elif selected_model == 'Super Resolution':
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    if uploaded_image and st.button("Run Super Resolution"):
        model = replicate.models.get("superresolution/superresolution")
        output = model.predict(image=uploaded_image)
        st.image(output, caption="Super Resolved Image")

elif selected_model == 'Image to Video':
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    if uploaded_image and st.button("Generate Video"):
        model = replicate.models.get("image-to-video/model")
        output = model.predict(image=uploaded_image)
        st.video(output)

elif selected_model == 'Text to Video':
    text_input = st.text_area("Enter a text prompt")
    if text_input and st.button("Generate Video"):
        model = replicate.models.get("text-to-video/model")
        output = model.predict(prompt=text_input)
        st.video(output)

elif selected_model == 'Text to Music':
    text_input = st.text_area("Enter a text prompt for music generation")
    if text_input and st.button("Generate Music"):
        model = replicate.models.get("text-to-music/model")
        output = model.predict(prompt=text_input)
        st.audio(output)

elif selected_model == 'Voice Generation':
    text_input = st.text_area("Enter text to generate voice")
    if text_input and st.button("Generate Voice"):
        model = replicate.models.get("voice-generation/model")
        output = model.predict(text=text_input)
        st.audio(output)

elif selected_model == 'Audio Enhancement':
    uploaded_audio = st.file_uploader("Upload an audio file", type=["mp3", "wav"])
    if uploaded_audio and st.button("Enhance Audio"):
        model = replicate.models.get("audio-enhancement/model")
        output = model.predict(audio=uploaded_audio)
        st.audio(output)

elif selected_model == 'LLaMA (Text Generation)':
    text_input = st.text_area("Enter a text prompt for LLaMA")
    if text_input and st.button("Generate Text"):
        model = replicate.models.get("llama/text-generation")
        output = model.predict(prompt=text_input)
        st.write(output)

elif selected_model == 'Summarization':
    text_input = st.text_area("Enter text to summarize")
    if text_input and st.button("Summarize Text"):
        model = replicate.models.get("summarization/model")
        output = model.predict(text=text_input)
        st.write(output)

elif selected_model == 'Sentiment Analysis':
    text_input = st.text_area("Enter text to analyze sentiment")
    if text_input and st.button("Analyze Sentiment"):
        model = replicate.models.get("sentiment-analysis/model")
        output = model.predict(text=text_input)
        st.write(f"Sentiment: {output}")
