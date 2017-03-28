import numpy as np
import tensorflow as tf
from flask import Flask, jsonify, render_template, request
from tensorflow_app import tf_method as method

app = Flask(__name__)


@app.route('/')
def main():
    return method()


if __name__ == '__main__':
    app.run(debug=True)
