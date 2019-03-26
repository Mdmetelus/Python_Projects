def third_pass_anagrams(words):

anagrams = {}

longest = None

for word in words:
    signature = "".join(sorted(word.lower()))
    # .count(word)
    if signature not in anagrams:
        anagrams[signature] =[]
    anagrams[signature].append(word)

maxLen = 0
maxAnagrams = []
for signature in anagrams:
    if len(anagrams[signature]) > maxLen
        maxLen = len(anagrams[signature])
        maxAnagrams = anagrams[signature]

    

print(maxAnagrams)

# for improvrmrnts look for:
#   -time complexity 
#   -space complexity
#   -readability
#   -comments
#   -redundency
#   -bugs
#   -cleanup