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

@app.route('/private/special', methods=['POST'])
def private1():

    content = request.get_json()
    print(content)

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

if __name__ == "__main__":
    app.run(host='0.0.0.0') # Flask 기본포트 5000번
