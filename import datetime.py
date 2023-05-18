import datetime
import re

def create_membership():
    # 아래 코드는 python에 내장되어 있는 datetime 모듈을 활용하여 오늘 날짜를 입력하는 코드입니다. 
    # stnr_date 코드는 제가 작성했으니, 건드리지 않으셔도 되옵니다 :)
    now = datetime.datetime.now()
    stnr_date = now.strftime('%Y%m%d')
    
    users = []
    user = {}
    while True:
    username = input("사용자 이름: ")
    if not re.match("^[가-힣]{2,4}$", username):
    print("조건에 안맞음")
continue

password = input("비밀번호: ")
    if not re.match("^(?=.*[A-Z])(?=.*[!@#$])[A-Za-z\d!@#$%^&*()_+]{8,}$", password):
        print("조건에 안맞음")
        continue

    email = input("이메일 주소: ")
    if not re.match("^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]{2,}$", email):
        print("조건에 안맞음")
        continue

    user["username"] = username
    user["password"] = password
    user["email"] = email
    user["stnr"] = stnr_date
    
    break
    # user 딕셔너리에 username, password, email을 아래 주어진 제한 조건에 알맞게 입력받는 코드를 작성하세요.
    # user 딕셔너리 값에는 username, password, email, stnr_date 총 4가지 값이 저장되어야 합니다.
    users.append(user)

    return users

def load_to_txt(user_list):
    f = open('memberdb.txt', 'w', encoding='UTF-8')
    # user_list에 있는 user 3명의 딕셔너리 값을 txt에 작성하세요.
    # 올바르게 생성된 텍스트 파일i의 예시는 상단에 이미지로 첨부되어 있습니다.https://github.com/yg111703/HW5
    f.close()
    
def run():
    # 위에서 정의한 create_membership 함수가 실행되어 반환된 결과값을 user_list 객체에 저장합니다.
    user_list = create_membership()
    # 위에 생성된 user_list 객체를 load_to_txt 함수의 입력변수로 활용하여 txt 파일을 생성합니다.
    load_to_txt(user_list)
    
run()