"""
## Group Anagrams

Given a list of lowercase English strings, group together all strings that are anagrams of each other.

Two strings are anagrams if they contain the same characters with the same frequencies, but possibly in a different order.

### Example

```python
words = [
    "eat", "tea", "tan", "ate", "nat", "bat",
    "listen", "silent", "enlist",
    "abc", "cab", "bac",
    "a", "aa"
]
```

A valid output is:

```python
[
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"],
    ["listen", "silent", "enlist"],
    ["abc", "cab", "bac"],
    ["a"],
    ["aa"]
]
```

The order of the groups and the order of strings within each group do not matter.

Implement:

```python
def group_anagrams(words):
    pass
```

### Constraints

```text
1 <= len(words) <= 10^4
0 <= len(words[i]) <= 100
words[i] contains only lowercase English letters.
```

Also state the time and space complexity of your solution.

"""
def group_anagrams(words):
    groups = {}

    for word in words:
        counts = [0] * 26

        for ch in word:
            index = ord(ch) - ord('a')
            counts[index] += 1

        key = tuple(counts)

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return list(groups.values())


words = [
    "eat", "tea", "tan", "ate", "nat", "bat",
    "listen", "silent", "enlist",
    "abc", "cab", "bac",
    "a", "aa"
]

result = group_anagrams(words)

for group in result:
    print(group)
