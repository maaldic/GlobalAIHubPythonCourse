import math
myList = [1,2,3,4,5]
print(myList)
number_of_elements = len(myList)
two_pieces = len(myList)/2

if two_pieces%2==0:
    x = int(two_pieces)
    temp_list = myList[0:x]
    myList[0:x]=myList[x:len(myList)]
    myList[x:len(myList)]=temp_list
    print(myList)
else:
    y = math.ceil(two_pieces)
    #y = round(two_pieces)
    temp_list = myList[0:y-1]
    myList[0:y-1] = myList[y-1:len(myList)]
    myList[y:len(myList)] = temp_list
    print(myList)



