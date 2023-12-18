import socketio
import eventlet
import numpy as np
from flask import Flask
from keras.models import load_model
import base64
from io import BytesIO
from PIL import Image
import cv2

# Initialize SocketIO server
sio = socketio.Server()

# Create Flask application
app = Flask(__name__)

# Set a limit for the vehicle's speed
max_speed = 10

# Function to preprocess images for model prediction
def preprocess_image_for_model(image):
    # Crop, convert color, blur, resize and normalize the image
    image = image[60:135, :, :]
    image = cv2.cvtColor(image, cv2.COLOR_RGB2YUV)
    image = cv2.GaussianBlur(image, (3, 3), 0)
    image = cv2.resize(image, (200, 66))
    image = image / 255
    return image

# Handling telemetry data
@sio.on('telemetry')
def handle_telemetry(sid, data):
    current_speed = float(data['speed'])
    image = Image.open(BytesIO(base64.b64decode(data['image'])))
    image = np.asarray(image)
    image = preprocess_image_for_model(image)
    image = np.array([image])
    steering_prediction = float(model.predict(image))
    throttle_control = 1.0 - current_speed / max_speed
    print('Steering: {:.4f}, Throttle: {:.4f}, Speed: {:.2f}'.format(steering_prediction, throttle_control, current_speed))
    control_vehicle(steering_prediction, throttle_control)

# Event handler for new connections
@sio.on('connect')
def handle_connect(sid, environ):
    print('A new connection established')
    control_vehicle(0, 0)

# Function to emit control commands
def control_vehicle(steering, throttle):
    sio.emit('steer', data={
        'steering_angle': str(steering),
        'throttle': str(throttle)
    })

# Entry point of the application
if __name__ == '__main__':
    # Load the trained model
    model = load_model('model.h5')

    # Wrap Flask application with SocketIO's middleware
    app = socketio.Middleware(sio, app)

    # Deploy as an event-driven WSGI server
    eventlet.wsgi.server(eventlet.listen(('', 4567)), app)
