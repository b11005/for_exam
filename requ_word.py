#!usr/bin/python
#coding: utf-8

m = raw_input().split()
n = int(m[0])
k = int(m[1])
w = []
w_list = []

for i in range(n):
    w.append(raw_input())

if n <= 3:
    w_list.append(w[0] + w[2])
    w_list.append(w[2] + w[0])
else:
    for j in range(n):
        for k in range(n):
            if k == j + 1 or k == j - 1:
                continue
            else:
                w_list.append(w[j] + w[k])

result = [i[k] for i in w_list]

print min(result)


'''x = raw_input()
k = raw_input()

result = []

for i in range(10):
    temp = x + str(i)
    if int(temp) % int(k) == 0:
        result.append(int(temp))

for i in range(1, 10):
    temp = str(i) + x
    if int(temp) % int(k) == 0:
        result.append(int(temp))

print min(result)'''
