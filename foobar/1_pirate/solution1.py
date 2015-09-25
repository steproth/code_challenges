def answer(numbers):
    for i in range (1 ,len(numbers)):
        for j in range (i, 0, -1):
            print "**" + str(j)
            if numbers[j-1] == numbers[i]:
                return i-j+1
    return 2#len(numbers)
                
t1 = [0, 6, 7, 1, 2, 3, 4, 1, 6, 1]
t2 = [0, 1, 0]
t3 = [0, 1, 2, 3, 4, 5]
t4 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 1]

print str(answer(t1))
#print str(answer(t2))
#print str(answer(t3))
#print str(answer(t4))
