import sys
import random # сортировка вставками сортировка выбором
import time

numbers = 4000
max_r = 100000
t = 10
t_time = 0

def minimum(list):
    if len(list) == 0:
        return None
    m = 10**64
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


def insertion_sort(a): # вставками
    for i in range(1, len(a)):
        s = a[i]
        f = i - 1
        while (f >= 0 and s < a[f]):
            a[f + 1] = a[f]
            f = f - 1
        a[f + 1] = s
    return a
        

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
