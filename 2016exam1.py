# 아래 뼈대코드는 코드 작성에 도움을 주기 위해서 제공되는 것일 뿐이니,
# 굳이 따를 필요는 없습니다.
# 무시하고 자신의 코딩 스타일을 고수해도 논리만 맞고 제대로 작동하기만 하면 됩니다.

##### 2 #####
# 백일 계산하기
# 양수 인수만 제대로 처리하면 된다. 즉, 인수가 양수인지는 함수 호출하기 전에 이미 확인했다고 가정한다.

def is_leap_year(year):
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0

### A ###
def is_valid_date(year,month,day):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if day <= 31: # 이 부분을 채워 넣자.
            return True
        else:
            return False
    elif month == 4 or month == 6 or month == 9 or month ==11:
        if day <=30:
            return True
        else:
            return False
    elif month == 2:
        if is_leap_year(year)==False:
            if day <=28:
                return True
            else:
                return False
        if is_leap_year(year)==True:
            if day <=29:
                return True # 이 부분에 년,월,일을 연관짓는 논리식을 작성하여 채워넣자.
            else:
                return False
# test cases
# print(is_valid_date(2016,4,25)) # => True
# print(is_valid_date(2016,2,29)) # => True
# print(is_valid_date(2017,2,29)) # => False
# print(is_valid_date(2016,4,31)) # => False

### B ###
def next_month(year,month):
    if month<12:
        return (year,month+1)
    elif month == 12:
        return (year+1, month)

# test cases
# print(next_month(2016,4))  # => (2016, 5)
# print(next_month(2016,12)) # => (2017, 1)

### C ###
def days_in_month(year,month): # 아래 True를 적절한 논리식으로 바꾸자.
    if True: # True를 적절한 논리식으로 바꾸자.
        return 31
    elif True: # True를 적절한 논리식으로 바꾸자.
        return 30
    elif True: # True를 적절한 논리식으로 바꾸자.
        if True: # True를 적절한 논리식으로 바꾸자.
            return 29
        else:
            return 28
    else:
        return 0

# test cases
# print(days_in_month(2016,4)) # => 30
# print(days_in_month(2016,12)) # => 31
# print(days_in_month(2016,2)) # => 29
# print(days_in_month(2017,2)) # => 28
# print(days_in_month(2016,13)) # => 0

### D ###
def hundred_days_from(year,month,day):
    days_to_go = 100 - (days_in_month(year,month) - day)
    pass # 이 부분을 채워 넣자.
    while True: # True를 적절한 논리식으로 바꾸자.
        pass # 이 부분을 채워 넣자.
    return (year, month, days_to_go)

# print(hundred_days_from(2015,12,25)) # => (2016, 4, 3)
# print(hundred_days_from(2016,4,17)) # => (2016, 7, 26)
# print(hundred_days_from(2016,10,18)) # => (2017, 1, 26)
# print(hundred_days_from(2016,12,25)) # => (2017, 4, 4)


##### 3 #####
# factorial
# 0과 양수 인수만 제대로 처리하면 된다. 
# 즉, 인수가 음이 아닌지는 함수 호출하기 전에 이미 확인했다고 가정한다.

def fac0(n):
    if n > 0:
        return n * fac0(n-1)
    else:
        return 1

### A ###
def fac1(n):
    def loop(n,fac): # 꼬리 재귀
        if n > 0:
            return loop(n-1, n*fac)
        else:
            return fac
    return loop(n,1)

### B ###
def fac2(n):
    fac=[]
    while n > 0: # while 문
        n=n-1
        fac = n*fac
    return fac

### C ###
def fac3(n):
    s=range(n)
    fac=1
    for i in s: # for 
        if n > 0:
            n=n-1
            fac=n*fac
        else:
            return fac
    return fac

# print(fac0(0)) # => 1
# print(fac1(0)) # => 1
# print(fac2(0)) # => 1
# print(fac3(0)) # => 1
# print(fac0(5)) # => 120
# print(fac1(5)) # => 120
# print(fac2(5)) # => 120
# print(fac3(5)) # => 120


##### 4 #####
# 덧셈만으로 제곱 계산
# 작성한 함수는 정수 인수에 대해서 제대로 작동하면 된다. 
# 그런데 앞 문제와는 달리 음수 인수에 대해서도 제대로 작동해야 함을 명심하자.

def square0(n):
    def loop(n):
        if n > 0:
            return 2*n-1 + loop(n-1) # 여기에 적절한 식을 채워 넣자.
        else:
            return 0
    return loop(abs(n)) # 음수를 처리하려면 이 부분을 손봐야 한다.

def square1(n):
    def loop(n,sum): # 꼬리 재귀
        if n >0:
            return loop(n-1, sum+(2*n-1))
        else:
            return sum
    return loop(abs(n),0)

def square2(n):
    sum=0
    n=abs(n)
    while n>0: # while 문
        sum = sum+(2*n-1)   
        n=n-1
    return sum
def square3(n):
    sum=0
    n=abs(n)
    for i in range(1,n+1): # for 문
        i= 2*i -1
        sum=sum+(2*n-1)
    return sum

# print(square0(0)) # => 0
# print(square0(1)) # => 1
# print(square0(-2)) # => 4
# print(square0(3)) # => 9
# print(square0(-4)) # => 16
# print(square0(5)) # => 25

# print(square1(0)) # => 0
# print(square1(1)) # => 1
# print(square1(-2)) # => 4
# print(square1(3)) # => 9
# print(square1(-4)) # => 16
# print(square1(5)) # => 25

#print(square2(0)) # => 0
# print(square2(1)) # => 1
# print(square2(-2)) # => 4
# print(square2(3)) # => 9
# print(square2(-4)) # => 16
# print(square2(5)) # => 25

#print(square3(0)) # => 0
# print(square3(1)) # => 1
# print(square3(-2)) # => 4
# print(square3(3)) # => 9
# print(square3(-4)) # => 16
# print(square3(5)) # => 25


##### 5 #####
# 순열 permutation
# assume: n > 0, k > 0, n >= k
# 양수 인수만 제대로 처리하면 된다. 
# 즉, 인수가 양수인지는 함수 호출하기 전에 이미 확인했다고 가정한다. 
# 그리고  n < k 인 경우에는 0을 내주도록 해야 한다.

def permutation0(n,k):
    if k > 0:
        return n-k+1 # 여기에 적절한 식을 채워 넣자.
    else:
        return 1

def permutation1(n,k):
    def loop() # 꼬리 재귀

def permutation2(n,k):
    a=[] # while 문
    while k>0:
        n,k=n,k-1
    return a

def permutation3(n,k):
    s=range(n)
    for i in s: # for 문
       if k>0:
            n=n-1
            k=k-1
        else:
           return 

# print(permutation0(1,1)) # => 1
# print(permutation0(2,1)) # => 2
# print(permutation0(2,2)) # => 2
# print(permutation0(3,1)) # => 3
# print(permutation0(3,2)) # => 6
# print(permutation0(3,3)) # => 6
# print(permutation0(4,1)) # => 4
# print(permutation0(4,2)) # => 12
# print(permutation0(4,3)) # => 24
# print(permutation0(4,4)) # => 24

# print(permutation1(1,1)) # => 1
# print(permutation1(2,1)) # => 2
# print(permutation1(2,2)) # => 2
# print(permutation1(3,1)) # => 3
# print(permutation1(3,2)) # => 6
# print(permutation1(3,3)) # => 6
# print(permutation1(4,1)) # => 4
# print(permutation1(4,2)) # => 12
# print(permutation1(4,3)) # => 24
# print(permutation1(4,4)) # => 24

# print(permutation2(1,1)) # => 1
# print(permutation2(2,1)) # => 2
# print(permutation2(2,2)) # => 2
# print(permutation2(3,1)) # => 3
# print(permutation2(3,2)) # => 6
# print(permutation2(3,3)) # => 6
# print(permutation2(4,1)) # => 4
# print(permutation2(4,2)) # => 12
# print(permutation2(4,3)) # => 24
# print(permutation2(4,4)) # => 24

# print(permutation3(1,1)) # => 1
# print(permutation3(2,1)) # => 2
# print(permutation3(2,2)) # => 2
# print(permutation3(3,1)) # => 3
# print(permutation3(3,2)) # => 6
# print(permutation3(3,3)) # => 6
# print(permutation3(4,1)) # => 4
# print(permutation3(4,2)) # => 12
# print(permutation3(4,3)) # => 24
# print(permutation3(4,4)) # => 24


##### 6 #####

def drop_before(s,index):
    if s != [] and index > 0:
        return drop_before(s[1:],index-1)
    else:
        return s

### A ###  
def drop_before(s,index):
    a=[]
    while s != [] and index >0:
        s=s[1:]
        index=index-1
    return a # while 문 버전

# s = [1,2,3,4,5]
# print("s = [1,2,3,4,5]")
# print("drop_before(s,0) =", drop_before(s,0)) 
# print("drop_before(s,1) =", drop_before(s,1))
# print("drop_before(s,2) =", drop_before(s,2))
# print("drop_before(s,3) =", drop_before(s,3))
# print("drop_before(s,4) =", drop_before(s,4))
# print("drop_before(s,5) =", drop_before(s,5))
# print("drop_before(s,6) =", drop_before(s,6))
# print("drop_before(s,-3) =", drop_before(s,-3))
# print("drop_before([],4) =", drop_before([],4))

### B ###
def take_before(s,index):
    pass  # 재귀
 
def take_before(s,index):
    pass  # 꼬리 재귀

def take_before(s,index):
    pass  # while 문

# s = [1,2,3,4,5]
# print("take_before(s,0) =", take_before(s,0))
# print("take_before(s,1) =", take_before(s,1))
# print("take_before(s,2) =", take_before(s,2))
# print("take_before(s,3) =", take_before(s,3))
# print("take_before(s,4) =", take_before(s,4))
# print("take_before(s,5) =", take_before(s,5))
# print("take_before(s,6) =", take_before(s,6))
# print("take_before([],4) =", take_before([],4))
# print("take_before(s,-3) =", take_before(s,-3))

### C ###
def sublist(s,low,high):
    if low < 0: low = 0
    if high < 0: high = 0
    if low <= high:
        return None # 여기에 알맞은 식을 채워 넣자.
    else:
        return []

# s = [1,2,3,4,5]
# print("s = [1,2,3,4,5]")
# print("sublist(s,0,0) => [] ?", sublist(s,0,0))
# print("sublist(s,0,1) => [1] ?", sublist(s,0,1))
# print("sublist(s,0,2) => [1, 2] ?", sublist(s,0,2))
# print("sublist(s,0,3) => [1, 2, 3] ?", sublist(s,0,3))
# print("sublist(s,0,4) => [1, 2, 3, 4] ?", sublist(s,0,4))
# print("sublist(s,0,5) => [1, 2, 3, 4, 5] ?", sublist(s,0,5))
# print("sublist(s,0,6) => [1, 2, 3, 4, 5] ?", sublist(s,0,6))
# print("sublist(s,1,1) => [] ?", sublist(s,1,1))
# print("sublist(s,1,2) => [2] ?", sublist(s,1,2))
# print("sublist(s,1,3) => [2, 3] ?", sublist(s,1,3))
# print("sublist(s,1,4) => [2, 3, 4] ?", sublist(s,1,4))
# print("sublist(s,1,5) => [2, 3, 4, 5] ?", sublist(s,1,5))
# print("sublist(s,1,6) => [2, 3, 4, 5] ?", sublist(s,1,6))
# print("sublist(s,2,2) => [] ?", sublist(s,2,2))
# print("sublist(s,2,3) => [3] ?", sublist(s,2,3))
# print("sublist(s,2,4) => [3, 4] ?", sublist(s,2,4))
# print("sublist(s,2,5) => [3, 4, 5] ?", sublist(s,2,5))
# print("sublist(s,2,6) => [3, 4, 5] ?", sublist(s,2,6))
# print("sublist(s,3,3) => [] ?", sublist(s,3,3))
# print("sublist(s,3,4) => [4] ?", sublist(s,3,4))
# print("sublist(s,3,5) => [4, 5] ?", sublist(s,3,5))
# print("sublist(s,3,6) => [4, 5] ?", sublist(s,3,6))
# print("sublist(s,5,2) => [] ?", sublist(s,5,2))
# print("sublist(s,-3,-2) => [] ?", sublist(s,-3,-2))


##### 7 #####
# 빈 숫자열("")은 함수 호출 전에 이미 확인했다고 가정하고 처리하지 않기로 한다.

def longest_streak0(s):
    contender = leader = s[0]
    streak_length = streak_record = 1 
    for n in s[1:]:
        if n == contender:
            streak_length += 1
        else:
            contender = n
            streak_length = 1
        if streak_length > streak_record:
            leader = contender
            streak_record = streak_length
    return (leader, streak_record)

# def test_longest_streak(s):
#     for n in s:
#         print(n,end="")
#     print()
#     print(longest_streak0(s))

# s0 = "06479019955907200041185008780528384811265678111671"
# test_longest_streak(s0) 
# # => ('0', 3)
# s1 = "49715114250863455559013207228395154984882560834674"
# test_longest_streak(s1) 
# # => ('5', 4)
# s2 = "79083787262159815638834042282485195270836937488097"
# test_longest_streak(s2) 
# # => ('8', 2)
# s3 = "36888653851748777011129000999371447120618209984726"
# test_longest_streak(s3) 
# # => ('8', 3)

### A ###
def longest_streak1(s):
    contender = leader = s[0]
    streak_length = streak_record = 1
    contender_index = leader_index = 0
    index = 1
    for n in s[1:]:
        pass # 이 부분을 채워 넣자.
        index += 1
    return leader, streak_record, leader_index

# def test_longest_streak(s):
#     for n in s:
#         print(n,end="")
#     print()
#     print(longest_streak1(s))

# s0 = "06479019955907200041185008780528384811265678111671"
# test_longest_streak(s0) 
# # => ('0', 3, 15)
# s1 = "49715114250863455559013207228395154984882560834674"
# test_longest_streak(s1) 
# # => ('5', 4, 15)
# s2 = "79083787262159815638834042282485195270836937488097"
# test_longest_streak(s2) 
# # => ('8', 2, 19)
# s3 = "36888653851748777011129000999371447120618209984726"
# test_longest_streak(s3) 
# # => ('8', 3, 2)

### B ###
def longest_streak2(s):
    contender = leader = s[0]
    streak_length = streak_record = 1
    contender_index = leader_index = 0
    ties = []
    index = 1
    for n in s[1:]:
        pass # 이 부분을 채워 넣자.
        index += 1
    return [(leader, streak_record, leader_index)] + ties
    
# def test_longest_streak(s):
#     for n in s:
#         print(n,end="")
#     print()
#     print(longest_streak2(s))

# s0 = "06479019955907200041185008780528384811265678111671"
# test_longest_streak(s0) 
# # => [('0', 3, 15), ('1', 3, 44)]
# s1 = "49715114250863455559013207228395154984882560834674"
# test_longest_streak(s1) 
# # => [('5', 4, 15)]
# s2 = "79083787262159815638834042282485195270836937488097"
# test_longest_streak(s2) 
# # => [('8', 2, 19), ('2', 2, 25), ('8', 2, 45)]
# s3 = "36888653851748777011129000999371447120618209984726"
# test_longest_streak(s3) 
# # => [('8', 3, 2), ('7', 3, 14), ('1', 3, 18), ('0', 3, 23), ('9', 3, 26)]




