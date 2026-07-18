class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        left = 0
        top = 0
        right = len(matrix[0])
        bottom = len(matrix)

        ans = []

        while top < bottom and left < right:
            # Getting the full first row
            for i in range(left, right):
                ans.append(matrix[top][i])
            top += 1

            # Printing the last column
            for i in range(top, bottom):
                ans.append(matrix[i][right - 1])
            right -= 1

            # Priting the last row
            if not (top < bottom and left < right):
                break

            for i in range(right - 1, left - 1, -1):
                ans.append(matrix[bottom - 1][i])
            bottom -= 1

            for i in range(bottom - 1, top - 1, -1):
                ans.append(matrix[i][left])
            left += 1

        return ans
