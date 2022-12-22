from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class QuestionForm(FlaskForm):
    # 플라스크의 폼은 FlaskForm 클래스를 상속해서 만들어야 한다.
    subject = StringField('제목', validators=[DataRequired()])
    # StringField 를 사용하면 글자 수 제한이 생긴다.
    # 첫 번째 인수 '제목' 은 폼 라벨 이다.
    # validators = [DataRequired(), Email()] 과 같이 사용하면, 이 항목은 필수이고 이메일이어야 한다는 것이다. 해당 사항을 검증해준다,
    content = TextAreaField('내용', validators=[DataRequired()])
