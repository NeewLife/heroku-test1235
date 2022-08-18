from flask import Flask, request, jsonify
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import sys
import psycopg2

## DB 연결 Local
def db_create():
    # 로컬
    engine = create_engine("postgresql://postgres:1234@localhost:5432/chatbot", echo = False)
    
    # Heroku
    engine = create_engine("postgresql://avoldyshprcjzu:2a92b7788746e69afe72137c1021fdb9966e4ceb2c41ad68c71e7aedd7e65db3@ec2-107-23-76-12.compute-1.amazonaws.com:5432/d7njsi7ltrih2l", echo = False)

    engine.connect()
    engine.execute("""
        CREATE TABLE IF NOT EXISTS iris(
            sepal_length FLOAT NOT NULL,
            sepal_width FLOAT NOT NULL,
            pepal_length FLOAT NOT NULL,
            pepal_width FLOAT NOT NULL,
            species VARCHAR(100) NOT NULL
        );"""
    )
    
    engine.execute("""
        CREATE TABLE IF NOT EXISTS area(
            name VARCHAR(100) NOT NULL,
            division VARCHAR(100) NOT NULL,
            location VARCHAR(100) NOT NULL,
            notice_date DATE NOT NULL,
            start_day DATE NOT NULL,
            end_day DATE NOT NULL,
            release_date DATE NOT NULL,
            rink VARCHAR(100) NOT NULL
        );"""
    )

    engine.execute("""
        CREATE TABLE IF NOT EXISTS score(
            name VARCHAR(100) NOT NULL,
            division VARCHAR(100) NOT NULL,
            score INT NOT NULL,
            input INT NOT NULL
        );"""
    )

    data = pd.read_csv('data/iris.csv')
    print(data)
    data.to_sql(name='iris', con=engine, schema = 'public', if_exists='replace', index=False)

    data = pd.read_csv('data/area.csv')
    print(data)
    data.to_sql(name='area', con=engine, schema = 'public', if_exists='replace', index=False)

    data = pd.read_csv('data/score.csv',encoding = 'CP949')
    print(data)
    data.to_sql(name='score', con=engine, schema = 'public', if_exists='replace', index=False)

def area(response):
    conn_string = "host = 'ec2-107-23-76-12.compute-1.amazonaws.com' dbname = 'd7njsi7ltrih2l' user = 'avoldyshprcjzu' password = '2a92b7788746e69afe72137c1021fdb9966e4ceb2c41ad68c71e7aedd7e65db3'"
    conn = psycopg2.connect(conn_string)
    cur = conn.cursor()
    cur.execute("SELECT * FROM area WHERE location LIKE '%{0}%';".format(response))
    rows = cur.fetchall()
    print(type(rows))
    return rows

app = Flask(__name__)


@app.route("/")
def hello():
    #db_create()
    return "555"

if __name__=='__main__':
    # db_create()
    app.run(host='0.0.0.0')