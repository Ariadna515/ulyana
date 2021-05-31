def find_min_index(a,i=0):
    m = i
    l = len(a)
    while i < l:
        if a[i] < a[m]:
            m = i
        i = i + 1
    return m


def fill_the_array():
    a = []
    while True:
        s = input()
        if s == "":
            break
        e = int(s)
        a.append(e)
    return a


a = fill_the_array()
m = find_min_index(a)
x = a[m]


def swap(a,i,e):
    x = a[i]
    a[i] = a[e]
    a[e] = x


def sort(a):
    i = 0
    l = len(a)
    while i < l:
        x = find_min_index(a,i)
        swap(a,i,x)
        i = i + 1


def median(a):
    l = len(a)
    m = int(l/2)
    sort(a)
    if l % 2 == 0:  # even
        x = a[m-1]
        y = a[m]
        return (x+y)/2.0
    else:  # odd
        return a[m]


print("median of", a)
m = median(a)
print('sorted', a)
print(m)