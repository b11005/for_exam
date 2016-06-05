#!/usr/bin/env python

def divide(lis):
	if len(lis) == 1:
		return lis
	mean = len(lis)//2
	left = lis[:mean]
	right = lis[mean:]
	left = divide(left)
	right = divide(right)
	return list(merge(left,right))


def merge(left, right):
	index_left = index_right = 0
	result = []
	while len(left) > index_left and len(right) > index_right:
		if left[index_left] >= right[index_right]:
			result.append(right[index_right])
			index_right += 1
		else:
			result.append(left[index_left])
			index_left += 1
	if left:
		result.extend(left[index_left:])
	if right:
		result.extend(right[index_right:])
	return result


def main():
    lis = [5,2,4,6]
    print divide(lis)
    print divide([2,1,5,3])


if __name__ == '__main__':
    main()


