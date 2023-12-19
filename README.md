# Autonomous Driving using Behavioral Cloning

## Project Overview

This project demonstrates the application of deep learning in autonomous driving. By employing a convolutional neural network (CNN), the system learns to steer a car autonomously in a simulated environment. The project is structured into key phases: data preparation, model training, and real-time vehicle control.

## Key Features

Image Preprocessing: Implemented techniques such as cropping images by 40%, resizing to 200x66 pixels, and normalizing to facilitate efficient model training in a Google Colab GPU environment.

Data Augmentation: Applied on-the-fly augmentation strategies like random zoom, pan, and brightness adjustments to the training set, significantly enhancing the model's robustness under varying lighting and environmental conditions.

Model Architecture: Leveraged NVIDIA's ["End-to-end Learning for Self-Driving Cars"](https://images.nvidia.com/content/tegra/automotive/images/2016/solutions/pdf/end-to-end-dl-using-px.pdf) architecture to construct a model with 252,219 trainable parameters, ensuring detailed feature extraction and effective learning.

Flask Server for Telemetry Data: Developed a Flask server using Visual Studio Code to process real-time telemetry data from the Udacity simulator. The server dynamically manages vehicle control by adjusting the steering angle and throttle based on the model's predictions.

Speed Optimization: Fine-tuned the model to maintain a controlled speed limit, ensuring the vehicle's speed stays below 10 mph for stable and safe autonomous navigation.

## Training Details

Dataset: Utilized a dataset of 5,305 driving images from the Udacity simulator, balanced to mitigate straight-driving bias.

Training Environment: The model was trained in a Google Colab environment, taking advantage of GPU acceleration for efficient computation.

Validation Loss: Achieved a validation loss of 0.0368 after 10 epochs, indicating a high degree of accuracy in the model's predictions.


## Demo 

Autonomous Driving on known track

![Demo1](https://github.com/AryanKumarNadipally/Autonomous-Driving-using-Behavioral-Cloning/assets/143588978/9790f97e-f941-4008-ad68-83558565493d)


Autonomous Driving on Unknown Track

![Demo2](https://github.com/AryanKumarNadipally/Autonomous-Driving-using-Behavioral-Cloning/assets/143588978/8b4acfa8-ecd4-4671-b501-c2f09c1a155d)


## Acknowledgements

This work was inspired by NVIDIA's pioneering research in autonomous vehicles and the supportive open-source community that has built tools enabling this project.

## License

The source code is released under the MIT license.
