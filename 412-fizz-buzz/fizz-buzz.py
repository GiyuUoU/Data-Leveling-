class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        
        # Standard 1-based indexing for the loop
        for i in range(1, n + 1):
            # Check most restrictive condition first (3 AND 5)
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                # The problem requires the number as a string
                answer.append(str(i))
                
        return answer
        