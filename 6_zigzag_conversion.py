class Solution:
    def convert(self, s: str, numRows: int) -> str:

        grandlist = [[] for _ in range(numRows)]

        overall_count = 0
        vertical_count = 0
        vertical = True
        diagonal_count = 0
        while overall_count < len(s):
            if vertical:
                if vertical_count < numRows:
                    grandlist[vertical_count % numRows].append(s[overall_count])
                    vertical_count += 1
                    overall_count += 1

                else: 
                    vertical = False
                    diagonal_count = 0

            else: 
                if diagonal_count < numRows - 2:
                    grandlist[(numRows - 2) - diagonal_count].append(s[overall_count])
                    diagonal_count += 1 
                    overall_count += 1
                else: 
                    vertical = True
                    vertical_count = 0

        output = ""
        for _list in grandlist: 
            for item in _list: 
                output += item

        return output
    

class Solution:
    def convert(self, s: str, numRows: int) -> str:

        grandlist = ["" for _ in range(numRows)]

        overall_count = 0
        vertical_count = 0
        vertical = True
        diagonal_count = 0
        while overall_count < len(s):
            if vertical:
                if vertical_count < numRows:
                    grandlist[vertical_count % numRows] += s[overall_count]
                    vertical_count += 1
                    overall_count += 1

                else: 
                    vertical = False
                    diagonal_count = 0

            else: 
                if diagonal_count < numRows - 2:
                    grandlist[(numRows - 2) - diagonal_count] += s[overall_count]
                    diagonal_count += 1 
                    overall_count += 1
                else: 
                    vertical = True
                    vertical_count = 0

        output = ""
        for _string in grandlist: 
            output += _string

        return output
    

assert Solution().convert("PAYPALISHIRING", numRows=5) == 'PHASIYIRPLIGAN'
assert Solution().convert("PAYPALISHIRING", numRows=4) == 'PINALSIGYAHRPI'
assert Solution().convert("PAYPALISHIRING", numRows=3) == 'PAHNAPLSIIGYIR'
assert Solution().convert("ABCDEFGHIJK", numRows=2) == 'ACEGIKBDFHJ'

assert Solution().convert("a", numRows=5) == 'a'
assert Solution().convert("a", numRows=4) == 'a'
assert Solution().convert("a", numRows=3) == 'a'
assert Solution().convert("a", numRows=2) == 'a'
assert Solution().convert("a", numRows=1) == 'a'

print("Test cases passed successfully.")

