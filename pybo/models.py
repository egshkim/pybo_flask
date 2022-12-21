from pybo import db


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    # 글자 수가 제한된 텍스트에는 db.String()
    # nullable = False 로 설정하면, 빈 값을 허용하지 않음
    content = db.Column(db.Text(), nullable=False)
    # 글자 수를 제한할 수 없는 텍스트에는 db.Text()
    create_date = db.Column(db.DateTime(), nullable=False)


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey(
        'question.id', ondelete='CASCADE'))
    # Question 모델로 테이블을 생성하면 테이블명은 question 이 된다.
    # ondelete='CASCADE' 옵션으로 인해, 질문이 삭제되면 답변들도 삭제된다. 다만 데이터베이스 도구에서 쿼리로 삭제해야함.
    question = db.relationship('Question', backref=db.backref('answer_set'))
    # question 이라는 변수로, answer 테이블에서 question 테이블을 참조할 수 있게 된다.
    # ex) answer.question 로 답변 테이블에서 질문 테이블을 참조할 수 있게 된다.
    # relationship 메서드의 첫 번째 파라미터는 참조할 모델 명이고, backref 파라미터는 역참조 설정이다.
    # 어떤 질문에 해당하는 객체가 a_question 이라면, a_question.answer_set 코드로 해당 질문의 답변들을 참조할 수 있다.

    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
