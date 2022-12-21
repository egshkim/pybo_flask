from flask import Blueprint, render_template
from pybo.models import Question
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
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html', question_list=question_list)
    # 렌더링이란, 웹사이트 코드가 브라우저에 출력되는 과정 또는 그러한 행위를 말한다.
    # 템플릿이란, 파이썬 문법을 사용할 수 있는 HTML 파일을 말한다.
    # render_template 함수는 템플릿 파일을 화면으로 렌더링 하는 함수이다.
    # 앱으로 지정한 모듈 (pybo 디렉토리) 아래에 templates 라는 디렉토리를 만들면, 저절로 templates 를 템플릿 디렉토리로 인식한다.


@bp.route('/detail/<int:question_id>/')
# question_id 가 삽입된다는 것이 아니다. 삽입된 int 를, question_id 라는 변수에 저장하겠다는 것이다.
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    # get_or_404() 함수 말고 그냥 get() 함수를 사용하면, 정의되지 않은 페이지를 입력했을 때 그냥 빈 화면이 나타난다.
    return render_template('question/question_detail.html', question=question)
