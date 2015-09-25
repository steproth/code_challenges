filename = "B-large-practice.in"
f = open(filename, "r")
output = open("output.txt", "w+")
numcases = int(f.readline().strip("\n"))
print "File contains %s cases" % numcases

for case_count in range (0, numcases):
    item = []

    item = f.readline().split()
    item.reverse()
    out_line = "Case #%d: " % (case_count+1)
    output.write(out_line)
    output.write(" ".join(item))
    output.write("\r\n")
    #for item0_count in range(len(item), 0, -1):
            #out_line= "Case #%d: %d %d\r\n" %(case_count+1, item0_count+1, item1_count+1)
            #print "Case #%d: %d %d\r\n" %(case_count+1, item0_count+1, item1_count+1)
            #print "Case #%d: " % case_count+1
            #print 
            #output.write(out_line)
            
f.close()
output.close()
