from PIL import Image
import os

def resize_images(in_dir, out_dir, scale_factor, format='JPEG', quality=85):
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    for img_name in os.listdir(in_dir):
        img_path = os.path.join(in_dir, img_name)

        if os.path.isfile(img_path) and img_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            with Image.open(img_path) as img:
                
                if img.mode == 'RGBA':
                    img = img.convert('RGB')

                new_width = int(img.width * scale_factor)
                new_height = int(img.height * scale_factor)

                resized_img = img.resize((new_width, new_height), resample=Image.LANCZOS)

                output_path = os.path.join(out_dir, img_name)

                
                if format.upper() == 'JPEG' or format.upper() == 'JPG':
                    resized_img.save(output_path, format='JPEG', quality=quality)
                else:
                    resized_img.save(output_path)

                print(f"Saved {img_name} to {output_path} with {format} format and quality {quality}")

input_directory = "D:/UPES/Sem 1/DSA/New folder/img"
output_directory = "D:/UPES/Sem 1/DSA/New folder/img"
scale_factor = 5
resize_images(input_directory, output_directory, scale_factor, format='JPEG', quality=100)
