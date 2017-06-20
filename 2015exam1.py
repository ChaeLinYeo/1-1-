#2 윤년검사 함수
def isleapyear(year):
    return int(year)%4==0 and (int(year)%400==0 or int(year)%100!=0)

# test case
if __name__ == "__main__":
    for y in range(5):
        print(y,isleapyear(y))
    for y in range(2010,2017):
        print(y,isleapyear(y))
    for y in range(1900, 2600, 100):
        print(y,isleapyear(y))
# expected results
# 0 True
# 1 False
# 2 False
# 3 False
# 4 True
# 2010 False
# 2011 False
# 2012 True
# 2013 False
# 2014 False
# 2015 False
# 2016 True
# 1900 False
# 2000 True
# 2100 False
# 2200 False
# 2300 False
# 2400 True
# 2500 False

#3 문자열 처리하기 (for 문 사용)
def fillwith_(sentence):
    new_sentence = ''
    for char in sentence:
        pass            
    return new_sentence

#print(fillwith_('아름다운 가을 단풍 구경하러 산으로 갑시다.'))
#print(fillwith_("나는 한양대학교 컴퓨터공학과 학생이 되어 너무 행복하다."))

#4 add range (가정 step > 0) for 버전
def add_range(start,stop,step):
    pass

#print(add_range(5,13,2))

#5 other add ranges
def add_range0(start,stop,step):
    pass

def add_range1(start,stop,step):
    pass
    
def add_range2(start,stop,step):
    pass

#6 모음을 일련번호매기기
def vowel_numbering(word):
    pass 
    for c in s:
        if c in ['a','e','i','o','u','A','E','I','O','U']:
            pass
        else:
            pass
    return newword

#print(vowel_numbering('Massachussettes'))


#7 리스트에서 가장 큰 수 찾기
# 인수로 리스트만 들어온다고 가정해도 좋다.
def greatest0(s):
    def loop(s,top):
        if s != []:
            if s[0] > top:
                return loop(s[1:],s[0])
            else:
                return loop(s[1:],top)
        else:
            return top
    if len(s) == 0:
        return None
    else:
        return loop(s[1:],s[0])

def greatest1(s):
    pass

def greatest(s):
    pass

#print(greatest([5,2,3,6,4,3,7,5,8,2])) # 8
#print(greatest([5,2])) # 5
#print(greatest([5])) # 5
#print(greatest([])) # None

#8 rankith
def rankith(s,i):
    pass

#print(rankith([5,2,3,6,4,3,7,5,8,2],1)) # 8
#print(rankith([5,2,3,6,4,3,7,5,8,2],2)) # 7
#print(rankith([5,2,3,6,4,3,7,5,8,2],4)) # 5
#print(rankith([5,2,3,6,4,3,7,5,8,2],5)) # 5
#print(rankith([5,2,3,6,4,3,7,5,8,2],6)) # 4
#print(rankith([5,2],2)) # 2
#print(rankith([5],1)) # 5
#print(rankith([],1)) # None
    
#9 연속적으로 많이 반복된 수의 반복 횟수
def longest_repetition(s):
    if s != []:
        record = s[0]
        recordtimes = 1
        on = s[0]
        ontimes = 1
        for n in s[1:]:
            pass
        return (record,recordtimes)
    else:
        return (None,0)

#print(longest_repetition([5,5,4,4,4,4,4,2,2,2,2,7,8,4,4,3,3,3]))
#print(longest_repetition([2,2,2]))
#print(longest_repetition([]))






