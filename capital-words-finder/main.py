text = input()

words = text.split()

results = []

for i, word in enumerate(words, start=1):

    # حذف نقطه و ویرگول از آخر کلمه
    clean_word = word.strip(".,")

    # شرط: عدد نباشد
    if clean_word.isdigit():
        continue

    # شرط: کلمه اول جمله نباشد
    if i == 1:
        continue

    # شرط: حرف اول بزرگ باشد
    if clean_word[0].isupper():
        results.append(f"{i}:{clean_word}")

if results:
    for r in results:
        print(r)
else:
    print("None")