
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
    'Text': ['LLaMA (Text Generation)', 'Summarization', 'Sentiment Analysis', 'Text to Image']
}

# Sidebar for selecting category and model
st.sidebar.title("Model Categories")
selected_category = st.sidebar.selectbox("Select a category", list(categories.keys()))
selected_model = st.sidebar.selectbox("Select a model", categories[selected_category])

# Storing the pipeline of commands
if 'pipeline' not in st.session_state:
    st.session_state['pipeline'] = []

# Display selected model and its input options
st.title(f"{selected_category} - {selected_model}")
if st.button("Add to Pipeline"):
    st.session_state['pipeline'].append((selected_category, selected_model))
    st.success(f"Added {selected_model} to pipeline!")

# Display current pipeline
st.subheader("Current Pipeline")
if st.session_state['pipeline']:
    for idx, (category, model) in enumerate(st.session_state['pipeline']):
        st.write(f"{idx + 1}. {category} - {model}")
else:
    st.write("No steps in the pipeline yet.")

# Execution logic for the pipeline
if st.button("Execute Pipeline"):
    st.write("Executing the AI pipeline...")
    output_data = None
    for idx, (category, model) in enumerate(st.session_state['pipeline']):
        st.write(f"Running step {idx + 1}: {model}...")
        
        if model == 'Text to Image':
            text_input = st.text_area("Enter a text prompt")
            if text_input:
                model = replicate.models.get("stability-ai/stable-diffusion")
                output_data = model.predict(prompt=text_input)
                st.image(output_data, caption="Generated Image")
        
        elif model == 'Upscale Image' and output_data:
            model = replicate.models.get("upscaler/real-esrgan")
            output_data = model.predict(image=output_data)
            st.image(output_data, caption="Upscaled Image")
        
        elif model == 'Remove Background' and output_data:
            model = replicate.models.get("rembg/rembg")
            output_data = model.predict(image=output_data)
            st.image(output_data, caption="Image without Background")
        
        elif model == 'Image to Video' and output_data:
            model = replicate.models.get("image-to-video/model")
            output_data = model.predict(image=output_data)
            st.video(output_data)
        
        elif model == 'Text to Video':
            text_input = st.text_area("Enter a text prompt")
            if text_input:
                model = replicate.models.get("text-to-video/model")
                output_data = model.predict(prompt=text_input)
                st.video(output_data)
        
        elif model == 'Text to Music':
            text_input = st.text_area("Enter a text prompt for music generation")
            if text_input:
                model = replicate.models.get("text-to-music/model")
                output_data = model.predict(prompt=text_input)
                st.audio(output_data)

    st.success("Pipeline executed successfully!")

# Reset pipeline
if st.button("Reset Pipeline"):
    st.session_state['pipeline'] = []
    st.success("Pipeline reset!")
