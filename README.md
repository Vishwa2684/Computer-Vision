# Computer Vision Projects

## Cat and dog classification
- To get cats and dogs dataset 
   [click here](https://www.microsoft.com/en-us/download/confirmation.aspx?id=54765)
- Wrote a Python script to get proper images from the image dataset and store them in a list. Then pickle the list to use the clean images for CNN.
- For CNN I used Keras libaray by tensorflow. Then the images are normalized in range of 0 to 1.
- Then the images are trained in CNN. The layers of CNN are:

| Layers    | Parameters |
| :--------: | :-------: |
| Conv2D  | input image size=(50,50), kernel size=3, activation function = ReLU, neurons = 64  |
| MaxPool2D | pool size = (2,2)     |
| Conv2D  |  kernel size=3, activation function = ReLU, neurons = 64  |
| MaxPool2D | pool size = (2,2)     |
|Flatten| None|
|Dense| neurons = 64|
|Dense| neurns = 1, activation function = Sigmoid|
- The last dense layer is used to give output for the input image.
- The model yields 82% accuracy as it is a simple CNN.

## Image Segmentation
- This project uses OpenCV to segment images.
