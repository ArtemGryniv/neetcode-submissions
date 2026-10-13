class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr = [0] * len(temperatures)
        stack = []

        i = 0
        while i < len(temperatures):
            if not stack:
                stack.append(i)
                i += 1
                continue
            else:
                while temperatures[i] > temperatures[stack[-1]]:
                    index = stack.pop()
                    arr[index] = i - index
                    if not stack:
                        break

            stack.append(i)    
            i += 1

        return arr
                

