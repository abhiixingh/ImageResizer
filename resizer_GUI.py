from PIL import Image
import os
from tkinter import Tk, Label, Entry, Button, filedialog, StringVar, messagebox

def resize_images(file_paths, out_dir, scale_factor, format='JPEG', quality=85):
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    for img_path in file_paths:
        img_name = os.path.basename(img_path)
        if os.path.isfile(img_path) and img_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            with Image.open(img_path) as img:
                if img.mode == 'RGBA':
                    img = img.convert('RGB')

                new_width = int(img.width * scale_factor)
                new_height = int(img.height * scale_factor)

                resized_img = img.resize((new_width, new_height), resample=Image.LANCZOS)

                output_path = os.path.join(out_dir, img_name)

                if format.upper() in ['JPEG', 'JPG']:
                    resized_img.save(output_path, format='JPEG', quality=quality)
                else:
                    resized_img.save(output_path)

                print(f"Saved {img_name} to {output_path} with {format} format and quality {quality}")

def select_input_files():
    file_paths = filedialog.askopenfilenames(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    input_files.set(file_paths)

def select_output_directory():
    dir_path = filedialog.askdirectory()
    output_dir.set(dir_path)

def start_resizing():
    files = input_files.get().split(';')
    out_dir = output_dir.get()
    scale = float(scale_factor.get())
    img_format = format_var.get()
    quality = int(quality_var.get())

    if not files or not out_dir or scale <= 0:
        messagebox.showerror("Error", "Please provide valid inputs!")
        return

    try:
        resize_images(files, out_dir, scale, format=img_format, quality=quality)
        messagebox.showinfo("Success", "Images resized successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Tkinter GUI setup
root = Tk()
root.title("Image Resizer")

input_files = StringVar()
output_dir = StringVar()
scale_factor = StringVar(value="1.0")
format_var = StringVar(value="JPEG")
quality_var = StringVar(value="85")

Label(root, text="Select Images:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
Button(root, text="Browse", command=select_input_files).grid(row=0, column=1, padx=10, pady=5)

Label(root, text="Output Directory:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
Entry(root, textvariable=output_dir, width=40).grid(row=1, column=1, padx=10, pady=5)
Button(root, text="Browse", command=select_output_directory).grid(row=1, column=2, padx=10, pady=5)

Label(root, text="Scale Factor:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
Entry(root, textvariable=scale_factor, width=10).grid(row=2, column=1, padx=10, pady=5, sticky="w")

Label(root, text="Output Format:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
Entry(root, textvariable=format_var, width=10).grid(row=3, column=1, padx=10, pady=5, sticky="w")

Label(root, text="Quality (1-100):").grid(row=4, column=0, padx=10, pady=5, sticky="w")
Entry(root, textvariable=quality_var, width=10).grid(row=4, column=1, padx=10, pady=5, sticky="w")

Button(root, text="Start Resizing", command=start_resizing).grid(row=5, column=1, pady=10)

root.mainloop()
