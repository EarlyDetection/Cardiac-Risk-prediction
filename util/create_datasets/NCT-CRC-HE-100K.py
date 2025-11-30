import os
from PIL import Image

def convert_images(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".tif"):
                tif_path = os.path.join(root, file)
                png_path = os.path.splitext(tif_path)[0] + ".png"
                try:
                    with Image.open(tif_path) as img:
                        img.save(png_path, "PNG")
                    print(f"Converted {tif_path} to {png_path}")
                except Exception as e:
                    print(f"Failed to convert {tif_path}: {str(e)}")

# Convert images in the Test directory
test_directory = "/home/ahmedm04/projects/med_universal/datasets/NCT-CRC-HE-100K/Test"
convert_images(test_directory)

# Convert images in the Train directory
train_directory = "/home/ahmedm04/projects/med_universal/datasets/NCT-CRC-HE-100K/Train"
convert_images(train_directory)
