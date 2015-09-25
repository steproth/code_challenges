filename = "test1.txt"
f = open(filename, "r")
output = open("output.txt", "w+")
numcases = int(f.readline().strip("\n"))
print "File contains %s cases" % numcases

for case_count in range (0, numcases):
    total = int(f.readline().strip("\n"))
    numitems = int(f.readline().strip("\n"))
    item = []

    item = f.readline().split()
    item = [int(i) for i in item]
    for item0_count in range(0, numitems):
        for item1_count in range(item0_count+1, numitems):
            if (item[item0_count] + item[item1_count]) == total:
                out_line= "Case #%d: %d %d\r\n" %(case_count+1, item0_count+1, item1_count+1)
                output.write(out_line)
f.close()
output.close()
