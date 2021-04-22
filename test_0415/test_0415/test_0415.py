# 1-3옆으로 볼록
#num = int(input("Insert the number: "))

#i, j = 0, 0
#target = num * 2 - 1

#count = 0

#while  count < target :
#    while j <= i :
#        print ("*", end = "")   
#        j += 1
#    print("")
#    if count < (num - 1) :
#        i += 1
#    else :
#        i -= 1

#    j = 0
#    count += 1

#-----------------------------------

#2-3번째 왼쪽으로 볼록

#num = int(input("Insert the number: "))

#i, j = 0, 0
#k = num - 1
#a = 0
#count = 0
#target = num * 2 - 1

#while count < target :
#    while a <= k:
#        print (end = " ")
#        a += 1
#    while j <= i:
#        print("*", end = "")
#        j += 1

#    print ("")
#    if count < (num - 1) :
#        i += 1
#        k -= 1
#    else :
#        i -= 1
#        k += 1

#    j = 0
#    a = 0
#    count += 1
#-----------------------------
# 1-4번째 정삼각형

#i = 0
#k = num // 2 + 1
#a, b = 0, 0
#m, n = 0, (k - 1)

#while i < k :
#    while m < n:
#        print(end = " ")
#        m += 1
#    while a <= b :
#        print("*", end = "")
#        a += 1
#    print("")
#    b += 2
#    a = 0
#    m = 0
#    n -= 1
#    i += 1

#-------------------------
# 2-4 번째 아래 정삼각형
#i = 0
#k = num // 2 + 1
#a, b = 0, num - 1
#m, n = 0, 0

#while i < k :
#     while m < n:
#        print(end = " ")
#        m += 1
#     while a <= b :
#        print("*", end = "")
#        a += 1
#     print("")
#     b -= 2
#     a = 0
#     m = 0
#     n += 1
#     i += 1


#---------------------------------------
# 1-5 번째 마름모
#i = 0
#k = num // 2 + 1
#a, b = 0, 0
#m, n = 0, (k - 1)
#count = 0

#while count < num :
#    while m < n:
#        print(end = " ")
#        m += 1
#    while a <= b :
#        print("*", end = "")
#        a += 1
#    print("")
#    count += 1
#    if count < k :
#        b += 2
#        n -= 1
#    else :
#        b -= 2
#        n += 1
#    a = 0
#    m = 0
#    i += 1

#---------------------------------------
# 2-5번째 모래시계

#i = 0
#k = num // 2 + 1
#a, b = 0, (num - 1)
#m, n = 0, 0
#count = 0

#while count < num :
#    while m < n:
#        print(end = " ")
#        m += 1
#    while a <= b :
#        print("*", end = "")
#        a += 1
#    print("")
#    count += 1
#    if count < k :
#        b -= 2
#        n += 1
#    else :
#        b += 2
#        n -= 1
#    a = 0
#    m = 0
#    i += 1

#------------------------------------------------
# 1-6번째 왼쪽 시작 사다리꼴

#i, j = 0, 0
#target = num * 2 - 1
#m, n = 0, 0
#count = 0

#while  count < target :
#    while m < n:
#        print(end = " ")
#        m += 1

#    while j <= i :
#        print ("*", end = "")   
#        j += 1
#    print("")
#    if count < (num - 1) :
#        i += 1
#    elif count == num - 1 :
#        i -= 1
#        n = 1
#    else :
#        i -= 1
#        n += 1
#    m = 0
#    j = 0
#    count += 1
#------------------------------
# 2-6 오른쪽 시작 사다리꼴
#i, j = 0, 0
#target = num * 2 - 1
#m, n = 0, num - 1
#count = 0

#while  count < target :
#    while m < n:
#        print(end = " ")
#        m += 1
#    while j <= i :
#        print ("*", end = "")   
#        j += 1
#    print("")
#    if count < (num - 1) :
#        i += 1
#        n -= 1
#    elif count == num - 1 :
#        i -= 1
#        n = 0
#    else :
#        i -= 1
#    m = 0
#    j = 0
#    count += 1

#-------------------리스트--------------------------------------
#aa = []
#for i in range(0, 4) :
#    aa.append(i)
#sum = 0
#for i in range(0, 4) :
#    aa[i] = int(input(    str(i + 1)    +  "번째 숫자: "))
#    sum += aa[i]
#print("합계 : %d" % sum)

#list1 = []
#list2 = []
#value = 1
#for i in range (0, 3) :
#    for i in range (0, 4) :
#        list1.append(value)
#        value += 1
#    list2.append(list1)
#    list1 = []


#for i in range (0, 3) :
#    for j in range(0, 4) :
#        print(list2[i][j], end =" ")
#    print("")


#list3 = [[0 for i in range(5)] for j in range(4)]
#value = 0
#for i in range(0, 4):
#    for j in range(0, 5):
#        list3[i][j] = value
#        value += 3

#for i in range(0, 4):
#    for j in range(0, 5) :
#        print("%3d" % list3[i][j], end = "")
#    print("")


#num = int(input("Insert the number: "))
#list1 = []
#list2 = []
#for i in range (0, num) :
#    for j in range(0, i + 1):
#        list1.append("*")
#    list2.append(list1)

#    list1 = []
#for i in range (0, num) :
#    for j in range (0, len(list2[i])) :
#        print(list2[i][j], end = "")
#    print("")


# 5번 다이아몬드
a = int(input("값 입력: "))
b = a//2 + 1
c = 1
i = 0
d = 1
for i in range(0, b, 1):
    for i in range(0, b-1, 1):
        print("_", end = "")
    for i in range(0, c, 1):
        print("*", end = "")
    c += 2
    b -= 1
    print("")
#변수 초기화
b = a // 2 + 1
k = a - 2
c = 1
i = 0
d = 1
for i in range(0, b-1, 1):
    for i in range(0, c, 1):
        print("_", end = "")
    for i in range(0, b + 1, 1):
        print("*", end = "")
    c += 1
    b -= 2
    print("")
#a = int(input("값 입력: "))
#b = a//2 + 1
#i = 0


