class Solution:
    """First Draft"""
    def longestPalindrome(self, s: str) -> str:
        def is_a_palindrome(mystring): 
            left, right = 0, len(mystring) - 1
            while left < right: 
                if mystring[left] != mystring[right]: 
                    return False
                else: 
                    left += 1 
                    right -= 1
            return True

        best_option = ""
        for i in range(len(s)):
            print(f"i={i}")
            if len(best_option) > (len(s) - i): 
                print("breaking")
                break

            for j in range(len(s), 0, -1):
                print(f"j={j}")
                candidate = s[i:j]
                if is_a_palindrome(candidate) and len(candidate) > 0:
                    if len(candidate) > len(best_option):
                        best_option = candidate
                        # print(f"Replacing best option with {candidate}")
        
        if best_option == "": 
            best_option = s[0]

        return best_option


class Solution:
    """Improved Version"""
    def longestPalindrome(self, s: str) -> str:
        def is_a_palindrome(mystring): 
            left, right = 0, len(mystring) - 1
            while left < right: 
                if mystring[left] != mystring[right]: 
                    return False
                else: 
                    left += 1 
                    right -= 1
            return True

        best_option = ""
        for length in range(len(s), 0, -1):
            for start in range(len(s) - length + 1): 
                candidate = s[start:start+length]
                # print(length, start, candidate)
                if is_a_palindrome(candidate): 
                    return candidate

test_cases = [
    ("abcdef", ['a', 'b', 'c', 'd', 'e', 'f']), 
    ("abababa", ['abababa']), 
    ("asdfasdfasdfasdf", ['a', 's', 'd', 'f']), 
    ("abccba", ['abccba']), 
    ("babad", ['bab', 'aba'])
]

solution = Solution()
for case in test_cases: 
    assert solution.longestPalindrome(case[0]) in case[1]

print("Test cases passed successfully.")
