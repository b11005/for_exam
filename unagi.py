import sys
n, m = map(int, raw_input().split())
#n = 12
#customer = [map(int, i.split()) for i in sys.stdin]
customer = [[4, 6],[4, 8],[4, 10],[4, 12],[4, 2],[4, 4]]
seats = {i:0 for i in range(1, n + 1)}
result = 0
for j in customer:
    if j[0] + j[1] > n:
        temp = (j[0] + j[1]) - (n + 1)
        for k in range(j[1], n + 1):
            if not seats[k]:
                result += 1
                seats [k] = 1
            else:
                break
        for l in range(1, temp):
            if not seats[l]:
                result += 1
                seats[l] = 1
            else:
                break
    else:
        for k in range(j[1], j[0] + j[1]):
            if not seats[k]:
                result += 1
                seats[k] = 1
            else:
                break
            '''total = []
            if seats[k]:
                break
            else:
                if seats[k] not in total:
                    total.append(seats[k])
                else:
                    break
            if j[0] == len(total):
                for h in total:
                    seats[h] = 1
                    result += 1'''
print seats
print result
