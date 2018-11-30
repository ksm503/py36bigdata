# 연습문제


# 20. 복권발행 문제
# 3자리 수 입력
# 모두 일치 = 상금 100만원
# 2개 일치 = 상금 1만원
# 1개 일치 = 상금 1천원

# 파이썬에서 문자열은 문자의 리스트 집합임
# 따라서, 문자열의 각 문자는 리스트의 요소처럼 취급가능

# ex) lotto = 123, lucky = 345 1개 일치
# lotto[1] = lotto[1], lucky[2], lucky[3]


import random


# # 가정: 같은 숫자는 연속적으로 나오지 않는다
# # ex) 777, 111, 555 등

# # if 문으로 쓰기

#lotto = str(random.randint(100, 999))
# 배열처럼 쓰기 위해 숫자를 문자열로 변경

#lucky = input('3자리 복권번호를 입력하세요')
#input은 원래 문자열로 받으므로 바꿀 필요 없음
#
# # 일치여부 함수 초기화
# match = 0
#
# if (lucky[0] == lotto[0] or lucky[0] == lotto[1] or lucky[0] == lotto[2]):
#     match += 1
#
# if (lucky[1] == lotto[0] or lucky[1] == lotto[1] or lucky[1] == lotto[2]):
#     match += 1
#
# if (lucky[2] == lotto[0] or lucky[2] == lotto[1] or lucky[2] == lotto[2]):
#     match += 1
#
# print(lotto, lucky, match)
# # 너무 노가다성이 짙음
#


# # for 반복 문으로 줄이기
#
#
# lotto = str(random.randint(100, 999))
# # 배열처럼 쓰기 위해 숫자를 문자열로 변경
#
# lucky = input('3자리 복권번호를 입력하세요')
# #input은 원래 문자열로 받으므로 바꿀 필요 없음
#
#
# # 일치여부 함수 초기화
# match = 0
#
# for i in [0,1,2]:
#     for j in [0,1,2]:
#         if (lucky[i] == lotto[j]):
#             match += 1
#
# print(lotto, lucky, match)
#
# msg = '꽝!'
# if match == 3:
#     msg = '1등 당첨! : 100만원'
# elif match == 2:
#     msg = '2등 당첨! : 1만원'
# elif match == 1:
#     msg = '3등 당첨! : 1천원'
#
# print(msg)


# 21. 숫자만 입력받아 구구단 출력
# ASCII 코드 출력: ord()

# 0을 입력했을 때 ASCII 코드는 48
#print(ord('0'))
# 9를 입력할 때 ASCII 코드는 57
#print(ord('9'))

# ASCII 코드 입력시 문자 출력 : chr()
#print(chr(48), chr(57)) # 0, 9

# 이 밖의 ASCII 코드는 숫자가 아닌 것으로 판단



# 22. 숫자맞추기 2


#num1 = int(input('1부터 100사이의 숫자를 입력하세요: '))

# num2 = random.randint(1, 100)
#
# msg = ''

# # while문으로 쓰기
# while (num1 != num2):
#     if (num1 < 1 or num1 > 100):
#         msg = '숫자범위를 다시 설정해주세요'
#     elif (num1 > num2):
#         msg = '추측한 숫자가 큽니다'
#     elif (num1 < num2):
#         msg = '추측한 숫자가 작습니다'
#
#     print(msg)
#     num1 = int(input('1부터 100사이의 숫자를 입력하세요: '))
#
# msg = '숫자를 맞췄습니다! 추측: %d, 정답: %d'
# print(msg % (num1, num2))


# ---------------------------------------


#if - break 문으로 쓰기

# num2 = random.randint(1, 100)
#
# msg = ''

# while True:
#     num1 = int(input('1부터 100사이의 숫자를 입력하세요: '))
#     if (num1 == num2):
#         msg = '숫자를 맞췄습니다!'
#         print(msg)
#         break
#     elif (num1 > num2):
#         msg = '추측한 숫자가 큽니다'
#     elif (num1 < num2):
#         msg = '추측한 숫자가 작습니다'
#
#     print(msg)



# 30. 구구단 테이블

# 노가다

gugudan =  '         Multiplication Table \n'
gugudan += '     1   2   3   4   5   6   7   8   9 \n'
gugudan += '-------------------------------------- \n'
gugudan += '1 |  1   2   3   4   5   6   7   8   9 \n'
gugudan += '2 |  2   4   6   8  10  12  14  16  18 \n'
gugudan += '3 |  3   6   9  12  15  18  21  24  27 \n'
gugudan += '4 |  4   8  12  16  20  24  28  32  36 \n'
gugudan += '5 |  5  10  15  20  25  30  35  40  45 \n'


#print(gugudan)



# 반복문사용

# fmt = '\t\t Multiplication Table \n'
# fmt += '\t 1   2   3   4   5   6   7   8   9 \n'
# fmt += '-------------------------------------- \n'
# f = '%d | %2d  %2d  %2d  %2d  %2d  %2d  %2d  %2d  %2d \n'
#
# print(fmt)
# for i in range(1, 9+1):
#
#     print(f % (i, i *1, i*2, i* 3, i * 4, i * 5, i* 6, i * 7, i* 8, i * 9))



# 반복문사용 - 2개 이용해서 더 간단하게

# fmt = '\t\t Multiplication Table \n'
# fmt += '\t 1   2   3   4   5   6   7   8   9 \n'
# fmt += '--------------------------------------'
#
# print(fmt)
# for i in range(1, 9 + 1):
#     print('%d | %2d' % (i, i), end='')
#     for j in range(2, 9+1):
#         print('  %2d' % (i*j), end='')
#     print()



# 32. 주민번호 유효성 검사
# 1. 주민번호 각 자리를 2,3,4,5,6,7,8,9,2,3,4,5의 가중치로 곱함
# 2. 곱한 결과를 각각 모두 더함
# 3. 더한 값을 11로 나눠 나머지를 구함
# 4. 나머지와 주민번호의 끝자리와 일치여부 검사
# 5. 나머지가 2자리라면 맨 끝자리와 비교

# jumin ='1111111111118' # 6자리 + 7자리
# sum = 0
#
# # 가중치 2,3,4,5,6,7,8,9,2,3,4,5
#
# weight = [2,3,4,5,6,7,8,9,2,3,4,5]
#
#
#
# for i in range(len(weight)):
#     sum += int(jumin[i]) * weight[i]
#
#
# mod = sum % 11
# checker = 11 - mod
#
# # 나머지가 2자리인지 여부 검사
#
# if (checker > 9):
#     if (int(str(checker)[1]) == int(jumin[12])):
#         print('주민번호 일치')
#     else:
#         print('주민번호 일치하지 않음')
# elif (checker == int(jumin[12])):
#     print('주민번호 일치')
# else:
#     print('주민번호 일치하지 않음')


# 개선버젼

jumin = '1111111111118'
sum = 0

weight = [2,3,4,5,6,7,8,9,2,3,4,5]


for i in range(len(weight)):
    sum += int(jumin[i]) * weight[i]

checker = (11 - (sum % 11)) % 10
# 11을 뺀 나머지가 2자리이든 1자리이든 상관없이 10을 나눠주면 된다


if (checker == int(jumin[12])):
    print('주민번호 일치!')
else:
    print('주민번호 불일치!')


# 35. 잔돈 계산 프로그램
# 금액을 지불하고 되돌려받는 잔돈을
# 10원, 50원, 100원, 500원, 1000원, 5000원, 10000원, 50000원 단위로 수량 계산

# 지불해야하는 금액 : 12340원
# 지불한 금액 : 100000원
# 잔돈은 어떻게 거슬러줘야 좋을까?

cost = 12340
money = 100000
charge = money - cost

# print(charge)
#
# # // = 몫을 구한다
# c50000 = charge // 50000
#
# #charge = charge - (50000 * c50000)
# charge = charge % 50000
# print(charge)
#
# c10000 = charge // 10000
# charge = charge % 10000
# print(charge)
#
#
# c5000 = charge // 5000
# charge = charge % 5000
# print(charge)
#
# c1000 = charge // 1000
# charge = charge % 1000
# print(charge)
#
# c500 = charge // 500
# charge = charge % 500
# print(charge)
#
# c100 = charge // 100
# charge = charge % 100
# print(charge)
#
# c50 = charge // 50
# charge = charge % 50
# print(charge)
#
# c10 = charge // 10
# charge = charge % 10
# print(charge)
#
#
# print('5만원권: %d, 1만원권: %d, 5천원권: %d, 1천원권: %d, 500원 동전: %d, 100원 동전 : %d, 50원 동전: %d, 10원동전: %d'
#       %(c50000, c10000, c5000, c1000, c500, c100, c50, c10))



# coins = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
# ctitle= ['5만원', '1만원', '5천원', '1천원', '500원', '100원', '50원', '10원']
#
# cqty =[0, 0, 0, 0, 0, 0, 0, 0]
#
# for i in range(len(coins)):
#     cqty[i] = charge // coins[i] #지폐/동전 수량 리스트에 몫을 넣는다
#     charge = charge % coins[i]   # 잔돈 변수에 나머지값을 계산해서 다시 넣는다
#     print(ctitle[i], cqty[i])



# ------------------------------------------------------------------#


# Q46. 특정 년도의 1월 달력
# 1년 1월 1일은 무슨 요일일까? : 월요일


# 먼저 0001-01-01의 요일 확인

import datetime

print(datetime.date(1,1,1).weekday())
# 0 이 뜬다

print(datetime.date(2018,11,30).weekday())
# 4 가 뜬다.

# 파이썬의 datetime요일은 월요일부터 시작 0이면 월요일


# 요일 표시하기
wday = ['월', '화','수', '목', '금', '토', '일']

wd = datetime.date(1,1,1).weekday() # 값은 0

print(wday[wd]) # 파이썬에서 0은 첫번째니까 첫번째 인덱스가 나온다 = 월

wd = datetime.date(2018, 11, 30).weekday()

print(wday[wd]) #금요일



# 수식으로 직접 하기
# 전년도 12월 31일 요일/ 해당년도 1월 1일
# 수식 : ((년도-1) * 365 + ((년도-1)//4 - (년도-1)//100 + (년도-1)//400)) % 7



#파이썬의 datetime과 다르게 수식으로 구하는 것은 일요일이 첫번째 날이라고 가정한다


# wdays= ['일','월', '화','수', '목', '금', '토']
# year = int(input('년도는?')) #2018을 넣을 예정
#
# wday = ((year-1) * 365 + ((year-1)//4 - (year-1)//100 + (year-1)//400)) % 7
# # 나눌 때 소수점으로 나오면 안되므로 // 를 써서 몫만 구하게 한다
#
# print(wday) # 0이 떴다
#
# # 전년도 마지막날의 요일
# print('%d년의 12월 31일은 %s요일' % (year-1, wdays[wday]))
# # 2017년의 12월 31일은 일요일 = 사실
#
# # 해당년도 첫째날의 요일
# print('%d년의 1월 1일은 %s요일' % (year, wdays[wday+1]))
# # 2018년의 1월 1일은 월요일 = 사실
#
#
# # 달력 만들기 (1월)
# print(wday)
#
# print('\n%d년 1월' % year)
#
# for i in range(len(wdays)):
#     print('%3s' % wdays[i], end='')
#
# print() # 줄바꿈용
#
# for i in range(wday+1):
#     print('%3s' % (' '), end=' ')
#
#
#
# for i in range(wday + 1 +1, 31 + wday+1 +1):
#     if i % 7 == 0:
#         print('%3d' % (i-wday-1), end = '\n')
#     else:
#         print('%3d' % (i-wday-1) , end=' ') # 날짜 출력





# Q47 만년달력
# 년도와 월을 입력하면 해당 월의 달력 출력

dayWeek = ['월', '화','수', '목', '금', '토', '일'] # 요일

months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 각 달의 총 일수
# #인덱스가 0부터 시작해서 헷갈리니 0을 앞에 넣어놓는다

isleap = False # 윤년 여부


year = int(input('년도는?'))
month = int(input('월은?'))

day = ((year-1) * 365 + ((year-1)//4 - (year-1)//100 + (year-1)//400)) % 7
# 입력 년도의 1월 1일의 요일 계산 = 첫번째 날을 월요일로 가정



isleap = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
# 윤년 여부 검사

if isleap == True:
    months[2] = 29
# 해당 년도가 윤년일 경우 2월을 29일로 변경


for i in range(month):
    day += months[i]

day = day % 7
# 해당 월 이전까지의 모든 일수 합산 후 요일 계산


# 요일 체크
print(year, month, dayWeek[day])
# 2018 년 11월 1일 = 목요일

print(isleap)
# False = 윤년 아님



# 달력 만들기

wdays= ['일','월', '화','수', '목', '금', '토']
# 달력에서 날짜를 일요일부터 찍기 위해 다시.

print(day)
print('\n%d년 %d월' % (year, month))

for i in range(len(wdays)):
    print('%3s' % wdays[i], end='')

print() # 줄바꿈용


for i in range(day + 1):
    print('%3s' % (' '), end=' ')


for i in range(day+1+1, months[month]+day+1+1):
    if i % 7 == 0:
        print('%3d' % (i-day-1), end = '\n')
    else:
        print('%3d' % (i-day-1) , end=' ') # 날짜 출력
