def answer(meetings):
    #greedy alg

    #sort
    #loop
    myschedule = []
    meetings = sorted(meetings, key=lambda x: x[1])
    while meetings:
        print "meetings: " + str(meetings)
        #print "schedule: " + str(myschedule)
        nextmeeting = min(x[1] for x in meetings)
        #print "next meeting: " + str(nextmeeting) #3
        i = 0
        myschedule.append(meetings.pop(0))
        while meetings[0][0] <= nextmeeting:
            meetings.pop(0)
        
        print "\r\n"

    print "schedule: " + str(myschedule)
        

        

        
        #nextindex = meetings.index([x[1] for x in meetings if nextmeeting in x][1])
        #print "next index: " + str(nextindex)
        #print "next start: " + str(meetings[nextindex]) + "\tend: " + str(meetings[nextindex]) + "\r\n"
        
        
    #find min finish time
    #remove overlap
    return
    

t1 = [[0, 1], [1, 2], [2, 3], [3, 5], [4, 5]]
t2 = [[0, 1000000], [42, 43], [0, 1000000], [42, 43]]
t3 = [[0, 4], [0, 5], [2, 3], [3, 4], [4, 5]]

answer(t1)
answer(t2)
answer(t3)
