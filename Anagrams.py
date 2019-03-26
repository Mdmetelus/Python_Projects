def first_pass_anagrams(words):
    import random
    import operator

chars = [0] * 26
for i in range(26)
    chars[i] = random.randint(0,1000000)

anagrams = {}
signature = 0

for word in words:
    word = word.lower()
    for char in word:
        index = ord(char) - 97
        if index >= 0 and index < 26:
            signature += chars[index]

    if signature not in anagram:
        anagram[signature] = []
    anagram[signature].append(word)
    signature = 0

# whats a clean way to go through the dictionary in python
maxAnagrams = max(anagrams.items(), key=operator.intemgetter(1))[0]