import copy
from collections import deque
n, w = map(int, input().split(" "))
crackers = deque(sorted([int(input()) for i in range(n)]))
mini = 0
if w > crackers[0] and w < crackers[-1]:
    mini = crackers[-1] - crackers[0]
else:
    mini = max(abs(w-crackers[-1]), abs(w-crackers[0]))
def maxit(next):
    crackerse = copy.deepcopy(crackers)
    ans = 0
    cur = w
    while crackerse:
        if next == 'MAD':
            node = crackerse.pop()
            next = 'LOL'
        else:
            node = crackerse.popleft()
            next = 'MAD'
        ans += max(abs(cur - node), abs(w - node))
        cur = node
    return ans

ans1 = maxit('LOL')
ans2 = maxit('MAD')
print(str(mini), str(max(ans1, ans2)))

#solution provided by astrocat879
#min is math to calculate: if the water is in the range of the hottest and coolest cracker, the minimum is the hottest - the coolest
#if water is out of the range, it's the water - the cracker farthest from it

#max is main challenge
#to calculate, we must consider two possibilities: starting from hottest vs starting from coolest
#our greedy algorithm will then go through all the crackers,
#choosing the largest difference between the current cracker and the farthest cracker, vs the water and the farthest cracker

