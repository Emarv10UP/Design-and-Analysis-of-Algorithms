# # -Copy the code for Recursive Fibonacci. Run 3 examples. Explain, visualize the recursive calls structure (what function calls what function)
# def fibonacci_recursive(n):
#     # Базовые случаи
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     # Рекурсивный вызов
#     return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# print("fibonacci(3) =", fibonacci_recursive(3))
# print("fibonacci(5) =", fibonacci_recursive(5))
# print("fibonacci(7) =", fibonacci_recursive(7))

# -Copy the code for Iterative implementation of Binary Seach. Run 3 examples. . Explain, visualize how the input changes with every iteration, how the progress is made for the target search
# def binary_search_iterative(arr, target):
#     left = 0
#     right = len(arr) - 1
#     iteration = 1

#     while left <= right:
#         mid = left + (right - left) // 2

#         print(
#             f"Итерация {iteration}: left={left}, right={right}, mid={mid}, arr[mid]={arr[mid]}")

#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1

#         iteration += 1

#     return -1


# arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# # Запуск 3 примеров
# print("--- Пример 1: Ищем 14 ---")
# binary_search_iterative(arr, 14)

# print("\n--- Пример 2: Ищем 2 ---")
# binary_search_iterative(arr, 2)

# print("\n--- Пример 3: Ищем 15 (элемента нет) ---")
# binary_search_iterative(arr, 15)

# -Write a Recursive implementation of Binary Search
def binary_search_recursive(arr, target, left, right):

    if left > right:
        return -1

    mid = left + (right - left) // 2

    if arr[mid] == target:
        return mid

    if arr[mid] < target:
        # Ищем в правой половине
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        # Ищем в левой половине
        return binary_search_recursive(arr, target, left, mid - 1)


arr = [10, 20, 30, 40, 50, 60]
target = 40
result = binary_search_recursive(arr, target, 0, len(arr) - 1)
print(f"Индекс искомого элемента ({target}): {result}")
