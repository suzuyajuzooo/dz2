def print_average(arr):
   
    if not arr:
        return 0
    return sum(arr) / len(arr)

def find_median(arr):

    if not arr:
        return 0
    
    sorted_arr = sorted(arr) 
    n = len(sorted_arr)
    
    
    if n % 2 == 1:
        return sorted_arr[n // 2]
  
    else:
        mid1 = sorted_arr[n // 2 - 1]
        mid2 = sorted_arr[n // 2]
        return (mid1 + mid2) / 2

def print_statistics(arr):
    
    if not arr:
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        return
  
    print(len(arr))
  
    avg = print_average(arr)
    print(avg)
   
    print(min(arr))
    
    print(max(arr))
    
    median = find_median(arr)
    print(median)