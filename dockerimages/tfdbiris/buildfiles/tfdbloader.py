#Python code for localhost:7070/tflow:dbloader
#This code will download the iris dataset that tensorflow uses for tutorials
#    and then push it to our MySQLDB container for later use in ML training.
#References:
# https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/learn/iris.py
# https://stackoverflow.com/questions/10154633/load-csv-data-into-mysql-in-python

import os #For file IO
import urllib.request #For downloading iris dataset
import MySQLdb #For MySQL interactions
import csv #To open iris dataset

#Filenames / sources of iris datasets
IRIS_TRAINING = 'iris_training.csv'
IRIS_TRAINING_URL = 'http://download.tensorflow.org/data/iris_training.csv'
IRIS_TEST = 'iris_test.csv'
IRIS_TEST_URL = 'http://download.tensorflow.org/data/iris_test.csv'

#Downloads the file at the given url and saves it with given filename
#It then returns the data contained within the csv file.
def downloaddata(file_name, download_url):
  if not os.path.exists(file_name):
    raw = urllib.request.urlopen(download_url).read()
    with open(file_name, 'wb') as f1:
      f1.write(raw)
  data = []
  with open(file_name, 'r') as f2:
    reader = csv.reader(f2)
    data = list(reader)
  data.pop(0) #Pop the header
  return data

def main():
  #Download, open and save datasets
  training_data = downloaddata(IRIS_TRAINING, IRIS_TRAINING_URL)
  test_data = downloaddata(IRIS_TEST, IRIS_TEST_URL)
  
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
  #Drop tables if they already exist, this enables a refresh utility
  #    if this is rerun. Useful for demonstrations but bad for most
  #    actual implementations.
  cursor.execute("DROP TABLE IF EXISTS %s" %('training'))
  cursor.execute("DROP TABLE IF EXISTS %s" %('test'))
  mydb.commit
  #Create tables for training and testing
  cursor.execute("""CREATE TABLE IF NOT EXISTS training (
         sepal_length  FLOAT,
         sepal_width  FLOAT,
         petal_length FLOAT,
         petal_width  FLOAT,
         set_ver_vir INT )""")
  cursor.execute("""CREATE TABLE IF NOT EXISTS test (
         sepal_length  FLOAT,
         sepal_width  FLOAT,
         petal_length FLOAT,
         petal_width  FLOAT,
         set_ver_vir INT )""")
  mydb.commit()

  #Push data from csv files into tables
  for row in training_data:
      row[0] = float(row[0])
      row[1] = float(row[1])
      row[2] = float(row[2])
      row[3] = float(row[3])
      row[4] = int(row[4])
      cursor.execute('INSERT INTO training(sepal_length, \
            sepal_width, petal_length, petal_width, set_ver_vir )' \
            'VALUES("%s", "%s", "%s", "%s", "%s")', 
            row)

  for row in test_data:
      row[0] = float(row[0])
      row[1] = float(row[1])
      row[2] = float(row[2])
      row[3] = float(row[3])
      row[4] = int(row[4])
      cursor.execute('INSERT INTO test(sepal_length, \
            sepal_width, petal_length, petal_width, set_ver_vir )' \
            'VALUES("%s", "%s", "%s", "%s", "%s")', 
            row)
  mydb.commit()

  ##Example of how to fetch from this db.
  #cursor.execute("SELECT * FROM test\
  #                WHERE set_ver_vir = 1")
  #results = cursor.fetchall()
  #print(results)
  #Close db connection
  cursor.close()
  print("Successful handoff of iris CSV datasets to MySQL container.")
main()
