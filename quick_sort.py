def quock_sort(alist):
    if len(alist) <= 1:
        return alist
    right = []
    left = []
    mid = alist.pop()
    for i in alist:
        if i < mid:
            left.append(i)
        else:
            right.append(i)
    return quock_sort(left) + [mid] + quock_sort(right)

def maopao_sort(alist):
    for i in xrange(len(alist)):
        for j in xrange(len(alist)):
            if alist[i] < alist[j+1]:
                alist[i], alist[j+1] = alist[j+1], alist[i]
    return alist
    
    
alist1 = [1,5,3,7,7,7,9]
alist2 = [1,5,3,7,7,9,6,8]

aa = quock_sort(alist1)
print aa
print quock_sort(alist2)