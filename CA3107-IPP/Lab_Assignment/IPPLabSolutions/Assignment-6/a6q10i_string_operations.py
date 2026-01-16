s = "Satya"
freq = {}
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
max_char = None
max_count = 0
for ch in freq:
    if freq[ch] > max_count:
        max_count = freq[ch]
        max_char = ch
print("Character with max frequency:", max_char, "(", max_count, ")")
