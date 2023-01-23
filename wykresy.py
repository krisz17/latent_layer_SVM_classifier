"""
Definiuję klasę do generowania wykresów porównawczych modelu SVC z scaterplotem w warstwie ukrytej
Problem dotyczy klasyfikowania odręcznie pisanych cyfr czyli mnist10

"""

import os
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt


class latent_SVM():
    def load_mnist10():
        from keras.datasets import mnist 
        (x_train, y_train), (x_test, y_test) = mnist.load_data()
        x_train = x_train.astype('float32') / 255.
        x_train = x_train.reshape(x_train.shape + (1,))
        x_test = x_test.astype('float32') / 255.
        x_test = x_test.reshape(x_test.shape + (1,))
    return (x_train, y_train), (x_test, y_test)


