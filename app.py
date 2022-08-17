from flask import Flask, request, jsonify
import sys
app = Flask(__name__)

@app.route("/")
def hello():
    return "51"

@app.route('/keyboard')
def Keyboard():
    dataSend = {
    "Subject":"OSSP",
    "user":"corona_chatbot"
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
    
    dataSend = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard": 
                    {
                        "title": "간단한 텍스트 요소입니다.",
                        "buttons": [
                    {
                        "action": "message",
                        "label": "일반",
                        "messageText": "일반분양입니다."
                    },
                    {
                        "action": "message",
                        "label": "특별",
                        "messageText": "특별분양입니다."
                        }
                        ]
                    }
                }
                    
                ]
            }
        }
    

    return jsonify(dataSend)

@app.route('/private/special1', methods=['POST'])
def private1():

    content = request.get_json()
    print(content)

    dataSend = {
    "version": "2.0",
    "template": {
        "outputs": [
        {
            "basicCard": {
            "title": "신혼부부 특별공급",
            "thumbnail": {
                "imageUrl": "https://raw.githubusercontent.com/NeewLife/heroku-test1235/main/image/%EB%AF%BC%EA%B0%84%EC%8B%A0%ED%98%BC%EB%B6%80%EB%B6%80.png"
            },
            "profile": {
                "imageUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4BJ9LU4Ikr_EvZLmijfcjzQKMRCJ2bO3A8SVKNuQ78zu2KOqM",
                "nickname": "보물상자"
            },
            "buttons": [
                {
                "action": "message",
                "label": "열어보기",
                "messageText": "짜잔! 우리가 찾던 보물입니다"
                },
                {
                "action":  "webLink",
                "label": "구경하기",
                "webLinkUrl": "https://e.kakao.com/t/hello-ryan"
                }
            ]
            }
        }
        ]
    }
    }
    return jsonify(dataSend)

@app.route('/private1/', methods=['POST'])
def private1():

    content = request.get_json()
    print(content)

    dataSend = {
    "version": "2.0",
    "template": {
        "outputs": [
        {
            "basicCard": {
            "title": "보물상자",
            "description": "보물상자 안에는 뭐가 있을까",
            "thumbnail": {
                "imageUrl": "https://t1.kakaocdn.net/openbuilder/sample/lj3JUcmrzC53YIjNDkqbWK.jpg"
            },
            "profile": {
                "imageUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4BJ9LU4Ikr_EvZLmijfcjzQKMRCJ2bO3A8SVKNuQ78zu2KOqM",
                "nickname": "보물상자"
            },
            "social": {
                "like": 1238,
                "comment": 8,
                "share": 780
            },
            "buttons": [
                {
                "action": "message",
                "label": "열어보기",
                "messageText": "짜잔! 우리가 찾던 보물입니다"
                },
                {
                "action":  "webLink",
                "label": "구경하기",
                "webLinkUrl": "https://e.kakao.com/t/hello-ryan"
                }
            ]
            }
        }
        ]
    }
    }
    return jsonify(dataSend)

if __name__ == "__main__":
    app.run(host='0.0.0.0') # Flask 기본포트 5000번
