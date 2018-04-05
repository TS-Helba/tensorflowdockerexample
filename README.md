# Machine Learning Simplified
An example of how various technologies may be integrated to simplify machine learning workflows.

![alt text]( https://raw.githubusercontent.com/TS-Helba/tensorflowdockerexample/master/mdfiles/images/techsused.png  "Technologies used in this project.")
## Utilized Technologies
MySQL running in a Docker container will provide the storehouse for our machine learning datasets which will allow for simple SQL commands to be used in pre-processing of our datasets. Docker will also be used to run an instance of Google TensorFlow's Tensorboard to monitor the progress of machine learning models undergoing training and validation. Machine learning models will be created in TensorFlow and Keras and then packaged into Docker containers to train. This will allow for different environments for each model without requiring configuration changes of the host, as this is done in the containers.

## Versioning Info
Ubuntu 16.04.3
Docker 18.03.0-ce
Python 3.5.2
Tensorflow 1.7
MySQL X.Y

### Get Ubuntu
https://www.ubuntu.com/download/desktop

### Get Docker for Ubuntu
https://docs.docker.com/install/linux/docker-ce/ubuntu/#set-up-the-repository

### Get Packages/API's via pip and apt:
| ------------------------------------------ |
| sudo apt-get install python3.5 |
| sudo apt install python3-pip |
| sudo pip3 install tensorflow |
| sudo pip3 install keras |
| sudo apt-get install -y libmysqlclient-dev |
| sudo pip3 install mysqlclient |


## How To (WIP)
Directions on how to use the resources in this project will be added as well as a single bash script that will allow you to "press start" on this demonstration and allow you to observe and interact with this implementation.
