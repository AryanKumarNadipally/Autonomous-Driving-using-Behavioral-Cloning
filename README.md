# Autonomous Driving using Behavioral Cloning

This project uses deep learning to simulate autonomous driving through behavioral cloning, employing a convolutional neural network (CNN) that maps raw pixels from front-facing camera images to steering commands.

## Overview

The CNN model, inspired by NVIDIA's architecture, is trained on images captured from three camera angles (center, left, and right) alongside driving parameters such as steering angle, throttle, and speed. The trained model then predicts steering angles to autonomously navigate a car on a track.

## Dataset

The training data consists of images from a Udacity car simulator, annotated with corresponding driving parameters.

## Development Environments

- **Model Training**: The model was trained in [Google Colab](https://colab.research.google.com/), which provides a powerful GPU-accelerated environment.
- **Flask Server**: The server application, written in Flask, was developed using [Visual Studio Code](https://code.visualstudio.com/), an extensible code editor.

## Preprocessing

Images undergo preprocessing to ensure the neural network receives data in the correct format. This involves cropping irrelevant sections, normalizing pixel values, and resizing images for the model input.

## Model Architecture

The project uses a model architecture similar to the one described by NVIDIA in their self-driving car paper([End to End Learning for Self-Driving Cars](https://images.nvidia.com/content/tegra/automotive/images/2016/solutions/pdf/end-to-end-dl-using-px.pdf)). The model comprises several convolutional layers followed by fully connected layers, with dropout for regularization.

## Data Augmentation

Data augmentation techniques such as random zooms, pans, and brightness adjustments are applied to the training data to help the model generalize better to unseen road conditions.

## Flask Server

The Flask server acts as an intermediary between the trained model and the car simulator. It processes the telemetry data from the simulator, runs the model prediction, and sends back steering and throttle commands.

## Results

After training, the model successfully drives the car autonomously around the track without leaving the road.

## Demo 

![Demo video (3)](https://github.com/AryanKumarNadipally/Autonomous-Driving-using-Behavioral-Cloning/assets/143588978/2d8790c6-a5e4-4314-b85a-8e131ff78398)

![Demo video](https://github.com/AryanKumarNadipally/Autonomous-Driving-using-Behavioral-Cloning/assets/143588978/0e54a67f-d1b0-4742-8ba7-6e419ed56cbb)

## Acknowledgements

This work was inspired by NVIDIA's pioneering research in autonomous vehicles and the supportive open-source community that has built tools enabling this project.

## License

The source code is released under the MIT license.
