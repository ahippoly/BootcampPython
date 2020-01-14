phrase = "The right format"

res = ""
ph_len = len(phrase)

for i in range(42 - ph_len - 1) :
    res += "-"
res += phrase
print(res)
