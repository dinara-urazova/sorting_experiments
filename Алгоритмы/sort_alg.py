
def insert_sort(A):
    """сортировка списка A вставками"""
    N = len(A)
    for top in range(1,N):
        k = top
        while k>0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k-=1

def choice_sort(A):
    """сортировка списка A выбором"""
    pass

def bubble_sort(A):
    """сортировка списка A пузырьком"""
    pass

def test_sort(sort_algorithm):  #тестируемая функция в качестве параметра
    print("Тестируем: ", sort_algorithm.__doc__)
    print("testcase #1: ", end = "")
    A = [4,2,5,1,3]
    A_sorted = [1,2,3,4,5]
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")

if __name__  == "__main__":   
    #условие if __name__ == '__main__' проверяет, был ли файл запущен напрямую.
    test_sort(insert_sort)
    test_sort(choice_sort)
    test_sort(bubble_sort)
    
    

        