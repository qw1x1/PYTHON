import random as R
def criet_list(*args, long = 100):
    start, stop = args
    result_list = []
    for _ in range(long):
        result_list.append(R.randint(start, stop))
    return result_list
    
def quick_sort(a):
    if len(a) < 2:
        return a
    opora = a[0]
    l_baund = list(filter(lambda x: x < opora,a))
    midell = [k for k in a if k == opora]
    r_baund = [j for j in a if j > opora]

    return quick_sort(l_baund) + midell + quick_sort(r_baund)

print(quick_sort(criet_list(1, 1000, long = 1000)))

