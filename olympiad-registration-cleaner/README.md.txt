# Olympiad Registration Cleaner

A Python program that cleans and standardizes participant data for the Computer Olympiad final list.

---

## Problem Description

Participants' data is not standardized:
- Gender is provided first (`m` or `f`)
- Name format is inconsistent (mixed uppercase/lowercase)
- Programming language is provided at the end

The program must:
- Standardize names
- Separate participants by gender
- Sort names alphabetically inside each group
- Print females first, then males

---

## Input Format

```
n
gender.name.language
```

Example:
```
4
m.hosSein.python
f.miNa.C
m.aHMad.C++
f.Sara.java
```

---

## Output Format

```
f Mina C
f Sara java
m Ahmad C++
m Hossein python
```

---

## Rules

- Name must be converted to proper case (First letter uppercase, rest lowercase)
- Output order:
  1. Female (f)
  2. Male (m)
- Each group sorted alphabetically by name

---

## How to Run

```bash
python main.py
```
---------------------------------------------------------------------------------------
این برنامه‌ تعداد ،اسم، جنسیت و زبان قبول شدگان را از ورودی میخواند. 
سپس بر اساس جنسیت اسامی را تفکیک، استاندارد سازی و جلوی هر اسم زبانی که فرد با آن در مسابقات شرکت کرده است را میبنویسد. 
(در خروجی در ابتدا جنسیت زن و سپس جنسیت مرد چاپ میشود. اسامی در هر جنسیت به ترتیب الفبای انگلیسی چاپ میشوند.)


ورودی نمونه:

4
m.hosSein.python
f.miNa.C
m.aHMad.C++
f.Sara.java
خروجی نمونه:

f Mina C
f Sara java
m Ahmad C++
m Hossein python