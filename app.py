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

@app.route('/private')
def private():
    dataSend = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "알고 싶으신 민간분양 유형을 눌러주세요."
                    },
                    "buttons": [
                        {
                            "action": "message",
                            "label": "일반",
                            "messageText": "일반공급입니다."
                        },
                        {
                            "action": "message",
                            "label": "특별공급",
                            "messageText": "특별공급입니다."                   
                        }
                    ]
                }
            ]
        }
    }
    return jsonify(dataSend)

if __name__ == "__main__":
    app.run(host='0.0.0.0') # Flask 기본포트 5000번