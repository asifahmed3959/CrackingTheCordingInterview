import unittest


def string_rotation_using_lps(s2):
    m = len(s2)
    lps = [0] * m
    j = 0

    for i in range(1, m):
        while j > 0 and s2[i] != s2[j]:
            j = lps[j-1]

        if s2[i] == s2[j]:
            j += 1
            lps[i] = j

    return lps


def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    lps = string_rotation_using_lps(pattern)

    i = j = 0  # Pointers for text and pattern
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == m:
                return True  # Pattern found


        else:
            if j > 0:
                j = lps[j - 1]  # Use LPS array to skip comparisons
            else:
                i += 1

    return False


def string_rotation(s1, s2):
    # complexity O(n^2)
    if len(s1) != len(s2):
        return False

    i = 0

    for i in range(len(s1)):
        if s1[i] == s2[0]:
            remaining = len(s1) - i
            if s1[i:] == s2[:remaining] and s1[:i] == s2[remaining:]:
                return True

    return False


def string_rotation_order_time_complexity_two(s1, s2):
    #o(n) based on knuth-morris-pratt algorithm
    if len(s1) != len(s2):
        return False

    checker = s1 * 2

    return s2 in (s1 + s1)



class Test(unittest.TestCase):
    test_cases = [
        ("waterbottle", "erbottlewat", True),
        ("foo", "bar", False),
        ("foo", "foofoo", False),
    ]


    def test_string_rotation(self):
        for [s1, s2, expected] in self.test_cases:
            actual = string_rotation(s1,s2)
            print(actual, expected)
            assert actual == expected


    def test_string_rotation_using_knuth(self):
        for [s1, s2, expected] in self.test_cases:
            actual = string_rotation_order_time_complexity_two(s1,s2)
            print(actual, expected)
            assert actual == expected

    def test_string_rotation_using_km_search(self):
        for [s1, s2, expected] in self.test_cases:
            actual = kmp_search(s1,s2)
            print(actual, expected)
            assert actual == expected



if __name__ == "__main__":
    unittest.main()