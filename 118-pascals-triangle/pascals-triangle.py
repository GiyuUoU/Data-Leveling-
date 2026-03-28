class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        
        for i in range(1, numRows):
            prev = triangle[i-1]
            row = [1] + [prev[j-1] + prev[j] for j in range(1, i)] + [1]
            triangle.append(row)
        
        return triangle
