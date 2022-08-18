from flask import Flask, request, jsonify
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import sys
import psycopg2
import database


app = Flask(__name__)


@app.route("/")
def hello():
    #db_create()
    return "555"

@app.route("/commit", methods=['POST'])
def commit():
    content = request.get_json()
    print(content)
    response = content['userRequest']['utterance']
    print(response)
    print(type(response))
    print(database.area(response))
    

@app.route("/test", methods=['POST'])
def test():
    content = request.get_json()
    print(content)
    content1= content['userRequest']['utterance']
    print(content1)

    dataSend = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "<사용자 발화>입니다."
                    }
                }
            ],
            "userRequest": {
                "utterance": "<사용자 발화>"
            }
        }
    }
    return jsonify(dataSend)


@app.route('/message', methods=['POST'])
def Message():

    content = request.get_json()
    print(content)

    dataSend = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "간단한 텍스트 요소입니다."
                    }
                }
            ]
        }
    }
    return jsonify(dataSend)

@app.route('/private', methods=['POST'])
def private():

    content = request.get_json()
    print(content)
    content1= content['userRequest']['block']
    print(content1)
    
    dataSend = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard": 
                    {
                        "title": "알고 싶으신 민간분양 유형을 눌러주세요.",
                        "buttons": [
                    {
                        "action": "message",
                        "label": "일반공급",
                        "messageText": "일반분양입니다."
                    },
                    {
                        "action": "block",
                        "label": "특별공급",
                        "blockId": "62f5eb9070055f434dcd0a04"
                    },
                    {
                        "action": "block",
                        "label": "우선공급",
                        "blockId": "62f5ebc370055f434dcd0a0b"
                    }
                        ]
                    }
                }
                    
                ]
            }
        }
    

    return jsonify(dataSend)

@app.route('/private/special', methods=['POST'])
def private2():

    content = request.get_json()
    print(content)
    content1= content['userRequest']['block']
    print(content1)

    dataSend = {
    "version": "2.0",
    "template": {
        "outputs": [
        {
            "carousel": {
            "type": "basicCard",
            "items": [
                {
                    "title": "신혼부부 특별공급",
                    "thumbnail": {
                        "imageUrl": "https://raw.githubusercontent.com/NeewLife/heroku-test1235/main/image/%EB%AF%BC%EA%B0%84%EC%8B%A0%ED%98%BC%EB%B6%80%EB%B6%80.png",
                        "fixedRatio": True,
                        "width": 378,
                        "height": 378
                    },
                    "buttons": [
                        {
                        "action": "webLink",
                        "webLinkUrl": "https://www.easylaw.go.kr/CSP/CnpClsMain.laf?popMenu=ov&csmSeq=873&ccfNo=2&cciNo=4&cnpClsNo=1&search_put=",
                        "label": "정보",
                        }
                    ]
                },
                {
                    "title": "생애최초 특별공급",
                    "thumbnail": {
                        "imageUrl": "https://raw.githubusercontent.com/NeewLife/heroku-test1235/main/image/%EB%AF%BC%EA%B0%84%EC%83%9D%EC%95%A0%EC%B5%9C%EC%B4%88.png",
                        "fixedRatio": True,
                        "width": 378,
                        "height": 378
                    },
                    "buttons": [
                        {
                        "action": "webLink",
                        "webLinkUrl": "https://www.easylaw.go.kr/CSP/CnpClsMain.laf?popMenu=ov&csmSeq=873&ccfNo=2&cciNo=4&cnpClsNo=2&search_put=",
                        "label": "정보",
                        }
                    ]
                },
                {
                    "title": "다자녀가구 특별공급",
                    "thumbnail": {
                        "imageUrl": "https://raw.githubusercontent.com/NeewLife/heroku-test1235/main/image/%EB%AF%BC%EA%B0%84%EB%8B%A4%EC%9E%90%EB%85%80.png",
                        "fixedRatio": True,
                        "width": 378,
                        "height": 378
                    },
                    "buttons": [
                        {
                        "action": "webLink",
                        "webLinkUrl": "https://www.easylaw.go.kr/CSP/CnpClsMain.laf?popMenu=ov&csmSeq=873&ccfNo=2&cciNo=4&cnpClsNo=1&search_put=",
                        "label": "정보",
                        }
                    ]
                },
                {
                    "title": "노부모부양 특별공급",
                    "thumbnail": {
                        "imageUrl": "https://raw.githubusercontent.com/NeewLife/heroku-test1235/main/image/%EB%AF%BC%EA%B0%84%EB%85%B8%EB%B6%80%EB%AA%A8.png",
                        "fixedRatio": True,
                        "width": 378,
                        "height": 378
                    },
                    "buttons": [
                        {
                        "action": "webLink",
                        "webLinkUrl": "https://www.easylaw.go.kr/CSP/CnpClsMain.laf?popMenu=ov&csmSeq=873&ccfNo=2&cciNo=4&cnpClsNo=1&search_put=",
                        "label": "정보",
                        }
                    ]
                },
                {
                    "title": "기관추천 특별공급",
                    "thumbnail": {
                        "imageUrl": "https://raw.githubusercontent.com/NeewLife/heroku-test1235/main/image/%EB%AF%BC%EA%B0%84%EA%B8%B0%EA%B4%80%EC%B6%94%EC%B2%9C.png",
                        "fixedRatio": True,
                        "width": 378,
                        "height": 378
                    },
                    "buttons": [
                        {
                        "action": "webLink",
                        "webLinkUrl": "https://www.easylaw.go.kr/CSP/CnpClsMain.laf?popMenu=ov&csmSeq=873&ccfNo=2&cciNo=4&cnpClsNo=3&search_put=",
                        "label": "정보",
                        }
                    ]
                }
            ]
        }
        }
        ]
    }
    }
    return jsonify(dataSend)

@app.route('/private/priority', methods=['POST'])
def private3():

    content = request.get_json()
    print(content)
    content1= content['userRequest']['block']
    print(content1)

    dataSend = {
    "version": "2.0",
    "template": {
        "outputs": [
        {
            "carousel": {
            "type": "basicCard",
            "items": [
                {
                    "title": "대규모택지 개발지구 우선공급",
                    "thumbnail": {
                        "imageUrl": "https://raw.githubusercontent.com/NeewLife/heroku-test1235/main/image/%EB%AF%BC%EA%B0%84%EB%8C%80%EA%B7%9C%EB%AA%A8%ED%83%9D%EC%A7%80.png",
                        "fixedRatio": True,
                        "width": 378,
                        "height": 378
                    },
                    "buttons": [
                        {
                        "action": "webLink",
                        "webLinkUrl": "https://www.easylaw.go.kr/CSP/CnpClsMain.laf?popMenu=ov&csmSeq=873&ccfNo=2&cciNo=3&cnpClsNo=1&search_put=",
                        "label": "정보",
                        }
                    ]
                },
                {
                    "title": "임대사업자 우선공급",
                    "thumbnail": {
                        "imageUrl": "https://raw.githubusercontent.com/NeewLife/heroku-test1235/main/image/%EB%AF%BC%EA%B0%84%EC%9E%84%EB%8C%80%EC%82%AC%EC%97%85%EC%9E%90.png",
                        "fixedRatio": True,
                        "width": 378,
                        "height": 378
                    },
                    "buttons": [
                        {
                        "action": "webLink",
                        "webLinkUrl": "https://www.easylaw.go.kr/CSP/CnpClsMain.laf?popMenu=ov&csmSeq=873&ccfNo=2&cciNo=3&cnpClsNo=1&search_put=",
                        "label": "정보",
                        }
                    ]
                },
                {
                    "title": "주상복합 건축물의 건설부지 소유자 특별공급",
                    "thumbnail": {
                        "imageUrl": "https://raw.githubusercontent.com/NeewLife/heroku-test1235/main/image/%EB%AF%BC%EA%B0%84%EC%A3%BC%EC%83%81%EB%B3%B5%ED%95%A9.png",
                        "fixedRatio": True,
                        "width": 378,
                        "height": 378
                    },
                    "buttons": [
                        {
                        "action": "webLink",
                        "webLinkUrl": "https://www.easylaw.go.kr/CSP/CnpClsMain.laf?popMenu=ov&csmSeq=873&ccfNo=2&cciNo=3&cnpClsNo=1&search_put=",
                        "label": "정보",
                        }
                    ]
                },
            ]
        }
        }
        ]
    }
    }
    return jsonify(dataSend)


if __name__ == "__main__":
    #db_create()
    app.run(host='0.0.0.0') # Flask 기본포트 5000번
