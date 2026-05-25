# Movie Genre Survey

A Python program that collects users' favorite movie genres and calculates popularity of each genre.

---

## Genres

- Horror
- Romance
- Comedy
- History
- Adventure
- Action

---

## Input Format

First line:
```
number of people
```

Next lines:
```
name genre1 genre2 genre3
```

Each person selects 3 genres.

---

## Example Input

```
4
hossein Horror Romance Comedy
mohsen Horror Action Comedy
mina Adventure Action History
sajjad Romance History Action
```
---

## Example Output
```
Action : 3
Comedy : 2
History : 2
Horror : 2
Romance : 2
Adventure : 1
```
---
## Rules

- Each selected genre increases its count by 1
- If a genre is not selected, its value is 0
- Sorting:
  1. Higher count first
  2. Alphabetical order if equal
---
## Run Project

```bash
python main.py
```
-----------------------------------------------------------------------
در یک نظرسنجی از افراد علاقه‌­مند به تماشای فیلم، درخواست شد تا 3 تا از ژانرهای مورد علاقه‌­ی خود را بنویسند. 6 ژانر مختلف برای انتخاب به آن­‌ها داده شده است که شامل:

Horror, Romance, Comedy, History , Adventure , Action

‎این برنامه تعداد افراد را میگیرد سپس اسم هر فرد را با ژانرهای مورد علاقش سپس اسم هر ژانر و تعداد افراد علاقه‌مند به آن ژانر را به ترتیب از بیشترین علاقه‌مندی در خروجی چاپ میکند 
(در صورتی که میزان علاقه‌مندی در ژانرهای مختلف یکسان شد، به ترتیب الفبای انگلیسی در خروجی چاپ میکند) 
در صورتی که ژانری انتخاب نشد، مقدار آن را صفر در نظر میگیرد و در خروجی اسم و عدد 0 را چاپ میکند.

4
hossein Horror Romance Comedy
mohsen Horror Action Comedy
mina Adventure Action History
sajjad Romance History Action
نمونه خروجی:

Action : 3
Comedy : 2
History : 2
Horror : 2
Romance : 2
Adventure : 1