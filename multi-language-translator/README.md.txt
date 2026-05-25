# Multi Language Translator

A Python program that translates a sentence from English, French, or German into a base language using a dictionary.

---

## Problem Description

Each word in the dictionary has:
- A base word
- English translation
- French translation
- German translation

The program translates a sentence written in any of these languages back into the base language.

---

## Input Format

```
n
base english french german
sentence
```

---

## Example Input

```
4
man I je ich
kheili very très sehr
alaghemand interested intéressé interessiert 
barnamenevisi programming laprogrammation Programmierung
I am very interested in programming
```

---

## Output

```
man am kheili alaghemand in barnamenevisi
```

---

## Rules

- If a word exists in dictionary → replace it with base word
- If not found → keep original word
- Sentence may contain mixed languages
- No punctuation handling required

---

## Run Project

```bash
python main.py
```
---------------------------------------------------------------------------------------------
این پروژه یک مترجم ساده است که جمله‌ای را از زبان‌های انگلیسی، فرانسوی یا آلمانی به زبان اصلی 
(Base Language) 
ترجمه می‌کند.

---

## توضیح مسئله

در این پروژه یک دیکشنری داریم که هر کلمه شامل موارد زیر است:

- کلمه اصلی (زبان پایه)
- ترجمه انگلیسی
- ترجمه فرانسوی
- ترجمه آلمانی

برنامه باید یک جمله را دریافت کرده و هر کلمه را به زبان اصلی آن تبدیل کند.

اگر کلمه‌ای در دیکشنری وجود نداشت، همان کلمه بدون تغییر در خروجی قرار می‌گیرد.

---

## ورودی

### خط اول:
```
n
```
تعداد کلمات موجود در دیکشنری

### n خط بعد:
```
کلمه_اصلی انگلیسی فرانسوی آلمانی
```

### خط آخر:
جمله‌ای که باید ترجمه شود (ممکن است ترکیبی از چند زبان باشد)

---

## نمونه ورودی

```
4
man I je ich
kheili very très sehr
alaghemand interested intéressé interessiert 
barnamenevisi programming laprogrammation Programmierung
I am very interested in programming
```

---

## خروجی

```
man am kheili alaghemand in barnamenevisi
```

---

## قوانین

- اگر کلمه در دیکشنری وجود داشت → به کلمه اصلی تبدیل شود
- اگر وجود نداشت → همان کلمه چاپ شود
- جمله ممکن است ترکیبی از چند زبان باشد
- ترتیب کلمات در جمله باید حفظ شود
