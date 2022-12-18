FLASK Project Architecture :
<pre>
├── pybo/
│      ├─ __init__.py # 플라스크 어플리케이션 파일
│      ├─ models.py # 데이터베이스에 사용할 모델 클래스 정의
│      ├─ forms.py # 폼 클래스 정의
│      ├─ views/ # 웹사이트에서 보여줄 화면 구성을 정의
│      │   └─ main_views.py
│      ├─ static/ # style sheet, java scripts, image files 를 포함
│      │   └─ style.css
│      └─ templates/ # HTML template filees 를 포함
│            └─ index.html
└── config.py # 프로젝트의 환경 설정을 정의
</pre>
