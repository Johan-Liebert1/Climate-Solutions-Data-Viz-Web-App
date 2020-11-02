from os.path import dirname
from flask import Flask, send_file
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

def plot(num):
    dirname = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    save_path = os.path.join(dirname, 'frontend', 'public')

    x = [i for i in range(-100, 100)]
    y = [i**num for i in x]
    filename = f'{num}.png'

    fig, ax = plt.subplots(1,1)

    ax.plot(x, y)
    # fig.savefig(filename)

    del fig, ax

    return filename


@app.route('/')
def home():
    return {"message": "you've reached home"}

@app.route('/<string:power>')
def root(power):
    file_name = plot(int(power))

    return send_file(file_name, mimetype='image/gif'), 200

if __name__ == "__main__":
    app.run(debug = True)