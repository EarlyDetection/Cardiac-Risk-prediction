# https://www.kaggle.com/datasets/paultimothymooney/breast-histopathology-images/data
import os
base_dir = '/home/ahmedm04/projects/med_universal/datasets/IDC/'
base_dir = os.path.join(base_dir, 'IDC_regular_ps50_idx5')
test_size = 0.3

#make dir for Train and Test 
train_dir = os.path.join(base_dir, 'Train')
#os.mkdir(train_dir)
test_dir = os.path.join(base_dir, 'Test')
#os.mkdir(test_dir)

# inside Train and Test make dir for 0 and 1
train_0_dir = os.path.join(train_dir, '0')
#os.mkdir(train_0_dir)
train_1_dir = os.path.join(train_dir, '1')
#os.mkdir(train_1_dir)

test_0_dir = os.path.join(test_dir, '0')
#os.mkdir(test_0_dir)
test_1_dir = os.path.join(test_dir, '1')
#os.mkdir(test_1_dir)

# split patient dirs into train and test dirs
#patient_dirs = [file for file in os.listdir(base_dir) if file != 'Train' and file != 'Test']
#test_dirs = patient_dirs[:int(len(patient_dirs)*test_size)]
test_dirs = os.listdir(os.path.join(base_dir, 'Test'))
#train_dirs = patient_dirs[int(len(patient_dirs)*test_size):]
train_dirs = os.listdir(os.path.join(base_dir, 'Train'))


# move the test and train dirs into the corresponding dirs
#for file in test_dirs:
#    os.rename(os.path.join(base_dir, file), os.path.join(test_dir, file))

#for file in train_dirs:
#    os.rename(os.path.join(base_dir, file), os.path.join(train_dir, file))

# move the images into the corresponding dirs each dir is a patient and has two sub dirs 0 and 1
for file in os.listdir(train_dir):
    if file == '0' or file == '1':
        continue
    patient_dir = os.path.join(train_dir, file)
    pos, neg = os.listdir(patient_dir)
    for img in os.listdir(os.path.join(patient_dir, neg)):
        os.rename(os.path.join(patient_dir, neg, img), os.path.join(train_0_dir, img))
    for img in os.listdir(os.path.join(patient_dir, pos)):
        os.rename(os.path.join(patient_dir, pos, img), os.path.join(train_1_dir, img))
    #delete the patient dir
    os.rmdir(patient_dir)

for file in os.listdir(test_dir):
    if file == '0' or file == '1':
        continue
    patient_dir = os.path.join(test_dir, file)
    pos, neg = os.listdir(patient_dir)
    for img in os.listdir(os.path.join(patient_dir, neg)):
        os.rename(os.path.join(patient_dir, neg, img), os.path.join(test_0_dir, img))
    for img in os.listdir(os.path.join(patient_dir, pos)):
        os.rename(os.path.join(patient_dir, pos, img), os.path.join(test_1_dir, img))
    #delete the patient dir
    os.rmdir(patient_dir)
