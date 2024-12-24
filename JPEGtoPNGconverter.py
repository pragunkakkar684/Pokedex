import sys
import os
from PIL import Image

if len(sys.argv) < 3:
    print("Usage: python JPEGtoPNGconverter.py <source_folder> <output_folder>")
    sys.exit(1)

path = sys.argv[1]
directory = sys.argv[2]

if not os.path.exists(directory):
    os.makedirs(directory)

if not any(os.scandir(path)):
    print(f"No images found in the source folder '{path}'.")
    sys.exit(1)

for filename in os.listdir(path):
    if filename.lower().endswith(('.jpg', '.jpeg')):
        clean_name = os.path.splitext(filename)[0]
        img = Image.open(f'{path}/{filename}')
        img.save(f'{directory}/{clean_name}.png', 'PNG')
        print(f'{filename} converted to {clean_name}.png')

