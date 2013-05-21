import sys

def recursive_search(nowindexs, restkeys, restindexs):
    if not restindexs: return nowindexs
    
    for index in restindexs[::-1]:
        nextindexs = nowindexs+[index]

        nextrestkeys = [item for item in restkeys]

        try:
            print len(nowindexs)
            #print nowindexs, restkeys, restindexs
            #print index
            for item in chestinputs[index][1:]:
                nextrestkeys.remove(item)
        except ValueError:
            print "error"
            continue
                
        nextrestkeys.append(chestinputs[index][0])

        nextrestindexs = [ind for ind in restindexs]
        #print nextrestindexs
        #print index
        nextrestindexs.remove(index)


        ans = recursive_search(nextindexs, nextrestkeys, nextrestindexs)
        if ans: return ans

    return False
        
        
f_input = open(sys.argv[1])
problems = int(f_input.readline().rstrip())

for problem in xrange(problems):
    K,N = map(int, f_input.readline().rstrip().split(" "))
    keys = map(int, f_input.readline().rstrip().split(" "))

    chestinputs = [map(int, f_input.readline().rstrip().split(" ")) for i in xrange(N) ]

    restkeys = keys + reduce(lambda x,y: x+y, [line[1:] for line in chestinputs])
    print restkeys
    needkeys = [line[0] for line in chestinputs]
    print needkeys
    
    for item in needkeys:
        restkeys.remove(item)





        
    problemans = recursive_search([], restkeys, range(len(chestinputs)))
    if problemans:
        sys.stdout.write("Case #"+str(problem+1)+": ")
        for item in problemans[::-1]: sys.stdout.write(str(item+1)+" ")
        sys.stdout.write("\n")
    else:
        sys.stdout.write("Case #"+str(problem+1)+": "+"IMPOSSIBLE"+"\n")
