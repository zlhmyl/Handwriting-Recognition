# MIT Remote Research Project 
Handwriting Digit Recognition System
===

Description
---
This is a system that can recognize handwriting digits in images. The system is deployed on Docker. Users are allowed to visit the system through:http://localhost:5000/. Users can upload their image and get the recognition result immediately.


Demo
---
[Visit Now](http://localhost:5000/)

Project Structure
---
*Handwriting-Recognition
  *Remote Search Project Report_Lihan Zhang.pdf //report for the project
  *系统演示demo.gif //a demo for the system
  *系统演示_zlh.mp4 //a demo for the system
  *identification Dockerfiles 
    *_pychche_
    *model_2  //trained model is stored here
    *templates  //webpages are stored here
    *Dockerfile //used to create an image
    *app.py //main program
    *cqloperation.py  //program to connet with Cassandra
    *imageprepare.py  //program to prehandle the images before recognition
    *requirements.txt //part of libs and dependencies need for the image
    *testmodel.py //program to train the model
  


How to run
---
visit the website:http://localhost:5000/ in your browser. Upload your image and you will get the predict number immediately.





