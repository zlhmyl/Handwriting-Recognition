# MIT Remote Research Project 
Handwriting Digit Recognition System
===

Description
---
This is a system that can recognize handwriting digits in images. The system is deployed on Docker. Users are allowed to visit the system through:http://localhost:5000/. Users can upload their image and get the recognition result immediately.<br>
[Visit Now](http://localhost:5000/)

Demo
---
<img src="https://github.com/zlhmyl/Handwriting-Recognition/blob/master/系统演示demo.gif" alt="show" />
![image](https://github.com/zlhmyl/Handwriting-Recognition/blob/master/系统演示demo.gif)

Project Structure
---
* Handwriting-Recognition
  * Remote Search Project Report_Lihan Zhang.pdf //report for the project
  * 系统演示demo.gif //a demo for the system
  * 系统演示_zlh.mp4 //a demo for the system
  * identification Dockerfiles 
    * __pychche__
    * model_2  //trained model is stored here
    * templates  //webpages are stored here
    * Dockerfile //used to create an image
    * app.py //main program
    * cqloperation.py  //program to connet with Cassandra
    * imageprepare.py  //program to prehandle the images before recognition
    * requirements.txt //part of libs and dependencies need for the image
    * testmodel.py //program to train the model
  


How to run
---
visit the website:http://localhost:5000/ in your browser. Upload your image and you will get the predict number immediately.


Requirements
---
Their are some packages and tools needed for the project
### Docker
The Docker is an open source application container engine. It allows developers to package their applications and dependencies into a portable image and then publish it to any popular Linux or Windows machine, as well as virtualization.<br>
You can visit the website:https://www.docker.com/ to get more information and installation.

### Flask
Flask is a lightweight, customizable framework written in Python that is flexible, lightweight, secure, and easy to use. Flask has a strong customization, users can add corresponding functions according to their own needs, and realize the richness and expansion of functions while keeping the core functions simple. <br>
You can visit the website:https://dormousehole.readthedocs.io/en/latest/ to get more information and installation.


### Cassandra
Cassandra is an open source distributed NOSQL database system similar to Google's Big Table. In fact, it is a distributed network service composed of a bunch of database nodes. It has the characteristics of flexible mode, scalability, and multiple data centers. A good choice for the storage of big data.<br>
You can visit the website:http://cassandra.apache.org/ to get more information and installation.

### Tensorflow
Tensorflow is a symbolic mathematics system based on dataflow programming. It is widely used in the programming implementation of various machine learning algorithms.Tensorflow can run on a variety of hardware through support for threads, queues, and asynchronous calculations, and assigns operations to appropriate devices based on computational needs.<br>
You can visit the website:https://tensorflow.google.cn/ to get more information and installation.








