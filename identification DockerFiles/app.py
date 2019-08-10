# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 15:43:56 2019

@author: SA
"""
#/usr/bin/env python3
from flask import request, Flask, render_template
#from redis import Redis, RedisError
import tensorflow as tf
import os
from imageprepare import imageprepare
from cqloperation import insertData

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('UploadPage.html')
'''
@app.route("/login",methods=['POST','GET'])
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        return render_template('UploadPage.html')
    else:
        return render_template('failed.html')
'''

@app.route("/upload",methods=['POST','GET'])
def get_image():
    if request.method=='POST':
        upload_file=request.files['image']
        basepath=os.path.dirname(__file__)
        #upload_path=os.path.join(basepath,r'/app/uploadimages',upload_file.filename)
        file_path=os.path.join(basepath,upload_file.filename)
        file_name=upload_file.filename
        print(file_path)
        upload_file.save(file_path)
        context = {}
        result=imageprepare(file_path)
        #x=tf.placeholder(tf.float32,[None,784])
        x=tf.compat.v1.placeholder(tf.float32, [1, 784])
        W=tf.Variable(tf.zeros([784, 10]))
        b=tf.Variable(tf.zeros([10]))
        def weight_variable(shape):
            #initial = tf.truncated_normal(shape, stddev=0.1)
            initial=tf.random.truncated_normal(shape, stddev=0.1)
            return tf.Variable(initial)
        def bias_variable(shape):
            initial = tf.constant(0.1, shape=shape)
            return tf.Variable(initial)
        def conv2d(x,W):
            return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

        def max_pool_2x2(x):
            #return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
            return tf.nn.max_pool2d(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

        W_conv1 = weight_variable([5, 5, 1, 32])
        b_conv1 = bias_variable([32])

        x_image = tf.reshape(x, [-1,28,28,1])
        h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
        h_pool1 = max_pool_2x2(h_conv1)

        W_conv2 = weight_variable([5, 5, 32, 64])
        b_conv2 = bias_variable([64])

        h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
        h_pool2 = max_pool_2x2(h_conv2)

        W_fc1 = weight_variable([7 * 7 * 64, 1024])
        b_fc1 = bias_variable([1024])

        h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])
        h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

        #keep_prob = tf.compat.v1.placeholder(tf.float32)
        rate =1-tf.compat.v1.placeholder(tf.float32)
        h_fc1_drop = tf.nn.dropout(h_fc1, rate)

        W_fc2 = weight_variable([1024, 10])
        b_fc2 = bias_variable([10])

        y_conv=tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)

        init_op = tf.compat.v1.global_variables_initializer()

        saver = tf.compat.v1.train.Saver()
        with tf.compat.v1.Session() as sess:
            sess.run(init_op)
            saver.restore(sess, "./model_2/model_2.ckpt")#这里使用了之前保存的模型参数
            prediction=tf.argmax(y_conv,1)
            predint=prediction.eval(feed_dict={x: [result],rate: 1.0}, session=sess)
            print('recognize result:')
            print(predint[0])       
            context['digit']=predint[0]
        insertData(file_name,context['digit'])
        return render_template('success.html',**context)
    else: 
        return render_template('failed.hmtl')

if __name__ == "__main__":
    app.debug=True
    #app.run()
    app.run(host='0.0.0.0', port=5000)
