
# Multi-Modal Interactive AI Pipeline Builder

## Overview
This project is a comprehensive tool to visually build AI pipelines using multi-modal nodes such as text, image, video, and more. 
It integrates **Streamlit**, **Replicate API**, and **React-flow** for interactive workflow creation and seamless AI model integration.

### Key Features:
1. Split-screen layout with a node palette and workflow canvas.
2. Drag-and-drop nodes with adjustable parameters.
3. Real-time execution of AI models via Replicate API.
4. Handling multi-modal inputs and outputs.
5. Export functionality for workflows and generated outputs.

## How to Use
1. Enter your Replicate API key when prompted.
2. Add nodes from the sidebar to the interactive canvas.
3. Connect nodes and adjust parameters to build your AI pipeline.
4. Execute the workflow and view the outputs directly in the app.
5. Export the workflow or outputs as needed.

## Installation

```bash
pip install -r requirements.txt
```

Then run the app using Streamlit:
```bash
streamlit run scripts/app.py
```

## Requirements
- Python 3.8+
- Streamlit
- Replicate API key (Create an account at [Replicate](https://replicate.com/))

## Features
- **Node Palette**: Drag AI nodes such as text-to-image, upscaling, etc.
- **Workflow Canvas**: Interactively connect and manipulate nodes.
- **Replicate Integration**: Leverage AI models for various media types.
