def bubble_sort(array):
    n = len(array)
    
    for i in range(n):        
        already_sorted = True
          
# a flag to stop the function if sorting is finished 
# при прохождении цикла ниже в случае обмена -  значение флага True меняется на False, 
# следовательно если он войдет в цикл но не будет обмена - значение True будет прежним
# и условие if already sorted будет удовлетворено, Break 
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                        
                array[j], array[j + 1] = array[j + 1], array[j]
                
                already_sorted = False # 'false' to avoid premature finish

        if already_sorted:  #if no swaps during last iteration  - array is sorted
            break
    return array



nums = [45,2,4,7,8,1,2,3]
print(bubble_sort(nums))
