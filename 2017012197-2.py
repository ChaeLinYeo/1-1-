def __print_result():
	import os
	os.system("cat result.txt")
def bin_search_closest(ss,key):
	low = 0#최소
	high = len(ss) - 1#최대
	while low <= high: #최소<=최대
		mid = (high + low) // 2 #중간값을 낸다
		if key == ss[mid]: #키가 중간값과 같을때
			return mid #중간값을 돌려준다
		elif key < ss[mid]: #키가 중간값보다 작을때
			high = mid - 1 #최대는 중간값-1이다
		else: #키가 중간값보다 클 때	
			low = mid + 1 #최소는 중간값+1이다
		if abs(ss[low]-key) > abs(ss[high]-key):
			return high
		elif abs(ss[low]-key) < abs(ss[high]-key):
			return low




def testcase():
    db = [3260, 74, 3341, 8122, 6179, 4277, 3266, 5025, 1177, 239, 3561, 1827, 4294, 2766, 2969, 2517, 4189, 3066, 5044, 9623]
    db.sort()
    print("CASE 1")
    print("Expect: The closest value to 70 : 74 at index 0")
    key = 70
    index = bin_search_closest(db,key)
    if(index != None):
        print("Result: The closest value to",key,":",db[index],"at index",index)
        if index == 0:
            print("Correct")
        else:
            print("Failure")
    else:
        print("Result:",key,"found at",index)
        print("Failure")

    print("\nCASE 2")
    print("Expect: The closest value to 3263 : 3260 at index 8")
    print("    OR: The closest value to 3263 : 3266 at index 9")
    key = 3263
    index = bin_search_closest(db,key)
    if(index != None):
        print("Result: The closest value to",key,":",db[index],"at index",index)
        if index == 8 or index == 9:
            print("Correct")
        else:
            print("Failure")
    else:
        print("Result:",key,"found at",index)
        print("Failure")

    print("\nCASE 3")
    print("Expect: The closest value to 9891 : 9623 at index 19")
    key = 9891
    index = bin_search_closest(db,key)
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
    index = bin_search_closest([],key)
    if(index != None):
        print("Result: The closest value to",key,":",db[index],"at index",index)
        print("Failure")
    else:
        print("Result:",key,"found at",index)
        print("Correct")
testcase()