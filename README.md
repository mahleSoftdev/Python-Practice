# Python Practice — First Steps

A small collection of scripts I wrote to teach myself Python during school recess. I'm a second-year Software Development student (IIE Rosebank College) with a background in Java and C#, and wanted to see how the fundamentals carry over to a new language.

## Scripts

### `PasswordHintTool.py`
Prompts the user for a password (input is masked using `maskpass`) and validates that it's between 8 and 12 characters. Once valid, it generates a simple hint using the first and last characters of the password.

**Concepts practiced:** input validation loops, string indexing, masked input.

### `string_formatter.py`
Takes a first name, last name, and short bio, then generates a username and a title-cased full name.

**Concepts practiced:** f-strings, string methods, `.title()` formatting.

### `String_manipulation.py`
A practice file covering string indexing and slicing, plus a small email-generator exercise that builds a company email address from a user's name.

**Concepts practiced:** indexing, slicing, `.upper()` / `.lower()` / `.strip()`, `len()`.

## Setup
```bash
pip install maskpass
python PasswordHintTool.py
```

## What's next
- Add input validation/error handling across all scripts
- Explore functions and modules to reduce repetition between scripts

---
*Part of my ongoing Python learning journey: connect with me on LinkedIn(www.linkedin.com/in/asemahle-myeni-075870352).*
