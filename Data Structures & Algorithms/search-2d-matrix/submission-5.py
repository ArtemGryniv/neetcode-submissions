class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_arr = 0
        right_arr = len(matrix) - 1
        mid = 0
        while left_arr <= right_arr:
            mid = (left_arr + right_arr) // 2

            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                break
            elif target < matrix[mid][0]:
                right_arr = mid - 1
            else:
                left_arr = mid + 1
        else:
            return False

        left = 0
        arr = matrix[mid]
        right = len(arr) - 1
        while left <= right:
            middle = (left + right) // 2

            if target == arr[middle]:
                return True
            elif target < arr[middle]:
                right = middle - 1
            else:
                left = middle + 1
        
        return False