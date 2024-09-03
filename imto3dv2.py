import gradio as gr
import cv2
import os
from gradio_client import Client, handle_file

# Function to capture image from laptop camera and save it to a file
import os
import cv2

def capture_image():
    # Specify the directory where you want to save the image
    save_dir = "C:/Users/quang/Downloads"
    
    # Create the directory if it doesn't exist
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # The filename of the captured image
    img_filename = "captured_image.png"
    
    # Full path to the image file
    img_path = os.path.join(save_dir, img_filename)

    # Capture the image from the webcam
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(img_path, frame)  # Save the image to the specified path
        cap.release()
        print(f"Image successfully captured and saved at: {img_path}")
        return img_path  # Return the full file path
    
    cap.release()
    print("Error: Failed to capture the image.")
    return None

# Function to send the image via API and get 3D model path
def generate_3d_model(img_path):
    if img_path and isinstance(img_path, str):
        print(f"Sending image file at {img_path} to the API...")
        try:
            client = Client("facebook/VFusion3D")
            result = client.predict(
                image=handle_file(img_path),  # Ensure file path is passed here
                api_name="/step_1_generate_obj"
            )
            normalized_path = result[0].replace("\\", "/")
            print(f"3D model file saved at: {normalized_path}")
            return normalized_path
        except Exception as e:
            print(f"Error occurred during API call: {e}")
            return None
    else:
        print(f"Invalid image path: {img_path}")
        return None
# Function to create a pythreejs scene for the 3D model
def display_3d_model(obj_file_path):
    # Simply return the path to the 3D model file
    return obj_file_path

# Gradio interface
with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            img = gr.Image(label="Captured Image", type="filepath")  # Display captured image
            capture_btn = gr.Button("Capture Image")
            generate_btn = gr.Button("Generate 3D Model")
        with gr.Column():
            output_3d = gr.Model3D(label="3D Model Viewer")
            
    def capture_and_display():
        img_path = capture_image()
        if img_path:
            return img_path  # Return the file path as a string
        return None

    
    def generate_and_display(img_file):
        img_path = img_file
        obj_path = generate_3d_model(img_path)
        if obj_path:
            return obj_path  # Return the path of the 3D model
        return None
    
    capture_btn.click(capture_and_display, inputs=None, outputs=img)
    generate_btn.click(generate_and_display, inputs=img, outputs=output_3d)

demo.launch()
