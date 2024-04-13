
import os
from PIL import Image
def preprocess_image(image_path, target_size=(255, 255)):
   
    img = Image.open(image_path)
    width, height = img.size
    aspect_ratio = width / height
    
    target_width, target_height = target_size
    target_aspect_ratio = target_width / target_height
    
    if aspect_ratio > target_aspect_ratio:
        new_width = int(target_height * aspect_ratio)
        new_height = target_height
    else:
        new_width = target_width
        new_height = int(target_width / aspect_ratio)
    img = img.resize((new_width, new_height), resample=Image.BICUBIC)
    crop_left = (new_width - target_width) // 2
    crop_top = (new_height - target_height) // 2
    crop_box = (crop_left, crop_top, crop_left + target_width, crop_top + target_height)
    img = img.crop(crop_box)
    
    return img

def preprocess_and_save_images(input_folder, output_folder, target_size=(255, 255), image_format='JPEG'):
    os.makedirs(output_folder, exist_ok=True)
    files = os.listdir(input_folder)
    for file in files:
        try:
            img_path = os.path.join(input_folder, file)
            img = preprocess_image(img_path, target_size)
            output_path = os.path.join(output_folder, file)
            img.save(output_path, format=image_format)
            print(f"Saved preprocessed image: {output_path}")
        except Exception as e:
            print(f"Error processing '{file}': {e}")