import gradio as gr
import cv2
import os
from gradio_client import Client, handle_file
def capture_image():
    # Specify the directory where you want to save the image
    save_dir = "./"
    
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
            client = Client("facebook/VFusion3D")
            result = client.predict(
                image=handle_file(img_path),  # Ensure file path is passed here
                api_name="/step_1_generate_obj"
            )
            normalized_path = result[0].replace("\\", "/")
            print(f"3D model file saved at: {normalized_path}")
            return normalized_path
def display_3d_model(obj_file_path):
    return obj_file_path # why ? don't know, i just copy from the docs :D and it worked

# Gradio interface
with gr.Blocks(css="footer{display:none !important}", title= 'Imgto3D') as demo:
    # Display the logo in the header of the interface next to the maekdown text
    gr.Markdown(
            """
            # Image to 3D Model 
            """)
    with gr.Row():
        gr.Image(value="./Github/9.5AI_techday/logo3.png",show_label=False,width=150, height=150, show_download_button=False,show_fullscreen_button= False, container= False) # Display the logo
    with gr.Row():
        with gr.Column():
            img = gr.Image(label="Captured Image", type="filepath")  # Display captured image
            capture_btn = gr.Button("Capture Image")
            generate_btn = gr.Button("Generate 3D Model")
        with gr.Column():
            output_3d = gr.Model3D(label="3D Model Viewer", height= 400, camera_position=[-270, 180, 3])
            
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

demo.launch(allowed_paths=['./'])
