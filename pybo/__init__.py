from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
# db 와 migrate 객체를 전역 변수로 만든다. 함수 내에서 사용할 때는 init_app 메서드를 사용해 app 에 등록한다.
# 만약 create_app 함수 내에서 만든다면 블루프린트 같은 다른 모듈에서 사용할 수 없다.


def create_app():
    app = Flask(__name__)
    # 플라스크 어플리케이션을 생성하는 코드이다.
    # __name__ 이라는 변수에는 모듈명이 담긴다.
    # 그런데 우리는 ~/.bash_profile 파일에, FLASK_APP = pybo 라고 설정해주었다.
    # 이렇게 되면, 본 프로젝트의 루트 디렉토리인 pybo_flask/ 아래에서 pybo 를 탐색하게 된다.
    # pybo 는 디렉토리 이므로, 그 아래의 __ init__.py 가 실행되는 것이다.
    # 이 파일이 실행될때는 pybo 라는 모듈이 실행되는 것이므로, __name__ 변수에는 "pybo" 라는 문자열이 담긴다.

    # # URL 과 Flask code 를 mapping 하는 Flask 의 decorator (기존 함수 변경 없이 추가 기능을 덧붙이는 함수) 이다.
    # @app.route('/')
    # # 이러한 URL 매핑을 @app.route('/')라는 애너테이션이 만들어 준다. 이때 @app.route와 같은 애너테이션으로 URL을 매핑하는 함수를 라우팅 함수라고 한다.
    # # 새로운 URL 매핑이 필요할 때마다 라우팅 함수를 추가하면, 함수가 너무 복잡해진다. 따라서 Flask 의 Blueprint 를 사용한다.
    # # Blueprint : 플라스크에서 URL과 함수의 매핑을 관리하기 위해 사용하는 도구(클래스) 라는 의미로 쓰인다/
    # def hello_pybo():  # '/' URL 이 요청되면 hello_pybo 함수가 실행되는 것이다.
    #     return 'Hello, Pybo!'
    # return app

    app.config.from_object(config)
    app.config.from_envvar('APP_CONFIG_FILE')
    # 환경변수 APP_CONFIG_FILE 에 정의된 파일을 환경 파일로 사용하겠다는 의미이다.
    # 따라서 개발 중인 컴퓨터의 OS 에 맞게, APP_CONFIG_FILE 환경 변수에 '.../pybo_flask/config/development.py' 를 설정해주어야 한다.
    
    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # 작성한 블루프린트를 Flask Application 에 등록해보자.
    from .views import main_views, question_views, answer_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)

    return app
