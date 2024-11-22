Image Resizer:-
This Python script resizes images in a specified directory and saves the resized images in a specified output directory. It allows for scaling up or down by a user-defined factor, supports multiple image formats, and enables configuration for image quality and format (JPEG, PNG, etc.).

Features:-
Flexible Resizing: Resizes images in bulk by a specified scaling factor.
Output Format and Quality: Allows configuration of the output format (e.g., JPEG) and quality.
Handles Transparency: Converts RGBA images to RGB to support formats like JPEG that do not handle transparency.

Folder Structure:-
After executing the script, your directory structure may look like this:

project-folder/
├── input/
│   ├── image1.png
│   ├── image2.jpg
│   └── ...
└── output/
    ├── image1.png
    ├── image2.jpg
    └── ...

Usage:-
Requirements-
Python 3.x
Pillow library for image processing.
Installation
To install the required library, use:

-pip install pillow
-How to Use:-
Specify Input and Output Directories: Update the paths for the input and output directories in the script.

input_directory = "path/to/input_folder"
output_directory = "path/to/output_folder"
Set Scaling Factor, Format, and Quality: Define the scale_factor (e.g., 0.5 to reduce by half or 2 to double), output format (e.g., JPEG), and quality (1-100 for JPEG images).

scale_factor = 0.5  - for scaling down
resize_images(input_directory, output_directory, scale_factor, format='JPEG', quality=85)
Run the Script: Execute the script to resize the images.

-python image_resizer.py

Code Overview:-
The main function, resize_images(), iterates over each image file in the specified input directory, applies the scaling factor, and saves the resized image in the output directory with the specified format and quality. It handles:

Image Format Support: Works with PNG, JPEG, BMP, GIF, and other common formats.
Transparency Handling: Converts RGBA images to RGB if the output format doesn’t support transparency (like JPEG).
Example:-
Here’s an example of the initial and resized images:

Initial Directory
Place images to be resized in the specified input folder:


Resized Images
After running the script, the resized images will be saved in the output folder:

sample images:-

1.-
Image before scaling
![witcher](https://github.com/user-attachments/assets/87a8cf5b-8762-41ff-8cb1-59c2307ac182)
2.-
Image before scaling
![venom](https://github.com/user-attachments/assets/b69f04e1-dff9-4c75-8e59-8b181ef5f821)
3.-
Image after scaling factor of 5 i.e *5
![witcher](https://github.com/user-attachments/assets/04c8e09e-7f92-40cd-90c6-a5fd0ed93b6f)
4.-
Image after scaling factor of 5 i.e *5
![venom](https://github.com/user-attachments/assets/ebf4273a-eced-4b0a-a44b-fecd36a58cfb)
