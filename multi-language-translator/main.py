n = int(input())

eng_to_main = {}
fre_to_main = {}
ger_to_main = {}

for _ in range(n):
    data = input().split()

    main_word = data[0]
    eng = data[1]
    fre = data[2]
    ger = data[3]

    eng_to_main[eng] = main_word
    fre_to_main[fre] = main_word
    ger_to_main[ger] = main_word

sentence = input().split()

result = []

for word in sentence:

    if word in eng_to_main:
        result.append(eng_to_main[word])
    elif word in fre_to_main:
        result.append(fre_to_main[word])
    elif word in ger_to_main:
        result.append(ger_to_main[word])
    else:
        result.append(word)

print(" ".join(result))