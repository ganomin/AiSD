def max_heapify(A, heapsize, i):
    while True:
        l = 2 * i + 1
        r = 2 * i + 2

        if l < heapsize and A[l] > A[i]:
            largest = l
        else:
            largest = i

        if r < heapsize and A[r] > A[largest]:
            largest = r

        if not i == largest:
            A[largest], A[i] = A[i], A[largest]
            i = largest
        else:
            break

    return A

def build_max_heap(A):
    heapsize = len(A)

    for i in range(heapsize // 2 - 1, -1, -1):
        max_heapify(A, heapsize, i)

    return A

def heap_sort(A):
    A = build_max_heap(A)
    heapsize = len(A)

    for i in range(heapsize - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapsize = heapsize - 1
        max_heapify(A, heapsize, 0)

    return A

if __name__ == '__main__':
    input_table = [28, 6, 11, 12, 17, 8, 7, 18, 12, 14]
    print("Przed sortowaniem:", input_table)
    print("Po sortowaniu:", heap_sort(input_table))