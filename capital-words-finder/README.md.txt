# Capital Words Finder

A Python program that extracts **significant words** from a text.

---

## Definition of Significant Words

A word is considered significant if:

- It starts with a capital letter
- It is NOT the first word of a sentence
- It is NOT a number
- Punctuation (.,) is ignored

---

## Input

A single line of text.

Example:
```
The Persian League is the largest sport event dedicated to the deprived areas of Iran. The Persian League promotes peace and friendship. This video was captured by one of our heroes who wishes peace.
```

---

## Output

Format:
```
index:word
```

Example:
```
2:Persian
3:League
15:Iran
17:Persian
18:League
```

---

## Rules

- Word indexing starts from 1
- First word of sentence is ignored
- Only "." and "," may appear and must be removed
- Numbers are ignored
- If no valid word exists → print `None`

---

## Run Project

```bash
python main.py
```
------------------------------------------------------------------------------------------------------
این برنامه‌ از یک متن کلمات شاخص (کلماتی که با حروف بزرگ شروع می‌شوند) را به همراه شماره کلمه (چندمین کلمه می‌باشد) را در خروجی چاپ میکند. 
در صورتی که در متن، کلمه‌ای با این ویژگی یافت نشد، در خروجی 
None 
چاپ میکند.

کلماتی که در ابتدای جمله می‌باشند به عنوان کلمه شاخص در نظر نمیگیرد. (شماره کلمات را از یک شروع کنید)
اعداد جز کلمات شاخص حساب نمی‌شوند.
تنها نشانه مورد استفاده در جمله به جز نقطه، ویرگول می‌باشد. (در صورتی که نقطه یا ویرگول در آخر کلمه بود، حذف میشود)
 

ورودی نمونه:

The Persian League is the largest sport event dedicated to the deprived areas of Iran. The Persian League promotes peace and friendship. This video was captured by one of our heroes who wishes peace.
خروجی نمونه:

2:Persian
3:League
15:Iran
17:Persian
18:League