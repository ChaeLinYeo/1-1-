def __print_result():
	import os
	os.system("cat result.txt")
def seq_search_closest(s,key):
	i=0 #위치번호
	k=0 #가까운 거리의 위치번호
	if s !=[]:
		d=abs(key-max(s))
		for x in s:
			if abs(x-key)<=d: #더 가까운 거리를 찾았을 걍우
				d=abs(x-key)
				k=i
			i+=1
		return k
	return None

def testcase():
    db = [3260, 74, 3341, 8122, 6179, 4277, 3266, 5025, 1177, 239, 3561, 1827, 4294, 2766, 2969, 2517, 4189, 3066, 5044, 9623]
    print("CASE 1")
    print("Expect: The closest value to 70 : 74 at index 1")
    key = 70
    index = seq_search_closest(db,key)
    if(index != None):
        print("Result: The closest value to",key,":",db[index],"at index",index)
        if index == 1:
            print("Correct")
        else:
            print("Failure")
    else:
        print("Result:",key,"found at",index)
        print("Failure")

    print("\nCASE 2")
    print("Expect: The closest value to 3263 : 3260 at index 0")
    print("    OR: The closest value to 3263 : 3266 at index 6")
    key = 3263
    index = seq_search_closest(db,key)
    if(index != None):
        print("Result: The closest value to",key,":",db[index],"at index",index)
        if index == 0 or index == 6:
            print("Correct")
        else:
            print("Failure")
    else:
        print("Result:",key,"found at",index)
        print("Failure")

    print("\nCASE 3")
    print("Expect: The closest value to 9891 : 9623 at index 19")
    key = 9891
    index = seq_search_closest(db,key)
    if(index != None):
        print("Result: The closest value to",key,":",db[index],"at index",index)
        if index == 19:
            print("Correct")
        else:
            print("Failure")
    else:
        print("Result:",key,"found at",index)
        print("Failure")

    print("\nCASE 4")
    print("Expect: 9891 found at None")
    key = 9891
    index = seq_search_closest([],key)
    if(index != None):
        print("Result: The closest value to",key,":",db[index],"at index",index)
        print("Failure")
    else:
        print("Result:",key,"found at",index)
        print("Correct")
testcase()