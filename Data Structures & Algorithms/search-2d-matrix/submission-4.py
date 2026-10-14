class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_arr = 0
        right_arr = len(matrix)
        mid = 0
        while left_arr <= right_arr:
            if len(matrix) <= 1:
                break
            mid = (left_arr + right_arr) // 2
            if mid >= len(matrix):
                return False
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                break
            elif target < matrix[mid][0]:
                right_arr = mid - 1
            else:
                left_arr = mid + 1

        left = 0
        arr = matrix[mid]
        right = len(arr)
        while left <= right:
            if len(arr) <= 1 and target == arr[0]:
                return True
            elif len(arr) <= 1:
                break

            middle = (left + right) // 2
            if middle >= len(arr):
                return False

            if target == arr[middle]:
                return True
            elif target < arr[middle]:
                right = middle - 1
            else:
                left = middle + 1
        
        return False