from flask import Blueprint
bp = Blueprint('main', __name__, url_prefix='/')
# 첫 번째 인수로 전달한 'main' 이 Blueprint 의 "별칭"이 된다. 이 별칭은 나중에 자주 사용되는 url_for 함수에서 사용된다.
# __name__ 에는 모듈명인 "main_views" 가 전달된다.
# 세 번째 인수인 url_prefix 는 라우팅 함수의 Annotation URL 앞에 기본으로 붙일 prefix URL 이다.


# pybo/__init__.py 파일의 create_app 안에 있던 hello_pybo 함수를 옮겼다.
@bp.route('/hello')
# Annotation 이 @app.route 에서 @bp.route 로 변경되었다.
def hello_pybo():
    return 'Hello, Pybo!'


@bp.route('/')
def index():
    return 'Pybo index'
