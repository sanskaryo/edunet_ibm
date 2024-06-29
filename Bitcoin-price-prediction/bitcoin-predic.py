import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style
import seaborn as sns
sns.set_style('darkgrid')

from keras.models import Sequential
from keras.callbacks import EarlyStopping
from keras.layers import Dense, Dropout, Activation, Flatten, LSTM

from sklearn.preprocessing import MinMaxScaler