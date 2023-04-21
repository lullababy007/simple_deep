# from random import*

# lst = range(1,21) #1 부터 21 직전까지 숫자를 생성
# lst = list(lst)
# print(lst)
# shuffle(lst)

# print(lst)
# winners = sample(lst, 4)
# winners.sort()
# print(winners)

# print("1등 당첨자는 {}번".format(winners[0]))
# print("2,3,4등 당첨자는 {}".format(winners[1:]))


# weather = input("오늘의 날씨는? ")
# #input은 항상 문자열로 값을 받음
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")

# elif weather == "미세먼지":
#     print("마스크를 챙기세요")

# temp = int(input("기온은 어때요?"))
# if temp >= 30:
#     print("너무 더워요. 나가지 마세요")


# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다".format(customer))

# students  = ["담온", "형묵이"]
# students = [len(i) for i in students]
# print(students)

# from random import *

# cnt = 0

# for i in range(1,51):
#     time = randrange(5,50)

#     if time >=5 and time <15:
#         cnt +=1


# print("총 탑승객은 {0}명 입니다". format(cnt))

# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# open_account()

# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0} 입니다.".format(balance+money))
#     return balance+money

# print(deposit(50,30))

# def profile(name, age, main_lang):
#     print("이름: {0}\t나이 : {1}\t주 사용언어 : {2}" \
#         .format(name, age, main_lang))

# profile("유재석", 20, "파이썬")

# def profile(name, age, *main_lang):
#     print("{0},{1}".format(name, age),end =" ")
#     for lang in main_lang:
#         print(lang, end= " ")
#     print()
    


# profile("유재석", 36, "파이썬", "자바")

# def std_weight(height, gen):
#     if gen =="여자":
#         std = height *height *21

#     else:
#         std = height*height *22

#     return std


# g= input("성별을 입력하세요: ")
# h= float(input("키를 입력하세요: "))
# stdard = round(std_weight(h, g),2)

# print("키 {0} {1}의 표준 체중은 {2}입니다.".format(h, g, stdard)) 

# print("python", "java", end = "? " )
# print("무엇이 더?")

# for i in range(1,30):
#     print("대기번호: " + str(i).zfill(3))

#빈자리는 빈공간으로 두고, 오른쪽정렬을 하되, 총 10자리 공간을 확보
#왼쪽정렬하고, 빈공간엔 _로 채움
#3자리마다 콤마를 찍어주기

#3자리마다 콤마찍고, 부호 붙이고, 30자리 확보하고, 빈공간은 ^로 채워주기
# score_file = open("score.txt", "w", encoding = "utf8")
# print("영어: 100", file = score_file)
# score_file.close

# for i in range(1,51):
#     file_report = open( "{}주차 주간보고.txt".format(i), "w", encoding = "utf8" )
#     file_report.write("부서: ")
#     file_report.write("\n이름: ")
#     file_report.write("\n업무 요약: ")
#     file_report.close

class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def move(self, location):
        print("{0} 방향으로 지상 이동합니다".format(location))

class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage 

    def attack(self, direction):
        print("{0}가 {1} 방향으로 공격합니다".format(self.name, direction))

    def move(self, location):
        print("{0}가 {1} 방향으로 날아갑니다".format(self.name, location))

wraith = AttackUnit("레이스", 100, 20)
wraith.attack("5시")  
wraith.move("4시")     
goliath = Unit("골리앗",150)
goliath.move("3시")