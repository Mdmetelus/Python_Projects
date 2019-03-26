def second_pass_anagrams(words):

anagrams = {}

longest = None

for word in words:
    signature = "".join(sorted(word.lower()))
    # .count(word)
    if signature not in anagrams:
        anagrams[signature] =[]
    anagrams[signature].append(word)

    if longest == None or len(anagrams[signature]) > len(anagrams[longest]):
        longest = signature

print(anagrams[longest])