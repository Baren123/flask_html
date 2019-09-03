#!/usr/bin/env python
#coding: utf-8

from flask import Flask,send_file,request, jsonify,render_template
import time
import os
import json
import random


app = Flask(__name__)
@app.route('/login',methods=["GET"])
def login():
    return send_file("login.html")


@app.route('/sendInfo', methods=["GET","POST"])
def sendInfo():
    print('test')
    my_dict = {'cpu_usage': random.uniform(0, 20),'mem_usage':0.384,'current_ip':0.95}
    # jsonStr = json.dumps(my_dict)
    return render_template('getInfo.html',**my_dict)


@app.route('/getInfo', methods=["GET","POST"])
def getInfo():
    # my_dict = {'cpu_usage':0,'mem_usage':0,'current_ip':0}
    # my_dict = {'zynq_cpu_usage': random.uniform(0, 20),'zynq_mem_usage':0.384,'zynq_current_ip':0.95}
    if request.form['input_uid']=='123456':
        input_uid = request.form['input_uid']
        return render_template('getInfo.html')
        # return render_template('getInfo.html',**my_dict)
        # # return '12'
        # i = 0.1
        # while True:
        #     # time.sleep(4)
        #     print(time.time())
        #     my_dict = {'cpu_usage':i,'mem_usage':0.384,'current_ip':0.95}
        #     i = i + 1
        #     print(my_dict)
            # return render_template('getInfo.html',**my_dict)
    else:
        return ('Input devices is not connect')


@app.route('/mytable', methods=["GET","POST"])
def mytable():
    my_dict_1 = {'zynq_cpu_usage': random.uniform(0, 10),'zynq_mem_usage':random.uniform(0, 100),'zynq_ip':"172.16.0.1",
                'rk_1_cpu_usage': random.uniform(10, 40),'rk_1_gpu_usage':random.uniform(0, 100),'rk_1_mem_usage':random.uniform(0, 100),
                'rk_1_cpu_temp': random.uniform(30, 70), 'rk_1_gpu_temp':random.uniform(30, 70),'rk_1_ip':"172.16.0.2",
                'rk_2_cpu_usage': random.uniform(20, 30),'rk_2_gpu_usage':random.uniform(0, 100),'rk_2_mem_usage':random.uniform(0, 100),
                'rk_2_cpu_temp':random.uniform(30, 70),'rk_2_gpu_temp':random.uniform(30, 70),'rk_2_ip':"172.16.0.3",
                'rk_3_cpu_usage': random.uniform(20, 30),'rk_3_gpu_usage':random.uniform(0, 100),'rk_3_mem_usage':random.uniform(0, 100),
                'rk_3_cpu_temp':random.uniform(30, 70),'rk_3_gpu_temp':random.uniform(30, 70),'rk_3_ip':"172.16.0.4",
                'rk_4_cpu_usage': random.uniform(20, 30),'rk_4_gpu_usage':random.uniform(0, 100),'rk_4_mem_usage':random.uniform(0, 100),
                'rk_4_cpu_temp':random.uniform(30, 70),'rk_4_gpu_temp':random.uniform(30, 70),'rk_4_ip':"172.16.0.5",
                'rk_5_cpu_usage': random.uniform(20, 30),'rk_5_gpu_usage':random.uniform(0, 100),'rk_5_mem_usage':random.uniform(0, 100),
                'rk_5_cpu_temp':random.uniform(30, 70),'rk_5_gpu_temp':random.uniform(30, 70),'rk_5_ip':"172.16.0.6",
                'rk_6_cpu_usage': random.uniform(20, 30),'rk_6_gpu_usage':random.uniform(0, 100),'rk_6_mem_usage':random.uniform(0, 100),
                'rk_6_cpu_temp':random.uniform(30, 70),'rk_6_gpu_temp':random.uniform(30, 70),'rk_6_ip':"172.16.0.7",
                'rk_7_cpu_usage': random.uniform(20, 30),'rk_7_gpu_usage':random.uniform(0, 100),'rk_7_mem_usage':random.uniform(0, 100),
                'rk_7_cpu_temp':random.uniform(30, 70),'rk_7_gpu_temp':random.uniform(30, 70),'rk_7_ip':"172.16.0.8",
                'rk_8_cpu_usage': random.uniform(20, 30),'rk_8_gpu_usage':random.uniform(0, 100),'rk_8_mem_usage':random.uniform(0, 100),
                'rk_8_cpu_temp':random.uniform(30, 70),'rk_8_gpu_temp':random.uniform(30, 70),'rk_8_ip':"172.16.0.9",
                'rk_9_cpu_usage': random.uniform(20, 30),'rk_9_gpu_usage':random.uniform(0, 100),'rk_9_mem_usage':random.uniform(0, 100),
                'rk_9_cpu_temp':random.uniform(30, 70),'rk_9_gpu_temp':random.uniform(30, 70),'rk_9_ip':"172.16.0.10",
                'rk_10_cpu_usage': random.uniform(20, 30),'rk_10_gpu_usage':random.uniform(0, 100),'rk_10_mem_usage':random.uniform(0, 100),
                'rk_10_cpu_temp':random.uniform(30, 70),'rk_10_gpu_temp':random.uniform(30, 70),'rk_10_ip':"172.16.0.11"}
    print('my_dict')
    data = json.dumps(my_dict_1)
    print(data)
    # return '12'
    return data

if __name__ == "__main__":
    print ("run")
    app.run(host="127.0.0.1",port="5000")