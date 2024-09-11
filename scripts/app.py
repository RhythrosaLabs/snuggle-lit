
import streamlit as st
import os

# Initialize session state for pipeline if not already present
if 'pipeline' not in st.session_state:
    st.session_state['pipeline'] = []

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
    
    elif model_category == "Image":
        selected_model = st.sidebar.selectbox("Choose a model", ["Stable Diffusion (Text-to-Image)", "Upscale Image", "Remove Background", "Super Resolution"])

    elif model_category == "Video":
        selected_model = st.sidebar.selectbox("Choose a model", ["Image-to-Video", "Text-to-Video"])

    elif model_category == "Audio":
        selected_model = st.sidebar.selectbox("Choose a model", ["Text-to-Music", "Voice Generation", "Audio Enhancement"])

    if st.sidebar.button("Add Model to Pipeline"):
        # Add the selected model to the pipeline
        st.session_state['pipeline'].append(selected_model)
        st.sidebar.success(f"Added {selected_model} to the pipeline!")

# Tab 3: Node Properties
elif tabs == "Node Properties":
    st.sidebar.subheader("Node Properties")
    if len(st.session_state['pipeline']) == 0:
        st.write("No models in the pipeline yet. Go to 'Model Selection' to add some.")
    else:
        # Display the models added to the pipeline
        for idx, model in enumerate(st.session_state['pipeline'], start=1):
            st.write(f"Node {idx}: {model}")
            
            # Display parameters for each model
            if model == "LLaMA (Text Generation)":
                st.slider(f"Node {idx} - Temperature", 0.1, 1.0, 0.7, step=0.1)
                st.slider(f"Node {idx} - Max Tokens", 50, 500, 150, step=10)
                st.checkbox(f"Node {idx} - Top-P Sampling", value=True)
                st.slider(f"Node {idx} - Top-P Value", 0.1, 1.0, 0.9, step=0.1)

            elif model == "Stable Diffusion (Text-to-Image)":
                st.slider(f"Node {idx} - Prompt Strength", 0.0, 1.0, 0.8, step=0.1)
                st.slider(f"Node {idx} - Image Resolution", 256, 1024, 512, step=128)
                st.slider(f"Node {idx} - Guidance Scale", 1.0, 10.0, 7.5, step=0.5)
                st.slider(f"Node {idx} - Steps", 10, 100, 50, step=5)

            elif model == "Upscale Image":
                st.slider(f"Node {idx} - Scale Factor", 2, 4, 2, step=1)
                st.slider(f"Node {idx} - Denoise Strength", 0.0, 1.0, 0.5, step=0.1)

            elif model == "Remove Background":
                st.slider(f"Node {idx} - Threshold", 0.0, 1.0, 0.5, step=0.1)

            elif model == "Super Resolution":
                st.slider(f"Node {idx} - Scale Factor", 2, 4, 2, step=1)
                st.slider(f"Node {idx} - Denoise Strength", 0.0, 1.0, 0.5, step=0.1)

            elif model == "Text-to-Video":
                st.text_area(f"Node {idx} - Enter a prompt for video generation")
                st.slider(f"Node {idx} - Duration", 1, 30, 10, step=1)
                st.slider(f"Node {idx} - Frame Rate", 10, 60, 24, step=2)

            elif model == "Image-to-Video":
                st.slider(f"Node {idx} - Duration", 1, 30, 10, step=1)
                st.slider(f"Node {idx} - Frame Rate", 10, 60, 24, step=2)

            elif model == "Text-to-Music":
                st.text_area(f"Node {idx} - Enter a prompt for music generation")
                st.slider(f"Node {idx} - Duration", 10, 300, 120, step=10)
                st.selectbox(f"Node {idx} - Genre", ["Classical", "Pop", "Rock", "Electronic"])

            elif model == "Voice Generation":
                st.text_area(f"Node {idx} - Enter text to convert to voice")
                st.selectbox(f"Node {idx} - Voice Style", ["Formal", "Casual", "Serious", "Happy"])
                st.slider(f"Node {idx} - Pitch", 0.5, 2.0, 1.0, step=0.1)
                st.slider(f"Node {idx} - Speed", 0.5, 2.0, 1.0, step=0.1)

            elif model == "Audio Enhancement":
                st.slider(f"Node {idx} - Noise Reduction Level", 0.0, 1.0, 0.5, step=0.1)
                st.slider(f"Node {idx} - Gain Control", -10, 10, 0, step=1)

# Input Section: Text or Image input as the base
st.subheader("Pipeline Input")
input_type = st.radio("Choose input type", ["Text", "Image"])

if input_type == "Text":
    user_input_text = st.text_area("Enter your text input for the pipeline")
elif input_type == "Image":
    user_input_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Run the Pipeline Button
if st.button("Run Pipeline"):
    st.write("Running pipeline...")
    
    # Dummy processing flow for text input pipeline
    if input_type == "Text" and user_input_text:
        result = user_input_text
        for model in st.session_state['pipeline']:
            st.write(f"Processing {model}...")
            # Dummy process for each model
            result += f" -> Processed by {model}"
        st.write(f"Final output: {result}")

    # Dummy processing flow for image input pipeline
    elif input_type == "Image" and user_input_image:
        st.write(f"Processing image: {user_input_image.name}")
        for model in st.session_state['pipeline']:
            st.write(f"Processing {model}...")
            # Dummy image process for each model (In reality, you'd run model predictions)
            st.write(f"Image processed by {model}")
        st.image(user_input_image, caption="Final Processed Image")

# Display the current pipeline as a list of models added
st.subheader("Current Pipeline")
if st.session_state['pipeline']:
    for i, model in enumerate(st.session_state['pipeline'], start=1):
        st.write(f"Step {i}: {model}")
else:
    st.write("No models in the pipeline yet.")
