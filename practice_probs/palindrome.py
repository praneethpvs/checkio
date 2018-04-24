import pytest
import re


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = re.sub(r'\W+', '', s)
        new_s = s[::-1]
        if new_s == s:
            return True

        return False


@pytest.mark.parametrize("input, expected", [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    # TODO - More test cases
])
def test_isPalindrome(input, expected):
    assert Solution().isPalindrome(input) == expected
