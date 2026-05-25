# World Cup Group B Standings

A Python program that simulates Group B matches of the World Cup and calculates team rankings based on match results.

---

## Teams

- Iran
- Spain
- Portugal
- Morocco

---

## Rules

- Win = 3 points
- Draw = 1 point
- Lose = 0 points

Goal difference = goals scored - goals conceded

---

## Sorting Rules

Teams are ranked by:

1. Points (descending)
2. Wins (descending)
3. Alphabetical order

---

## Input Format

6 lines of match results in format:

```
x-y
```

Where:
- x = goals of left team
- y = goals of right team

---

## Example Input

```
2-2
2-1
1-2
2-2
3-1
2-1
```

---

## Example Output

```
Spain  wins:1 , loses:0 , draws:2 , goal difference:2 , points:5
Iran  wins:1 , loses:1 , draws:1 , goal difference:0 , points:4
Portugal  wins:1 , loses:1 , draws:1 , goal difference:0 , points:4
Morocco  wins:1 , loses:2 , draws:0 , goal difference:-2 , points:3
```

---

## How to Run

```bash
python main.py
```
-------------------------------------------------------------------------------------
در گروه ب مسابقات جام‌جهانی تیم‌های ایران، پرتغال، اسپانیا و مراکش حضور دارند.
 این برنامه‌ با دریافت نتایج بازی‌ها، نام تیم و تعداد برد و باخت و تفاضل گل و امتیاز
 آن‌ها را به ترتیب در یک خط چاپ میکند.
 هر تیم به ترتیب امتیاز در یک خط چاپ میشود.
 (در صورتی که امتیاز برابر بود، تعداد برد مدنظر قرار میگیرد. در صورتی که هم تعداد برد و هم امتیاز برابر بود، بر اساس ترتیب حروف الفبا چاپ میشوند.)

نکته: تیم در صورت باخت صفر امتیاز، در صورت تساوی یک امتیاز و در صورت برد سه امتیاز کسب می کند.
تفاضل گل تفاوت گل های زده و گل های خورده یک تیم است

نتایج بازی‌ها را به ترتیب زیر میخواند: (در ورودی نمونه عدد سمت چپ مربوط به تیم سمت راست می‌باشد.)
ایران – اسپانیا
ایران – پرتغال
ایران – مراکش
اسپانیا – پرتغال
اسپانیا – مراکش
پرتغال - مراکش


ورودی نمونه:

2-2
2-1
1-2
2-2
3-1
2-1
خروجی نمونه:

Spain  wins:1 , loses:0 , draws:2 , goal difference:2 , points:5
Iran  wins:1 , loses:1 , draws:1 , goal difference:0 , points:4
Portugal  wins:1 , loses:1 , draws:1 , goal difference:0 , points:4
Morocco  wins:1 , loses:2 , draws:0 , goal difference:-2 , points:3

