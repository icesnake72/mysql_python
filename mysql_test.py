# import mysql.connector
from flask import Flask, render_template, redirect as rd, url_for, request, session
from flask_mysqldb import MySQL, MySQLdb
from my_constant import *
import json


app = Flask(__name__)

@app.route(HOME)
def index():
  if EMAIL_ID in session and USER_ID in session:
    todos = get_todos(session.get(USER_ID))
    return render_template(INDEX_HTML, todos=todos, signin=True, nick_name=session.get(NICK_NAME))
  
  return render_template(INDEX_HTML, signin=False)
  

@app.route('/get_user_todos', methods=['POST'])
def get_user_todos():
  if request.method=='POST':
    email_id = request.form['InputEmail']     # index.html의 form에서 넘겨받은 email id ---> name : InputEmail
    user_id = request.form['InputID']  # index.html의 form에서 넘겨받은 password ---> name : InputPassword

    # login 가정하고
    todos = get_todos(user_id)
    print(todos)
    return todosToJson(todos)
  
  print(session)
  print("not in session")
  return "not in session"


def todosToJson(todos) -> str:
  liTodos = []
  result = dict() 
  
  for item in todos:
    todo = dict()
    todo["id"] = item[0]
    todo["todo"] = item[1]
    todo["done"] = item[2]
    todo["created_time"] = item[3].strftime("%Y-%m-%d %H:%M:%S")
    todo["user_id"] = item[4]
    liTodos.append( todo )

  result["todos"] = liTodos
  print(result)
  ret_json = json.dumps(result, ensure_ascii=False, indent="\t")
  print(ret_json)
  return ret_json


def get_todos(user_id):
  sql = 'select * from todos where user_id=%s order by done, created_time'
  val = (user_id,)  # 튜플에 값 한개만 입력할때는 ()의 사용이 튜플임을 알리기 위해 ,를 찍는다
  cursor = mysql.connection.cursor()  # todos 데이터베이스에 연결한다
  cursor.execute(sql, val)     # 위에 sql, val 변수를 이용하여 mysql에 쿼리문을 전달하고 실행한다.
  result = cursor.fetchall()  # mysql에서 실행한 결과의 모든 행을 받아온다
  cursor.close()
  return result


@app.route('/login_app', methods=['post'])
def login_app():
  if request.method=='POST':
    email_id = request.form['InputEmail']     # index.html의 form에서 넘겨받은 email id ---> name : InputEmail
    password = request.form['InputPassword']  # index.html의 form에서 넘겨받은 password ---> name : InputPassword

    # mysql 데이터베이스를 핸들링하기 위한 핸들러를 생성한다!!!
    cursor = mysql.connection.cursor()  # todos 데이터베이스에 연결한다
    sql = 'select * from users where email=%s and password=%s'  # 쿼리문을 작성한다 : index.html의 form으로부터 넘겨받은 email과 password를 이용하여
    val = (email_id, password)  # sql 변수의 %s 부분에 각각 포맷팅될 값을 튜플의 형식으로 지정한다.
    cursor.execute(sql, val)     # 위에 sql, val 변수를 이용하여 mysql에 쿼리문을 전달하고 실행한다.
    result = cursor.fetchall()  # mysql에서 실행한 결과의 모든 행을 받아온다
    cursor.close()     # 데이터베이스 핸들러를 닫아준다!!! (중요 : 핸들러는 사용후에 반드시 닫아주어야 한다!!!) 

    login_info = dict()

    # len() 을 이용하여 결과값이 1보다 크면 중복 사용자가 있는것이므로 오류를 반환한다!!!
    if len(result) > 1 :
      login_info['email_id'] = 'null'
      login_info['nick_name'] = 'null'
      login_info['id'] = 'null'
    else:      
      login_info['email_id'] = email_id
      login_info['nick_name'] = result[0][3]
      login_info['id'] = result[0][0]

      # session[EMAIL_ID] = email_id      # 이 email은 쿼리로 얻어온 값과 같다
      # session[NICK_NAME] = result[0][3]  # 쿼리해서 얻어온 닉네임
      # session[USER_ID] = result[0][0]       # 쿼리해서 얻어온 id
      # return rd('/get_user_todos')

    ret_json = json.dumps(login_info, ensure_ascii=False, indent='\t')
    print(ret_json)
    return ret_json

  return '<p>잘못된 접근 방식입니다</p>'





@app.route('/login', methods=['POST'])
def login():
  if request.method=='POST':
    email_id = request.form['InputEmail']     # index.html의 form에서 넘겨받은 email id ---> name : InputEmail
    password = request.form['InputPassword']  # index.html의 form에서 넘겨받은 password ---> name : InputPassword

    # mysql 데이터베이스를 핸들링하기 위한 핸들러를 생성한다!!!
    cursor = mysql.connection.cursor()  # todos 데이터베이스에 연결한다
    sql = 'select * from users where email=%s and password=%s'  # 쿼리문을 작성한다 : index.html의 form으로부터 넘겨받은 email과 password를 이용하여
    val = (email_id, password)  # sql 변수의 %s 부분에 각각 포맷팅될 값을 튜플의 형식으로 지정한다.
    cursor.execute(sql, val)     # 위에 sql, val 변수를 이용하여 mysql에 쿼리문을 전달하고 실행한다.
    result = cursor.fetchall()  # mysql에서 실행한 결과의 모든 행을 받아온다
    cursor.close()     # 데이터베이스 핸들러를 닫아준다!!! (중요 : 핸들러는 사용후에 반드시 닫아주어야 한다!!!) 

    # len() 을 이용하여 결과값이 1보다 크면 중복 사용자가 있는것이므로 오류를 반환한다!!!
    if len(result) > 1 :
      return '회원 정보에 중복된 값이 있습니다, 관리자에게 문의하세요'
    
    # print(result)

    # 
    # for col in result[0]:
    # print(result[0][0], result[0][1], result[0][2], result[0][3])

    # 로그인 정보를 session 변수에 저장한다.
    # session : 클라이언트와 서버 간에 상태를 유지하기 위한 메커니즘
    session[EMAIL_ID] = email_id      # 이 email은 쿼리로 얻어온 값과 같다
    session[NICK_NAME] = result[0][3]  # 쿼리해서 얻어온 닉네임
    session[USER_ID] = result[0][0]       # 쿼리해서 얻어온 id
    
    # session 정보를 저장하고 다시 홈으로 돌아간다~~~
    return rd(HOME)

    # print(request.form['InputEmail'], request.form['InputPassword'])
    # return request.form['InputEmail'] + request.form['InputPassword']
  else:
    return '<p>잘못된 접근 방식입니다</p>'
  

@app.route('/signup', methods=['get', 'post'])
def signup():
  if request.method=='GET':
    error = request.args.get('param1')
    return render_signup(error)
    
  elif request.method=='POST':
    return insert_user(request.form['InputEmail'],
                request.form['InputPassword'],
                request.form['InputPasswordConfirm'],
                request.form['InputNickName'])


def render_signup(error:str):
  if error=="":
    return render_template(SIGNUP_HTML)
  else:
    return render_template(SIGNUP_HTML, error_msg=error)


def insert_user(email, passwd, passwd_conf, nick_name):
  # input으로 입력된 값들중에 하나라도 빠진게 있으면...
  if email=="" or passwd=="" or passwd_conf=="" or nick_name=="":
    error = '모든 필수 항목들을 입력해주세요'
    return rd(url_for(SIGNUP, param1=error))  # signup form page로 redirect 시킴 (method를 post로 지정하지 않았기 때문에 GET 방식임)
  
  # 입력한 비밀번호와 비밀번호 확인 필드가 서로 다르면...
  if passwd!=passwd_conf:
    error = '비밀번호 입력을 확인해주세요'
    return rd(url_for(SIGNUP, param1=error))  # signup form page로 redirect 시킴 (method를 post로 지정하지 않았기 때문에 GET 방식임)
  
  # 정상적인 입력이 확인되었으면 todos데이터베이스의 users 테이블에 위 항목들을 입력한다
  # 먼저 insert sql문을 작성한다
  sql = '''insert into users(email, password, nick_name)
  values(%s,%s,%s)''' 
  values = (email, passwd, nick_name) # 위 %s에 포맷팅될 각각의 값을 순서대로 튜플형태로 만든다
  cur = mysql.connection.cursor() # 데이터베이스 핸들러 객체를 가져온다
  try:
    cur.execute(sql, values)  # sql문을 변수들과 함께 실행한다
    mysql.connection.commit() # insert문을 실행한뒤에는 반드시 commit을 해주어야 한다
    cur.close()               # 데이터베이스 핸들러 사용을 완료했으면 반드시 close()해준다
  except MySQLdb.IntegrityError as err:
    error = f'회원가입 실패 : 이미 가입된 회원(email : {email})이 있습니다)'
    return rd(url_for(SIGNUP, param1=error))
  except:
    error = '회원가입 실패 : 알 수 없는 오류 (관리자에게 문의해주세요)'
    return rd(url_for(SIGNUP, param1=error))
    
  return '회원가입해 주셔서 감사합니다 : <a href="/">로그인 페이지로 돌아가 로그인을 해주세요.</a>'


@app.route(LOGOUT)
def logout():
  if EMAIL_ID in session and USER_ID in session:
    session.pop(EMAIL_ID)
    session.pop(NICK_NAME)
    session.pop(USER_ID)
  
  return rd(HOME)


@app.route(INPUT_TODO, methods=[POST])
def input_todo():
  if session.get(USER_ID)=="":
    error = '<p>로그인 정보가 없습니다, <a href="/">홈으로...</a></p>'

  sql = 'insert into todos (todo, user_id) values(%s, %s)'
  val = (request.form.get('InputTodo'), session.get(USER_ID))
  cur = mysql.connection.cursor()
  cur.execute(sql, val)
  mysql.connection.commit()
  cur.close()

  return rd(HOME)

@app.route('/update_done', methods=[POST])
def updateDone():    
  if request.method!=POST:
     return "잘못된 경로로 접근하였습니다"
  
  done = request.json['done']
  #print(str(done))

  user_id = request.json['user_id']
  #print(str(user_id))

  todo_id = request.json['todo_id']
  #print(str(todo_id))  

  # sql = 'update 테이블명 set 필드명=값 where 조건'
  sql = 'update todos set done=%s where id=%s and user_id=%s'
  val = (done, todo_id, user_id)

  cursor = mysql.connection.cursor()
  cursor.execute(sql, val)
  mysql.connection.commit()
  cursor.close()

  return rd(HOME)


@app.route('/delete_todo', methods=[POST])
def deleteTodo():  
  todo_id = request.json['todo_id']
  print(todo_id)

  # sql = 'delete from 테이블명 where 조건'
  sql = 'delete from todos where id=%s'
  val = (todo_id,)

  cursor = mysql.connection.cursor()
  cursor.execute(sql, val)

  mysql.connection.commit()
  cursor.close()

  return rd(HOME)


if __name__ == '__main__':  
  app.secret_key = SECRET_KEY
  app.config['TEMPLATES_AUTO_RELOAD'] = True
  app.config['MYSQL_HOST'] = DB_HOST
  app.config['MYSQL_USER'] = DB_USER
  app.config['MYSQL_PASSWORD'] = DB_PASSWD
  app.config['MYSQL_DB'] = DB_NAME
  mysql = MySQL(app)
  # app.run(port=SERV_PORT, debug=True)
  app.run(host='0.0.0.0', port=SERV_PORT, debug=True)









