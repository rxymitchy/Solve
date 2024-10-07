def diagonal_difference(matrix):
    n = len(matrix)
    left_to_right = sum(matrix[i][i] for i in range(n))
    right_to_left = sum(matrix[i][n - 1 - i] for i in range(n))
    return abs(left_to_right - right_to_left)

if __name__ == "__main__":
    input_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [9, 8, 9]
    ]
    result = diagonal_difference(input_matrix)
    print(result)  # Output: 2
