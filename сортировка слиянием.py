import sys
import random # сортировка вставками сортировка выбором QuickSort слиянием
import time

#sys.setrecursionlimit(2000)
numbers = 8000
max_r = 100000
t = 10
t_time = 0

def minimum(list):
    if len(list) == 0:
        return None
    m = sys.maxsize
    for i in list:
        if i < m:
            m = i
    return m


def check_min(list, m):
    for i in list:
        if i < m:
            return False
    return True


def check(list_):
    for i in range(len(list_)-1):
        if list_[i] > list_[i+1]:
            return False
    return True

def generation(n, max_r):
    list_ = [0] * n
    for i in range(n):
        list_[i] = random.randint(-max_r, max_r)
    return list_


def bubble(list_):
    sw = True
    cnt = 1
    while sw:
        sw = False
        for i in range(len(list_) - cnt):
            if list_[i] > list_[i+1]:
                list_[i], list_[i+1] = list_[i+1], list_[i]
                sw = True
        cnt += 1
    return list_


def insertion_sort(a):
    for i in range(1, len(a)):
        for j in range(i, 0, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
            else:
                break
    return a


'''def insertion_binary(data):
	for i in range(len(data)):
		key = data[i]
		lo = 0
		hi = i - 1
		while lo < hi:
			mid = lo + (hi - lo) // 2
			if key < data[mid]:
				hi = mid
			else:
				lo = mid + 1
		for j in range(i, lo + 1, -1):
			data[j] = data[j - 1]
		data[lo] = key
	return data'''

def Merge(a, b):
    c = []
    ix1 = 0
    ix2 = 0
    while (ix1 < len(a)) and (ix2 < len(b)):
        if a[ix1] < b[ix2]:
            c.append(a[ix1])
            ix1 += 1
        else:
            c.append(b[ix2])
            ix2 += 1
            
    while (ix1 < len(a)):
        c.append(a[ix1])
        ix1 += 1
    while (ix2 < len(b)):
        c.append(b[ix2])
        ix2 += 1
        
    return c

    
def Merge_sort(a):
    d = []
    if len(a) <= 2:
        if len(a) == 1:
            return a
        if len(a) == 2:
            d.append(min(a))
            d.append(max(a))
            return d
    elif len(a) > 2:
        a[:(len(a) // 2)] = Merge_sort(a[:(len(a) // 2)])
        a[(len(a) // 2):] = Merge_sort(a[(len(a) // 2):])
        a = Merge(a[:(len(a) // 2)], a[(len(a) // 2):])
        return a
        

        
def Quick_sort(a):
    if len(a) <= 1:
        return a
    else:
        r = random.choice(a)
        b = [i for i in a if i < r]
        c = [i for i in a if i > r]
        d = [i for i in a if i == r]
        return Quick_sort(b) + d + Quick_sort(c)

              
def sort_select(list_):
    c = []
    m = sys.maxsize
    for i in range(len(list_)):
        for j in list_:
            if j < m:
                m = j
        c.append(m)
        list_.remove(m)
        m = sys.maxsize
    return c
                
def test(f):
    t_time = 0
    for i in range(t):
        list_ = generation(numbers, max_r)
        time1 = time.time()
        list_ = f(list_)
        time2 = time.time()
        t_time += time2 - time1
        if not(check(list_)):
            print(i)
            break

    print(t_time, t_time/t)

test(sorted)
test(bubble)
test(sort_select)
test(insertion_sort)
test(Merge_sort)
test(Quick_sort)
