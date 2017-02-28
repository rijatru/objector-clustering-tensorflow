import numpy as np
import tensorflow as tf
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route('/')
def main():
    return 'OK!'

if __name__ == '__main__':
    app.run(debug=True)
