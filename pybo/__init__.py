from flask import Flask
app = Flask(__name__)
# 플라스크 어플리케이션을 생성하는 코드이다.
# __name__ 이라는 변수에는 모듈명이 담긴다.
# 즉, 이 파일이 실행될때는 pybo.py 라는 모듈이 실행되는 것이므로, __name__ 변수에는 "pybo" 라는 문자열이 담긴다.


# URL 과 Flask code 를 mapping 하는 Flask 의 decorator (기존 함수 변경 없이 추가 기능을 덧붙이는 함수) 이다.
@app.route('/')
def hello_pybo():  # '/' URL 이 요청되면 hello_pybo 함수가 실행되는 것이다.
    return 'Hello, Pybo!'
