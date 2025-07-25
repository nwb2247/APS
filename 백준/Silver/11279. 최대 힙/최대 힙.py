import sys
input = sys.stdin.readline

N = int(input())

heap = [0]*(N+2)
size = 0

def add(num) :
    global size
    size += 1
    i = size
    heap[i] = num
    while i > 1 :
        p = i//2
        if heap[p] < heap[i] :
            heap[p], heap[i] = heap[i], heap[p]
            i = p
        else :
            break

def pop() :
    global size
    if size == 0 :
        return 0
    mx = heap[1]
    heap[1] = heap[size]
    heap[size] = 0
    size -= 1
    i = 1
    while True :
        left = i*2
        right = i*2+1
        if left > size :
            break
        elif right > size :
            if heap[i] < heap[left] :
                heap[left], heap[i] = heap[i], heap[left]
                i = left
            else :
                break
        else :
            if heap[left] >= heap[right] and heap[i] < heap[left] :
                heap[left], heap[i] = heap[i], heap[left]
                i = left
            elif heap[right] >= heap[left] and heap[i] < heap[right] :
                heap[right], heap[i] = heap[i], heap[right]
                i = right
            else :
                break
    return mx

for _ in range(N) :
    n = int(input())
    if n == 0 :
        print(pop())
    else :
        add(n)

