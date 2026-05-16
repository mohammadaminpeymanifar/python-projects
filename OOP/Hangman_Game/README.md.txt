# Hangman Game (OOP)

A simple Hangman game developed with Python using Object-Oriented Programming concepts.

## Features
- Random word selection
- OOP structure
- Multiple attempts system
- User-friendly terminal gameplay

## Concepts Used
- Classes and Objects
- Inheritance
- Encapsulation
- Methods
- Loops and Conditions

## Run Project

```bash
python hangman.py

برنامه Hangman یا «مرد دارزن» یک بازی حدس کلمه است.
کامپیوتر یک کلمه مخفی انتخاب می‌کند و بازیکن باید با حدس‌زدن حروف، آن کلمه را پیدا کند.

روند بازی

فرض کن کلمه مخفی این باشد:

+python

در ابتدا فقط جای خالی‌ها نمایش داده می‌شود:

+ _ _ _ _ _ _

اگر کاربر حرف p را وارد کند:

+ p _ _ _ _ _

اگر حرف اشتباه وارد کند، تعداد فرصت‌ها کم می‌شود.

مثلاً:

Remaining attempts: 5

اگر قبل از تمام شدن فرصت‌ها همه حروف را پیدا کند، برنده می‌شود؛ وگرنه بازی تمام می‌شود.