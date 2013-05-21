import sys

f_input = open(sys.argv[1])
problems = int(f_input.readline().rstrip())


for count in xrange(problems):
    ## read ##
    numrow, numcolumn = map(int, f_input.readline().rstrip().split(" "))
    rowmap = [map(int, f_input.readline().rstrip().split(" ")) for k in xrange(numrow) ]
    #print rowmap
    #print numcolumn
    #print [[line[0] for line in rowmap] for i in xrange(numcolumn)]
    colmap = [[line[i] for line in rowmap] for i in xrange(numcolumn)]
    #print colmap
    
    ## indexing ##
    #levels = set()
    for x,y in ((a,b) for a in xrange(numrow) for b in xrange(numcolumn)):
        if max(rowmap[x]) > rowmap[x][y] and max(colmap[y]) > rowmap[x][y]:
            ans="NO"
            break
    else:
        ans="YES"

    sys.stdout.write("Case #"+str(count+1)+": "+ans+"\n")
    
    ## solve ##
    # for level in levels:
    #     for node in nodes[level]:
    #             print node
    #             if max(rowmap)
