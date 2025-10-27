🌾 Rice Leaf Disease Detection (Deep Learning)
A Python project using a Convolutional Neural Network (CNN) to classify diseases in rice leaves from images. The model is deployed via a Flask web application.

🛠️ Setup & Installation
Clone Repository:

Bash

git clone https://github.com/C-H-I-R-A-N-T-H/Rice-leaf-disease-detection-by-deep-learning.git
cd Rice-leaf-disease-detection-by-deep-learning
Install Dependencies: (Ensure Python is installed)

Bash

pip install tensorflow==2.12.0 Flask==2.2.2 Werkzeug==2.2.2 pillow==9.4.0 efficientnet==1.1.1 protobuf==3.20.0 gevent==24.2.1
🚀 Usage
Run the web application to start the prediction service:

Bash

python app.py
Access the live prediction at http://127.0.0.1:5000/.

🧠 Key Technologies
Deep Learning: TensorFlow/Keras

Model: CNN (EfficientNet recommended)

Web Framework: Flask

Web Server: gevent

Image Processing: Pillow, Werkzeug
