"""
## Valid Anagram Pair

Given two lowercase English strings `s` and `t`, determine whether they are anagrams of each other.

Two strings are anagrams if they contain exactly the same characters with exactly the same frequencies, possibly in a different order.

### Examples

```python
s = "anagram"
t = "nagaram"
```

Output:

```python
True
```

```python
s = "rat"
t = "car"
```

Output:

```python
False
```

```python
s = "aacc"
t = "ccac"
```

Output:

```python
False
```

Implement:

```python
def is_anagram(s, t):
    pass
```

### Constraints

```text
1 <= len(s), len(t) <= 5 * 10^4
s and t contain only lowercase English letters.
```

Also state the time and space complexity of your solution.
"""

def is_anagram(s, t):
    if len(s) != len(t):
        return False

    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in t:
        if ch not in freq:
            return False

        freq[ch] -= 1

        if freq[ch] < 0:
            return False

    return True


print(is_anagram("anagram", "nagaram"))
print(is_anagram("rat", "car"))
print(is_anagram("aacc", "ccac"))
print(is_anagram("listen", "silent"))
print(is_anagram("a", "aa"))
