def maxnum(list):
    most = list [0] 
    for i in list:
       if i > most:
        most = i
    print (most)
#example
maxnum([-9 , -10 , -32 , -43 ,-40 ,-2, -7])


def minnum(list):
    least = list [0] 
    for i in list:
       if i < least:
        least = i
    print (least)
#example
minnum([2, -3, 30, -90, -100 ,0])    

