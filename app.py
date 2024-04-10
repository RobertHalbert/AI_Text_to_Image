from flask import Flask, render_template, request
from transformers import pipeline
app = Flask(__name__)


@app.route("/", methods=['POST','GET'])
def ChatProgram():
    if request.method == 'GET':
        return render_template("index.html")  
    else:
        user_input = request.form['question']
        if user_input != "":
            response = AIResponse(user_input)
            return render_template("index.html", question = user_input, answer = response[0]["generated_text"].capitalize())
        else: 
            return render_template("index.html")
        
        
def AIResponse(user_input):
   image_to_text = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")
   return image_to_text(user_input)