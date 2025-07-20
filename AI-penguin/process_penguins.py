import os
import json
from PIL import Image
import numpy as np

def convert_image_to_canvas_data(image_path):
    """
    Loads an image, resizes it to 128x128, converts it to RGBA,
    and returns a flattened list of pixel data suitable for canvas_data.
    """
    try:
        img = Image.open(image_path)
        # Resize the image to 128x128
        img = img.resize((128, 128), Image.Resampling.LANCZOS)
        # Convert to RGBA format (if not already)
        img = img.convert("RGBA")
        # Get pixel data as a numpy array
        data_array = np.array(img, dtype=np.uint8)
        # Flatten the array to a 1D list
        # The judge.py expects a flat array of RGBA values
        flattened_data = data_array.flatten().tolist()
        return flattened_data
    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    penguin_dir = "D:/art/Public/penguins"
    output_json_dir = "D:/art/Public/output_json"

    # Create output directory if it doesn't exist
    os.makedirs(output_json_dir, exist_ok=True)

    for filename in os.listdir(penguin_dir):
        if filename.lower().endswith((
            '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp', '.avif')):
            image_path = os.path.join(penguin_dir, filename)
            print(f"Processing {image_path}...")
            canvas_data = convert_image_to_canvas_data(image_path)
            if canvas_data:
                json_filename = os.path.splitext(filename)[0] + ".json"
                output_json_path = os.path.join(output_json_dir, json_filename)
                with open(output_json_path, "w") as f:
                    json.dump({"canvas_data": canvas_data}, f)
                print(f"Saved canvas data to {output_json_path}")
            else:
                print(f"Failed to convert {filename}")
    print("All eligible images processed.")
