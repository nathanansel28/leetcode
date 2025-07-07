class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x) if x >=0 else str(x)[1:]
        x_str_reversed = x_str[::-1]
        x_str_reversed_int = int(x_str_reversed)
        if (x_str_reversed_int < -2**31) or (x_str_reversed_int > 2**31 - 1):
            return 0
        return x_str_reversed_int if x >= 0 else -x_str_reversed_int
