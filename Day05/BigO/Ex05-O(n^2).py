'''
파일명 : Ex05-O(n^2).py

- O(n^2): 제곱 시간 복잡도, 중첩 반복문을 사용하는 알고리즘
'''

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr