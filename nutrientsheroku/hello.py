# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 10:45:47 2019

@author: aayush
"""

from __future__ import unicode_literals, print_function
from flask import Flask,jsonify,request
import difflib

import pandas as pd
import numpy as np

url = "http://chahalacademyexpenditures.hostingerapp.com/Nutrients.csv"
mycsv = pd.read_csv(url,encoding='cp1252')
text=[]
text1=[]
text.append(mycsv.iloc[:,0].values[:])
text1.append(np.array(text).tolist())
questions=text1[0][0]
print(questions)

text2=[]
text12=[]
text2.append(mycsv.iloc[:,1].values[:])
text12.append(np.array(text).tolist())
answers=text2[0]
print(answers)

text3=[]
text13=[]
text3.append(mycsv.iloc[:,2].values[:])
text13.append(np.array(text).tolist())
category=text3[0]
print(category)

   

text=[]
ans=[]
textorurl=[]



#reader = csv.reader(text, delimiter=',')
#url = 'https://chahalacademyexpenditures.000webhostapp.com/ortho.csv'

#mycsv = pd.read_csv(url)

#mycsv = csv.reader(open('./ortho.csv',encoding='cp1252'))
#mycsv = csv.reader(text, delimiter=',')

app=Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return jsonify({"about" : "hello world i am aayush"})

@app.route("/check", methods=['GET'])
def returnall():
    #return jsonify({"languages" : languages}) 
   # with io.open("dataset.json") as f:
    #    sample_dataset = json.load(f)
        
    #load_resources("snips_nlu_en")
    #nlu_engine = SnipsNLUEngine(config=CONFIG_EN)
    #nlu_engine.fit(sample_dataset)
    
    res = request.args.get('query').lower()
    """
    for row in mycsv:
       text.append(row[0])
       ans.append(row[1])
       textorurl.append(row[2])
      """
    natext=[x.lower() for x in questions]   
    query = res.lower()
    na=[x.lower() for x in questions]
    r=difflib.get_close_matches(query, na, n = 1,cutoff = 0.3)
    indexval=natext.index(r[0])
    response=answers[indexval]
    res2=category[indexval]
    return jsonify({"returenedans" : response,"cate":res2})


@app.route("/lang", methods=['POST'])
def postnew():
    return jsonify({"returenedname" : request.json['abc']})


if __name__=='__main__':
    app.run(debug=True)
