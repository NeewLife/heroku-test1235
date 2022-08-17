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
                    ,
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
            ]
        }
    }

    return jsonify(dataSend)

if __name__ == "__main__":
    app.run(host='0.0.0.0') # Flask 기본포트 5000번
