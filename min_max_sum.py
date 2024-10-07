def min_max_sum(arr):
    arr.sort()
    min_sum = sum(arr[:4])
    max_sum = sum(arr[1:])
    return min_sum, max_sum

if __name__ == "__main__":
    input_array = [1, 3, 5, 7, 9]
    min_value, max_value = min_max_sum(input_array)
    print(min_value, max_value)  # Output: 16 24
