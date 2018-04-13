#Python code for localhost:7070/tflow:train
#This code will pull the iris data set from our MySQLDB container
#    and then train on it.
#References:
# https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/learn/iris.py
# https://stackoverflow.com/questions/10154633/load-csv-data-into-mysql-in-python
# https://www.kaggle.com/akashsri99/deep-learning-iris-dataset-keras
import MySQLdb #For MySQL interactions
#Various TF/Keras/Numpy imports for machine learning / array tools.
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.optimizers import Adam
from keras.utils import to_categorical
from keras.callbacks import Callback, TensorBoard
import datetime
import numpy as np

def main():
  #These values were setup in docker run command. IP can be found by running 
  #    docker inspect <container name> for db
  try:
    mydb = MySQLdb.connect(host='172.17.0.2',
        user='tfmysql',
        passwd='s0m3d0ck3rus3r',
        db='irisdb')
  except: #irisdb may resolve if ip is unavailable. #TODO improve this to be more resilient
    mydb = MySQLdb.connect(host='irisdb',
        user='tfmysql',
        passwd='s0m3d0ck3rus3r',
        db='irisdb')
  cursor = mydb.cursor()
  #Select all training and test data from irisdb
  cursor.execute("SELECT * FROM training")
  training_data = cursor.fetchall()
  training_data = list(training_data)
  cursor.execute("SELECT * FROM test")
  test_data = cursor.fetchall()
  test_data = list(test_data)
  cursor.close()
  #Setup logging for tensorboard.
  logging = ("./logs/" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
  tb = TensorBoard(log_dir=logging, histogram_freq=0, batch_size=32, write_graph=True, write_grads=True, write_images=True,
      embeddings_freq=0, embeddings_layer_names=None, embeddings_metadata=None)
  #Separate X and Y's from datasets (Features from classifications)
  x_train = []
  y_train = []
  for entry in training_data:
    x_train.append([float(entry[0]),float(entry[1]),float(entry[2]),float(entry[3])])
    y_train.append([float(entry[4])])
  x_train = np.asarray(x_train)
  y_train = np.asarray(y_train)

  x_test = []
  y_test = []
  for entry in test_data:
    x_test.append([float(entry[0]),float(entry[1]),float(entry[2]),float(entry[3])])
    y_test.append([float(entry[4])])
  x_test = np.asarray(x_test)
  y_test = np.asarray(y_test)

  #Model definition
  model = Sequential()
  model.add(Dense(32,input_shape=(4,)))
  model.add(Dense(32,activation='relu'))
  model.add(Dense(32,activation='relu'))
  model.add(Dense(32,activation='relu'))
  model.add(Dense(3,activation='softmax'))
  model.compile(Adam(lr=0.0001),'sparse_categorical_crossentropy',metrics=['accuracy'])

  model.summary() #Print output of what our neural network will look like
  pause = input("Press enter to begin training...")
  model.fit(x_train,y_train,epochs=1000,callbacks=[tb]) #Train and validate model
  out = model.evaluate(x_test,y_test)

  #Formatting for readable summary of predictions.
  print("Test Loss: " + str(out[0]) + " Test Acc: " + str(out[1]))
  y_pred = model.predict(x_test)
  y_pred = y_pred.tolist()
  x_test = x_test.tolist()
  y_test = y_test.tolist()
  print("Given:\t\t\tPredicted:\tActual:")
  for i in range(len(y_pred)):
    y_pred[i][0] = round(y_pred[i][0],2)
    y_pred[i][1] = round(y_pred[i][1],2)
    y_pred[i][2] = round(y_pred[i][2],2)
    y_pred[i] = [x_test[i], y_pred[i], y_test[i]]
    print(y_pred[i])

main()





