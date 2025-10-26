#!/usr/bin/env python
from flask import Flask, render_template, request
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
 
import numpy as np
 
import efficientnet.tfkeras as efn


app = Flask(__name__)
verbose_name = {
0: "Bacterial leaf blight",
1: "BrownSpot",
2: "Healthy",
3: "LeafBlast" 

}

 

model = load_model('efficient.h5')

def predict_label(img_path):
	test_image = image.load_img(img_path, target_size=(224,224))
	test_image = image.img_to_array(test_image)/255.0
	test_image = test_image.reshape(1, 224,224,3)

	predict_x=model.predict(test_image) 
	classes_x=np.argmax(predict_x,axis=1)
	
	return verbose_name [classes_x[0]]
 

# Load your trained model
 


@app.route("/")
@app.route("/first")
def first():
	return render_template('first.html')
    
@app.route("/login")
def login():
	return render_template('login.html')    
@app.route("/chart")
def chart():
	return render_template('chart.html')

@app.route("/performance")
def performance():
	return render_template('performance.html')

@app.route("/index", methods=['GET', 'POST'])
def index():
	return render_template("index.html")


@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		img = request.files['my_image']

		img_path = "static/tests/" + img.filename	
		img.save(img_path)
		#plt.imshow(img)
		predict_result = predict_label(img_path)


		 

	
	return render_template("result.html", prediction = predict_result, img_path = img_path)
 
 
if __name__ == '__main__':
    app.run(debug=True, port=7000)

