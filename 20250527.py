#조건문 반복문 문제풀이

# count = 0
# while count < 9:
#     print("{0}번 반복".format(count))
#     count += 1

# while count < 9:
#     count += 1
#     if count % 2 == 0:
#         print("{0}번 반복".format(count))

# 별문제(for랑 while 둘다)
# n = int(input())
# star = 1
# while star <= n:
#     print("*" * star)
#     star += 1
# for star in range(1, n+1):
#     i = 0
#     while i < star:
#         print("*", end="")
#         i += 1
#     print("") 


#구구단
# st_num = input()
# for num in range(1,10):
#     print("{0} X {1} = ".format(st_num,num)+ str((int(st_num) * num)) ) # 1가로로,2. 입력안받고 가로 9까지 세로로도 9까지지

# 2배수 더하기
# n = int(input())
# sum_2 = 0
# for mul_2 in range(2, n+1, 2):
#     sum_2 += mul_2
# print(sum_2)

# 카운트다운
# n = int(input())
# for i in range (0,n):
#     print(n - i)

# 숫자 삼각형
# n = int(input())

# for num in range(1,n + 1):
#     for i in range(1, num + 1):
#         print(i, end="")
#     print()


#1. range 간격 1로 ex range(N)
# n = int(input())
# if 1 <= n and n<= 1000:
#     hab = 0
#     for num in range(1,n + 1):
#         if num % 3 == 0:
#             hab += num
#     print(hab)
# else:
#     print("X")

# #2. 구구단(가로)
# st_num = int(input())
# for num in range(1,10):
#      print("{0} X {1} = {2}".format(st_num, num, st_num * num),end="\t" )

#2. 구구단(입력x 가로세로)
# for width in range(1,10):
#     for length in range(1,10):
#         print(f"{length} X {width} = {width * length}",end="\t" )
#     print()

#손님 태우기기
# from random import *
# count = 0
# for customer in range(1,51):
#     time = randint(5,51)
#     if 5 <= time and time <= 15:
#         print(f"[o] {customer}번째 손님 (소요시간 : {time}분)")
#         count += 1
#     else:
#         print(f"[ ] {customer}번째 손님 (소요시간 : {time}분)")
# print(f"총 탑승객 : {count}명")