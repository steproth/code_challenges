import re

def convert_letter(letter):
    let2num = { #' ': 0,
                'a': 2,
                'b': 22,
                'c': 222,
                'd': 3,
                'e': 33,
                'f': 333,
                'g': 4,
                'h': 44,
                'i': 444,
                'j': 5,
                'k': 55,
                'l': 555,
                'm': 6,
                'n': 66,
                'o': 666,
                'p': 7,
                'q': 77,
                'r': 777,
                's': 7777,
                't': 8,
                'u': 88,
                'v': 888,
                'w': 9,
                'x': 99,
                'y': 999,
                'z': 9999
            }
    return let2num[letter]


filename = "C-small-practice.in"
f = open(filename, "r")
output = open("output.txt", "w+")
numcases = int(f.readline().strip("\n"))
print "File contains %s cases" % numcases

for case_count in range (0, numcases):
    item = [] #list of words
    #item = f.readline().split()
    item = re.split(r'(\s+)', f.readline())
    item.reverse()
    print item
    out_line = "Case #%d: " % (case_count+1)
    output.write(out_line)
    #if item: #list is not empty
        
        #for item_count in range (0, len(item)):#words
            #myletters = list(item.pop())
            #for letter_count in range (0, len(myletters)):
                #out_line = convert_letter(myletters[letter_count])
                #output.write("".join(str(out_line) + " "))    
    output.write("\r\n")

            
f.close()
output.close()
