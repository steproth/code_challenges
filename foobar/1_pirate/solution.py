def answer(numbers):
    nextpirate = numbers[0]
    visited = []
    visited.append(nextpirate)
    while(visited.count(numbers[nextpirate]) < 1):
        visited.append(numbers[nextpirate])
        nextpirate = numbers[nextpirate]
    #there is a loop. now find the length of it
    visited.append(numbers[nextpirate])
    for i in range (len(visited)-2, 1, -1):
        if visited[i] == visited[len(visited)-1]:
            return len(visited)-1-i
    return len(visited)-1
                
t1 = [1, 0] #2
t2 = [1, 2, 1] #2
t3 = [1, 3, 0, 1] #2
t4 = [1, 2, 3, 1] #3
t5 = [1, 2, 3, 7, 10, 15, 1, 4, 11, 5, 8, 9, 1, 1, 1, 3] #4
#     0  1  2  3  4   5  6  7    8  9  10 11,12,13,14,15
# 1, 2, 3, 4, 2
print str(answer(t1)) + "\r\n"
print str(answer(t2)) + "\r\n"
print str(answer(t3)) + "\r\n"
print str(answer(t4)) + "\r\n"
print str(answer(t5)) + "\r\n"
#x[n] = n[x]
