def divisible_sum_pairs(arr, k):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] + arr[j]) % k == 0:
                count += 1
    return count

if __name__ == "__main__":
    input_array = [1, 2, 3, 4, 5, 6]
    k = 5
    result = divisible_sum_pairs(input_array, k)
    print(result)  # Output: 3
