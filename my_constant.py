'''
앞으로 사용될 모든 문자열 및 숫자 상수들을 이곳에 정의해둔다
'''

from typing import Final


# 데이터베이스 연결과 HTTP 통신 보안에 사용될 키값의 정의
DB_HOST:Final = 'localhost'
DB_USER:Final = 'root'
DB_PASSWD:Final = '1234'
DB_NAME:Final = 'todos'

SERV_PORT:Final = 5001

SECRET_KEY:Final = 'student_application_secret_key_25798237985792379582092042093437'

# HTTP Methods
POST:Final = 'post'
GET:Final = 'get'


# 사용될 route 정의
HOME:Final = '/'
SIGNUP:Final = 'signup'
_SIGNUP:Final = '/signup'
INPUT_TODO:Final = '/input_todo'
LOGOUT:Final = '/logout'


# 템플릿 파일 또는 HTML 파일 정의
INDEX_HTML:Final = 'index.html'
SIGNUP_HTML:Final = 'signup.html'

# DB 및 session에 사용되는 변수
EMAIL_ID:Final = 'email_id'
NICK_NAME:Final = 'nik_name'
USER_ID:Final = 'id_'

