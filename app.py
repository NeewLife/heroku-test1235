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
            "carousel": {
            "type": "commerceCard",
            "header": {
                "title": "커머스 카드\n케로셀 헤드 예제",
                "thumbnail": {
                "imageUrl": "https://t1.kakaocdn.net/openbuilder/sample/lj3JUcmrzC53YIjNDkqbWK.jpg"
                }
            },
            "items": [
                {
                "description": "따끈따끈한 보물 상자 팝니다",
                "price": 10000,
                "discount": 1000,
                "currency": "won",
                "thumbnails": [
                    {
                    "imageUrl": "https://t1.kakaocdn.net/openbuilder/sample/lj3JUcmrzC53YIjNDkqbWK.jpg",
                    "link": {
                        "web": "https://store.kakaofriends.com/kr/products/1542"
                    }
                    }
                ],
                "profile": {
                    "imageUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4BJ9LU4Ikr_EvZLmijfcjzQKMRCJ2bO3A8SVKNuQ78zu2KOqM",
                    "nickname": "보물상자 팝니다"
                },
                "buttons": [
                    {
                    "label": "구매하기",
                    "action": "webLink",
                    "webLinkUrl": "https://store.kakaofriends.com/kr/products/1542"
                    },
                    {
                    "label": "전화하기",
                    "action": "phone",
                    "phoneNumber": "354-86-00070"
                    },
                    {
                    "label": "공유하기",
                    "action": "share"
                    }
                ]
                },
                {
                "description": "따끈따끈한 보물 상자 팝니다",
                "price": 10000,
                "discount": 1000,
                "currency": "won",
                "thumbnails": [
                    {
                    "imageUrl": "https://t1.kakaocdn.net/openbuilder/sample/lj3JUcmrzC53YIjNDkqbWK.jpg",
                    "link": {
                        "web": "https://store.kakaofriends.com/kr/products/1542"
                    }
                    }
                ],
                "profile": {
                    "imageUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4BJ9LU4Ikr_EvZLmijfcjzQKMRCJ2bO3A8SVKNuQ78zu2KOqM",
                    "nickname": "보물상자 팝니다"
                },
                "buttons": [
                    {
                    "label": "구매하기",
                    "action": "webLink",
                    "webLinkUrl": "https://store.kakaofriends.com/kr/products/1542"
                    },
                    {
                    "label": "전화하기",
                    "action": "phone",
                    "phoneNumber": "354-86-00070"
                    },
                    {
                    "label": "공유하기",
                    "action": "share"
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