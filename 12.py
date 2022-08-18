from flask import Flask, request, jsonify
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import sys
import psycopg2

def area(response):

    content = request.get_json()
    print(content)
    content1= content['userRequest']['utterance']
    print(content1)

    conn_string = "host = 'ec2-107-23-76-12.compute-1.amazonaws.com' dbname = 'd7njsi7ltrih2l' user = 'avoldyshprcjzu' password = '2a92b7788746e69afe72137c1021fdb9966e4ceb2c41ad68c71e7aedd7e65db3'"
    conn = psycopg2.connect(conn_string)
    cur = conn.cursor()
    cur.execute("SELECT * FROM area WHERE location LIKE '%{0}%';".format(response))
    rows = cur.fetchall()
    print(type(rows))
    return rows

if __name__=='__main__':
    result = input("지역입력")
    print(area(result))