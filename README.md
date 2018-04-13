# Machine Learning Simplified
#### An example of how various technologies may be integrated to simplify machine learning workflows.

## Utilized Technologies
![alt text]( https://raw.githubusercontent.com/TS-Helba/tensorflowdockerexample/master/mdfiles/images/techsused.png  "Technologies used in this project.")
#### MySQL running in a Docker container will provide the storehouse for our machine learning datasets which will allow for simple SQL commands to be used via PHPMyAdmin in pre-processing of our datasets. Docker will also be used to run an instance of Google TensorFlow's Tensorboard to monitor the progress of machine learning models undergoing training and validation. Machine learning models will be created in TensorFlow and Keras and then packaged into Docker containers to train. This will allow for different environments for each model without requiring configuration changes of the host, as this is done in the containers. The Iris classification dataset provided by Google's TensorFlow will be used as a sample implementation.

## Data flows
![alt text]( https://github.com/TS-Helba/tensorflowdockerexample/raw/master/mdfiles/images/dataflowsexample.png  "Dataflows")
#### This shows how different containers/services in this implementation talk to one another.

### Project's Docker Hub
#### https://hub.docker.com/r/helba/tensorflowdockerexample/

## Versioning Info
###### Ubuntu 16.04.3
###### Docker 18.03.0-ce
###### Python 3.5.2
###### Tensorflow 1.7
###### MySQL 5.7
###### PHPMyAdmin 4.7

### Get Ubuntu
#### https://www.ubuntu.com/download/desktop

### Get Docker for Ubuntu
#### https://docs.docker.com/install/linux/docker-ce/ubuntu/#set-up-the-repository

### Get Packages/API's via pip and apt:
###### sudo apt-get install python3.5
###### sudo apt install python3-pip
###### sudo pip3 install tensorflow
###### sudo pip3 install keras
###### sudo apt-get install -y libmysqlclient-dev
###### sudo pip3 install mysqlclient

## How To Use
#### After performing a git pull of the project and installing the required packages, these steps will get you going. You will be able to access TensorBoard on port 6006 and PHPMyAdmin on port 8080 via localhost using a web browser. You can easily alter your datasets using PHPMyAdmin and observe the progress of your training by viewing TensorBoard.
##### Use docker run on first run and docker start on later runs. Make sure to replace directories where indicated by "ParentDirectory". Alternatively use docker stop in place of docker start to bring down containers.
### Operational Steps
#### Initialize MySQLDB.
###### docker run --name irisdb -v /"ParentDirectory"/tensorflowdockerexample/persistence/irisdbdata/varlib/:/var/lib/mysql/ -e MYSQL_USER=tfmysql -e MYSQL_PASSWORD=s0m3d0ck3rus3r -e MYSQL_DATABASE=irisdb -e MYSQL_ROOT_PASSWORD=supersecret -d -p 3306:3306 helba/tensorflowdockerexample:mysql-server5.7
###### docker start irisdb
#### Initialize TensorBoard
###### docker run --name tfboard -v /"ParentDirectory"/tensorflowdockerexample/persistence/tensorboardlogs/:/app/ -d -p 6006:6006 helba/tensorflowdockerexample:board
###### docker start tfboard
#### Initialize PHPMyAdmin (Login: tfmysql - s0m3d0ck3rus3r)
###### docker run -p 8080:80 --link irisdb:db --name mysqladmin -e MYSQL_USER=tfmysql -e MYSQL_PASSWORD=s0m3d0ck3rus3r -e MYSQL_ROOT_PASSWORD=supersecret -e PMA_PORTS=3306 -e PMA_HOSTS=irisdb -d helba/tensorflowdockerexample:phpmyadmin4.7
###### docker start mysqladmin
#### Upload/ingest CSV data into database.
###### docker run --name irisloader helba/tensorflowdockerexample:dbiris -p 3306:3306
###### docker start irisloader
#### Train your model
###### docker run -it -v /"ParentDirectory"/tensorflowdockerexample/persistence/tensorboardlogs/iris/:/app/logs/ helba/tensorflowdockerexample:train -p 3306:3306
## Additional Notes
#### An altered MNIST implementation borrowed from Keras examples is included under the persistence folder which will run on the host instead of in a container but its log data will populate in our TensorBoard container. It may be invoked by using python3 directly.








