"""
Definiuję klasę do generowania wykresów porównawczych modelu SVC z scaterplotem w warstwie ukrytej
Problem dotyczy klasyfikowania odręcznie pisanych cyfr czyli mnist10

"""

import os
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
from models.AE import Autoencoder
from keras.datasets import mnist 

from models.AE import Autoencoder

class latent_SVM():
    def _load_mnist10(self):
        (self.x_train, self.y_train), (self.x_test, self.y_test) = mnist.load_data()
        self.x_train = self.x_train.astype('float32') / 255.
        self.x_train = self.x_train.reshape(x_train.shape + (1,))
        self.x_test = self.x_test.astype('float32') / 255.
        self.x_test = self.x_test.reshape(x_test.shape + (1,))

    def __init__(self, section = 'vae', run_id = '0001', data_name= 'digits', run_folder=None, MODE = 'build'):
        self._load_mnist10
        self.SECTION = section
        self.RUN_ID = run_id
        self.DATA_NAME = data_name
        if run_folder is None:
            self.RUN_FOLDER = 'run/{}/'.format(self.SECTION)
            self.RUN_FOLDER += '_'.join([self.RUN_ID, self.DATA_NAME])
        if not os.path.exists(self.RUN_FOLDER):
            os.mkdir(self.RUN_FOLDER)
            os.mkdir(os.path.join(self.RUN_FOLDER, 'viz'))
            os.mkdir(os.path.join(self.RUN_FOLDER, 'images'))
            os.mkdir(os.path.join(self.RUN_FOLDER, 'weights'))
        self.MODE = MODE

    def AE(self):
        

    


