from flask import Flask, render_template, request
import os
import openai
from fractions import Fraction

openai.api_key = os.environ['API_KEY']

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['input']
    length = float(Fraction(request.form['menu']))
    len_text = len(text)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"{text}\n\nTl;dr",
        temperature=0.7,
        max_tokens=int(len_text*length*2),
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=1
    )
    return render_template('index.html', text=response.choices[0].text, inp=text)
