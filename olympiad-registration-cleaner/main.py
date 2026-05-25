n = int(input())

female = []
male = []

for _ in range(n):
    data = input().split(".")

    gender = data[0]
    name = data[1]
    language = data[2]

    # استانداردسازی اسم (First letter capital + rest lowercase)
    name = name.capitalize()

    item = (name, language)

    if gender == "f":
        female.append(item)
    else:
        male.append(item)

# مرتب‌سازی الفبایی بر اساس اسم
female.sort(key=lambda x: x[0])
male.sort(key=lambda x: x[0])

# چاپ خروجی
for name, lang in female:
    print(f"f {name} {lang}")

for name, lang in male:
    print(f"m {name} {lang}")