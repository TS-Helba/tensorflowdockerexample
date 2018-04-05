#Python code for localhost:7070/tflow:dbloader
#Refer to https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/learn/iris.py
import os
import urllib.request
import tensorflow as tf
import csv

IRIS_TRAINING = 'iris_training.csv'
IRIS_TRAINING_URL = 'http://download.tensorflow.org/data/iris_training.csv'

IRIS_TEST = 'iris_test.csv'
IRIS_TEST_URL = 'http://download.tensorflow.org/data/iris_test.csv'
FEATURE_KEYS = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

def maybe_download_iris_data(file_name, download_url):
  """Downloads the file and returns the number of data."""
  if not os.path.exists(file_name):
    raw = urllib.request.urlopen(download_url).read()
    with open(file_name, 'wb') as f1:
      f1.write(raw)
  data = []
  # The first line is a comma-separated string. The first one is the number of
  # total data in the file.
  with open(file_name, 'r') as f2:
    reader = csv.reader(f2)
    data = list(reader)
  data[0][0] = FEATURE_KEYS[0]
  data[0][1] = FEATURE_KEYS[1]
  data[0][2] = FEATURE_KEYS[2]
  data[0][3] = FEATURE_KEYS[3]
  data[0][4] = "setosa-versicolor-virginica"
  return data

def main():
  training_data = maybe_download_iris_data(IRIS_TRAINING, IRIS_TRAINING_URL)
  test_data = maybe_download_iris_data(IRIS_TEST, IRIS_TEST_URL)
  print(repr(num_training_data)) #TODO: Pass this data to mysql container
main()
