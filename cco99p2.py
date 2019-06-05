def abbreviation(k):

    if k in [13, 12, 11, 113, 112, 111, 1113, 1112, 1111]:
        return 'th'
    else:
        if len(str(k)) != 1:
            if str(k)[1] == '1':
                return 'st'
            elif str(k)[1] == '2':
                return 'nd'
            elif str(k)[1] == '3':
                return 'rd'
            else:
                return 'th'
        else:

            if k == 1:
                return 'st'
            elif k == 2:
                return 'nd'
            elif k == 3:
                return 'rd'
            else:
                return 'th'
n = int(input())
for testcase in range(n):
    occurences = {}
    m, k = map(int, input().split(" "))
    print(str(k)+abbreviation(k)+" most common word(s):")

    for i in range(m):
        word = input()
        if word in occurences:
            occurences[word] += 1
        else:
            occurences[word] = 1
    if len(occurences.keys()) >= k:
        sortedvalues = list(occurences.values())
        sortedvalues.sort(reverse=True)
        if k != 1:
            kthvalue = sortedvalues[k-1]
            if sortedvalues[k-2] != kthvalue:
                for i in occurences.keys():
                    if occurences[i] == kthvalue:
                        print(i)
        else:
            kthvalue = sortedvalues[0]
            for i in occurences.keys():
                if occurences[i] == kthvalue:
                    print(i)
    print("")
    
#legit the hardest part is the abbrievations.
