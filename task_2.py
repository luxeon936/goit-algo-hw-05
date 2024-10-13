def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None
    
    while left <= right:
        iterations += 1
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return (iterations, arr[mid])
        
        elif arr[mid] < target:
            left = mid + 1  
        else:
            upper_bound = arr[mid]  
            right = mid - 1  

    # Якщо елемент не знайдений, повертаємо кількість ітерацій і верхню межу
    return (iterations, upper_bound)

sorted_array = [1.1, 2.2, 3.3, 4.4, 5.5, 7.7, 9.9, 11.11]

# Шукаємо елемент, який є в масиві
result1 = binary_search(sorted_array, 4.4)
print(result1)

# Шукаємо елемент, який відсутній в масиві
result2 = binary_search(sorted_array, 6.0)
print(result2)