
import streamlit as st
import replicate
import os

# Define tabs in the sidebar
st.sidebar.title("AI Pipeline Builder")

tabs = st.sidebar.radio("Select a tab", ["API Settings", "Model Selection", "Node Properties"])

# Tab 1: API Settings
if tabs == "API Settings":
    st.sidebar.subheader("API Key")
    api_key = st.sidebar.text_input("Enter your Replicate API key", type="password")
    if api_key:
        st.sidebar.success("API key saved.")
        os.environ["REPLICATE_API_TOKEN"] = api_key  # Set API key

# Tab 2: Model Selection
elif tabs == "Model Selection":
    st.sidebar.subheader("Select a Model Category")
    model_category = st.sidebar.selectbox("Choose a category", ["Text", "Image", "Video", "Audio"])

    if model_category == "Text":
        selected_model = st.sidebar.selectbox("Choose a model", ["LLaMA (Text Generation)", "Summarization", "Sentiment Analysis", "Stable Diffusion (Text-to-Image)"])
        st.write(f"Selected Model: {selected_model}")
    
    elif model_category == "Image":
        selected_model = st.sidebar.selectbox("Choose a model", ["Stable Diffusion (Text-to-Image)", "Upscale Image", "Remove Background", "Super Resolution"])
        st.write(f"Selected Model: {selected_model}")

    elif model_category == "Video":
        selected_model = st.sidebar.selectbox("Choose a model", ["Image-to-Video", "Text-to-Video"])
        st.write(f"Selected Model: {selected_model}")

    elif model_category == "Audio":
        selected_model = st.sidebar.selectbox("Choose a model", ["Text-to-Music", "Voice Generation", "Audio Enhancement"])
        st.write(f"Selected Model: {selected_model}")

# Tab 3: Node Properties
elif tabs == "Node Properties":
    st.sidebar.subheader("Node Properties")
    st.sidebar.write("Here you can adjust the parameters for the selected model node.")
    
    # Display parameters based on the selected model from the Model Selection tab
    if 'selected_model' in globals():
        st.write(f"Adjust parameters for {selected_model}")
        
        # Example parameters for Text models
        if selected_model == "LLaMA (Text Generation)":
            st.sidebar.slider("Temperature", 0.1, 1.0, 0.7, step=0.1)
            st.sidebar.slider("Max Tokens", 50, 500, 150, step=10)
            st.sidebar.checkbox("Top-P Sampling", value=True)
            st.sidebar.slider("Top-P Value", 0.1, 1.0, 0.9, step=0.1)
        
        # Example parameters for Image models
        elif selected_model == "Stable Diffusion (Text-to-Image)":
            st.sidebar.slider("Prompt Strength", 0.0, 1.0, 0.8, step=0.1)
            st.sidebar.slider("Image Resolution", 256, 1024, 512, step=128)
            st.sidebar.slider("Guidance Scale", 1.0, 10.0, 7.5, step=0.5)
            st.sidebar.slider("Steps", 10, 100, 50, step=5)

        # Example parameters for Video models
        elif selected_model == "Text-to-Video":
            st.sidebar.text_area("Enter a prompt for video generation")
            st.sidebar.slider("Duration", 1, 30, 10, step=1)
            st.sidebar.slider("Frame Rate", 10, 60, 24, step=2)
        
        # Example parameters for Audio models
        elif selected_model == "Text-to-Music":
            st.sidebar.text_area("Enter a prompt for music generation")
            st.sidebar.slider("Duration", 10, 300, 120, step=10)
            st.sidebar.selectbox("Genre", ["Classical", "Pop", "Rock", "Electronic"])
    else:
        st.write("No model selected.")
