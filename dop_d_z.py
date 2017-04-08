sym = "aaababac"
new_sym = sym.replace(sym[0], sym[-1])

print(new_sym[:-1] + sym[0])

#  или же можно результат записать в переменную и вывести ее
#  res = new_sym[:-1] + sym[0]
#  print(res)

s = "In HTML <i>italic</i> words are embraced with 'i' tag. This is a <i>test</i> example."
tag_open = "<i>"
tag_close = "</i>"

tag_start_idx = s.find(tag_open)
tag_finish_idx = s.find(tag_close)

tag_start_idx2 = s.rfind(tag_open)
tag_finish_idx2 = s.rfind(tag_close)

word_start_idx = tag_start_idx + len(tag_open)
word_start_idx2 = tag_start_idx2 + len(tag_open)

word1 = s[word_start_idx:tag_finish_idx]
word2 = s[word_start_idx2:tag_finish_idx2]

print(word1)
print(word2)
