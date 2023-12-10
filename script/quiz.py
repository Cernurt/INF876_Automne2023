import numpy as np

def itob(N):
    s = ''
    while N > 1:
        s = str(N%2) + s
        N = N//2
    s = str(N) + s
    return s

def bingap(N):
    gap = 0
    tmp = -1
    while N > 1:
        r = N%2        
        if r == 1:
            if tmp > gap:
                gap = tmp
            tmp = 0  
        elif tmp > -1:
            tmp += 1
        N //= 2
    if N == 1:
        if tmp > gap:
            gap = tmp
    return gap

def reverse(A, i, j):
    while i < j:
        tmp = A[j]
        A[j] = A[i]
        A[i] = tmp
        i+=1
        j-=1
    
def rotate(A, K):
    if A:
        K = K % len(A)
        if K > 0:
            reverse(A, 0, len(A)-1)
            reverse(A, 0, K-1)
            reverse(A, K, len(A)-1)
    return A

def tape_diff_slow(A):
    md = None
    for p in range(1, len(A)):
        d = abs(sum(A[:p])-sum(A[p:]))
        # print(d)
        md = d if md is None or d < md else md
    print('min diff: ' + str(md))


def tape_diff(A, n, s1, s2):
    if n < 0:
        return abs(s1-s2)
    else:
        inc = tape_diff(A, n-1, s1+A[n], s2)
        exc = tape_diff(A, n-1, s1, s2+A[n])
        return min(inc, exc)

def tape_diff_fast(A):
    return tape_diff(A, len(A)-1, 0, 0)

A = [3,1,2,4,3]
A = np.random.randint(-1000, 1000, 100)
print(A)
print(tape_diff_fast(A))