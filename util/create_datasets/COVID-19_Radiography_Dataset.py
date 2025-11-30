import os
import shutil
from sklearn.model_selection import train_test_split

# Define the paths to the dataset directories
dataset_dir = '/home/ahmedm04/projects/med_universal/datasets/COVID-19_Radiography_Dataset'
train_dir = '/home/ahmedm04/projects/med_universal/datasets/COVID-19_Radiography_Dataset/train'
val_dir = '/home/ahmedm04/projects/med_universal/datasets/COVID-19_Radiography_Dataset/val'

# Get the list of subdirectories in the dataset directory
subdirectories = [subdir for subdir in os.listdir(dataset_dir) if os.path.isdir(os.path.join(dataset_dir, subdir))]

# Split each subdirectory into train and val directories

for subdir in subdirectories:
    # Get the list of images in the subdirectory
    images = [image for image in os.listdir(os.path.join(dataset_dir, subdir)) if os.path.isfile(os.path.join(dataset_dir, subdir, image))]
    # Split the images into train and val sets
    train_images, val_images = train_test_split(images, test_size=0.2, random_state=42)
    # Create the train and val directories for the subdirectory
    if not os.path.exists(os.path.join(train_dir, subdir)):
        os.makedirs(os.path.join(train_dir, subdir))
    if not os.path.exists(os.path.join(val_dir, subdir)):
        os.makedirs(os.path.join(val_dir, subdir))
    # Copy the images to the train and val directories
    for image in train_images:
        shutil.copy(os.path.join(dataset_dir, subdir, image), os.path.join(train_dir, subdir, image))
    for image in val_images:
        shutil.copy(os.path.join(dataset_dir, subdir, image), os.path.join(val_dir, subdir, image))