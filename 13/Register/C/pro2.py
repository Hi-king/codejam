import sys

def generate_palindrome(digit_limit):
    nums=[range(1, 10), [x*10+x for x in xrange(1, 10)] ]
    
    for digit in xrange(2, digit_limit):
        nums.append([x*10**digit+y*10+x for x in xrange(1, 10) for y in nums[digit-2]])
    return reduce(lambda x,y:x+y, nums)

    #print generate_palindrome(3)


candidates = generate_palindrome(40)
alss = generate_palindrome(80)
#ans2 = [y for y in [x*x for x in candidates] if y in alss]
#ans = [x*x for x in candidates]

nowindex = 0
ans = []
for x in candidates:
    #print x
    nowcandidate = x*x
    while nowcandidate>alss[nowindex]:
        nowindex+=1
    else:
        if nowcandidate==alss[nowindex]:
            ans.append(nowcandidate)
            #print ans



f_input = open(sys.argv[1])
problems = int(f_input.readline().rstrip())

for i in xrange(problems):
    a,b = map(int, f_input.readline().rstrip().split(" "))

    nums = [num for num in ans if a<=num and b>=num]

    #print a,b
    #print ans
    #print nums
    sys.stdout.write("Case #"+str(i+1)+": "+str(len(nums))+"\n")
