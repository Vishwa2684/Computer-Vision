"""
To get the dataset go to the below link:
https://www.microsoft.com/en-us/download/confirmation.aspx?id=54765    
"""

import cv2
import os
import pickle

curdir =os.path.join(os.getcwd(),'PetImages') 

categories = ['Cat','Dog'] 

training_data = []

i=0 # i to check where resizing fails
IMG_SIZE = 50 #You can set any image size you like
def create_training_data(i):
    for c in categories:
        path = os.path.join(curdir,c)
        class_num = categories.index(c)
        
        for img in os.listdir(path):
            # Handling exception in this dataset because some images are broken in it
            try:
                img_array = cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
                new_img = cv2.resize(img_array,(IMG_SIZE,IMG_SIZE))
                training_data.append([new_img,class_num])
                i+=1
            except Exception:
                print(f'failed to resize: {i}')

create_training_data(i) 

# Save the list of image and label in .pkl format
with open('training_data.pkl','wb')as b:
    pickle.dump(training_data,b)