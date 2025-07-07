from tools.my_logger import load_logger
from tools.tester import run_test_cases
DEBUG=True
logger=load_logger(DEBUG=DEBUG)

class Solution: 
    """Decent solution using translation and counting."""
    def __init__(self):
        self.translation = {
            'IV': 'I' * 4, 'V': 'I' * 5, 'IX': 'I' * 9,  
            'XL': 'X' * 4, 'L': 'X' * 5, 'XC': 'X' * 9, 
            'CD': 'C' * 4, 'D': 'C' * 5, 'CM': 'C' * 9, 
        }
        self.roman_dictionary = {
            'I': 1, 
            'V': 5, 
            'X': 10, 
            'L': 50, 
            'C': 100, 
            'D': 500, 
            'M': 1000
        }


    def unpack_roman(self, s: str) -> str:
        for key, item in self.translation.items():
            s = s.replace(key, item)
        return s


    def romanToInt(self, s: str) -> int:
        integer = 0
        roman_unpacked = self.unpack_roman(s)
        logger.debug(f"romanToInt -> roman_unpacked: {roman_unpacked}")
        counts = self.count_each_roman(roman_unpacked)
        for char in set(roman_unpacked): 
            count = counts[char]
            integer += self.roman_dictionary[char] * count
            logger.debug(f"count: {count}, integer: {integer}")

        return integer        


    def count_each_roman(self, roman_unpacked: str) -> dict[str, int]: 
        count = {'I': 0, 'V': 0, 'X': 0, 'L': 0, 'C': 0, 'D': 0, 'M': 0}
        for char in set(roman_unpacked):
            count[char] = roman_unpacked.count(char)
            logger.debug(f"count_each_roman -> count: {count}, char: {char}")
        return count 


test_cases = [
    ('I', 1), 
    ('II', 2), 
    ('III', 3), 
    ('IV', 4), 
    ('V', 5), 
    ('VI', 6), 
    ('VII', 7), 
    ('VIII', 8), 
    ('IX', 9), 
    ('X', 10), 
    ('XI', 11), 
    ('XII', 12), 
    ('XIII', 13), 
    ('XIV', 14), 
    ('XV', 15), 
    ('MMMDCCXLIX', 3749), 
    ('LVIII', 58), 
    ('MCMXCIV', 1994), 
    ('MMDLXV', 2565), 
    ('MMLXIX', 2069), 
    ('XXII', 22), 
    ('MMDLXXXIII', 2583), 
    ('DXXXIX', 539), 
    ('MLIV', 1054), 
    ('MMDXCIII', 2593), 
    ('MDLXXI', 1571), 
    ('MMMCIX', 3109), 
    ('MLXIV', 1064), 
    ('MMXCI', 2091), 
    ('XLV', 45), 
    ('MMXCIV', 2094), 
    ('MMXCVI', 2096), 
    ('MMMCXXIII', 3123), 
    ('MMDCXIV', 2614), 
    ('MMMDCXL', 3640), 
    ('MDCIV', 1604), 
    ('MMMDCLXVI', 3666), 
    ('MMMCLVIII', 3158), 
    ('MMDCLXV', 2665), 
    ('MMMDCXCIII', 3693), 
    ('MMMDCCXI', 3711), 
    ('MDCLXXIII', 1673), 
    ('DCLII', 652), 
    ('DCLVI', 656), 
    ('CXLVIII', 148), 
    ('MMDCCX', 2710), 
    ('MMMCCXXVII', 3227), 
    ('CLX', 160), 
    ('CLXII', 162), 
    ('MDCXCIX', 1699), 
    ('MMDCCXXVIII', 2728), 
    ('MMDCCXXXI', 2731), 
    ('MMMCCXLIX', 3249), 
    ('MMMDCCLXVI', 3766), 
    ('MDCCXVIII', 1718), 
    ('MMMCCLVII', 3257), 
    ('MMDCCXLV', 2745), 
    ('MMMCCLXIII', 3263), 
    ('MMMDCCLXXX', 3780), 
    ('MMMCCLXIX', 3269), 
    ('MMDCCLXIII', 2763), 
    ('DCCXIX', 719), 
    ('CCVIII', 208), 
    ('DCCXXIII', 723), 
    ('MMMCCLXXXVII', 3287), 
    ('MMMDCCCII', 3802), 
    ('DCCXXXIV', 734), 
    ('DCCXLII', 742), 
    ('MCCLIX', 1259), 
    ('DCCXLIX', 749), 
    ('MMCCLXXXV', 2285), 
    ('DCCLXVI', 766), 
    ('MMDCCCXIV', 2814), 
    ('MMCCCXIII', 2313), 
    ('MMDCCCXXX', 2830), 
    ('MMMCCCLI', 3351), 
    ('MCCCIII', 1303), 
    ('MMDCCCLIX', 2859), 
    ('CCCII', 302), 
    ('MMCCCLIV', 2354), 
    ('MMCCCLXIII', 2363), 
    ('MMCCCLXXIII', 2373), 
    ('CCCXXVIII', 328), 
    ('MDCCCLXIV', 1864), 
    ('MCCCLXI', 1361), 
    ('MDCCCLXXV', 1875), 
    ('MCCCLXVI', 1366), 
    ('MMCCCXCVI', 2396), 
    ('MMMCMXXXV', 3935), 
    ('MDCCCLXXXIX', 1889), 
    ('MCCCLXXXVI', 1386), 
    ('DCCCLXXIV', 874), 
    ('MMMCDXXXVII', 3437), 
    ('MMMCMLIX', 3959), 
    ('MCDV', 1405), 
    ('DCCCXCIII', 893), 
    ('MMCMXLVI', 2946), 
    ('MMMCDLX', 3460), 
    ('MCDXVIII', 1418), 
    ('MMCMLV', 2955), 
    ('CDIII', 403), 
    ('MMCMLXXI', 2971), 
    ('MMMCDLXXXV', 3485), 
    ('MCDXLI', 1441), 
    ('MMMCDXCII', 3492), 
    ('CDXXIV', 424), 
    ('MCDLIII', 1453), 
    ('MMMDXXIX', 3529), 
    ('MMII', 2002), 
    ('CMLXXIX', 979), 
    ('CMLXXXI', 981), 
    ('MCDXCVI', 1496), 
    ('MMIX', 2009), 
    ('MMMXL', 3040), 
    ('MMMXLIV', 3044), 
    ('MDXXXII', 1532), 
    ('MMMDLXXXII', 3582), 

]

run_test_cases(Solution().romanToInt, test_cases)