# -*- coding: utf-8 -*-
from flask import Flask
import pandas as pd 
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

## DB 연결 Local
def db_create():
    # 로컬
    engine = create_engine("postgresql://postgres:1234@localhost:5432/chatbot", echo = False)
    
    # Heroku
    engine = create_engine("postgresql://xulxpjyjsmiezj:79049b8e66c1f943285e01a2b88b7bf63039616b863bd05e6e5f417d224f5095@ec2-44-206-197-71.compute-1.amazonaws.com:5432/da7bkvmriok0f1", echo = False)

    engine.connect()
    engine.execute("""
        CREATE TABLE iris(
            sepal_length FLOAT NOT NULL,
            sepal_width FLOAT NOT NULL,
            pepal_length FLOAT NOT NULL,
            pepal_width FLOAT NOT NULL,
            species VARCHAR(100) NOT NULL
        );"""
    )
    data = pd.read_csv('data/iris.csv')
    print(data)
    data.to_sql(name='iris', con=engine, schema = 'public', if_exists='replace', index=False)

app = Flask(__name__)

@app.route("/")
def index():
    db_create()
    return "Hello World!"



if __name__ == "__main__":
    db_create()
    app.run()