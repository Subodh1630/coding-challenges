def is_anagram(first: str, second: str) -> bool:
    return sorted(first) == sorted(second)


print(is_anagram("anagram", "nagaram"))  # True
print(is_anagram("rat", "car"))          # False
print(is_anagram("", ""))                # True
print(is_anagram("aacc", "ccac"))        # False
print(is_anagram("A", "a"))              # False
print(is_anagram("a!", "!a"))            # True