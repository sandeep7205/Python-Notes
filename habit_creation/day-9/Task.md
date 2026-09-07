# 🚀 Day 9 — Dynamic Counting with Dictionaries

SKM, yesterday on Day 8 you took a big step: reading raw text files from disk and counting items.

But remember the problem we noticed at the end of Day 8?

To count 4 categories, you had to write:

```python
f_cnt = 0
t_cnt = 0
s_cnt = 0
e_cnt = 0
```

> **What happens if tomorrow your file contains 20 or 50 new categories?**

Are you going to create 50 separate variables and 50 `if/elif` statements?

Of course not.

Today we replace hardcoded counters with **dynamic dictionary counting**.

---

## 🎯 Today's goal

You have `expenses.txt` in your `day-9` folder with multiple expense categories:

```text
Food
Fuel
Travel
Food
Shopping
...
```

By the end of today, you will:
1. Build a reusable function that takes a list of items and dynamically counts frequencies.
2. Use dictionary keys to automatically track new categories as they appear.
3. Eliminate repetitive `if/elif` variable counter logic.
4. Print a clean, formatted category summary.

---

# ⏱️ Your 15-minute mission

### 🧠 0–3 min — Recall

Before touching code, answer these from memory:

1. What does `readlines()` return?
2. Why did we use `.strip()`?
3. What is a dictionary?
4. How do you access a dictionary value using a key?
5. How do you add a new key/value pair to a dictionary?
6. What does `.items()` give you?
7. What does `+= 1` do?

Keep your answers short.

---

# 🔨 3–5 min — The Dynamic Counting Pattern

Instead of hardcoding variable names, let the data dictate the dictionary keys:

```text
Read next category from file: "Food"
             │
   Is "Food" in dictionary?
           ┌─┴─┐
          NO   YES
          │     │
   Create key   Increment value
   dict["Food"] = 1   dict["Food"] += 1
```

At the end of the loop, you have a single dictionary with all category counts:

```python
{
    "Food": 4,
    "Fuel": 3,
    "Travel": 2,
    "Shopping": 1,
    ...
}
```

No matter how many new categories appear in the file, your code never needs to change!

---

# 🛠️ 5–12 min — Your challenge

You already have `expenses.txt` in your `day-9` folder.

### Challenge 1 — Create `count_function()`

1. Define a function (e.g. `def count_function(input_list):`).
2. Inside, initialize an empty dictionary: `count_dict = {}`.
3. Loop through `input_list`:
   - Remove whitespace and newlines using `.strip()`.
   - Check if the category is already a key in `count_dict`:
     - If **not**, add it with a starting count of `1`.
     - If **already present**, increment its count by 1 (`count_dict[category] += 1`).
4. Return `count_dict`.

### Challenge 2 — Read file and call your function

1. Open `expenses.txt` using `with open("habit_creation/day-9/expenses.txt", "r") as f:`.
2. Read all lines into a list using `f.readlines()`.
3. Check if the list contains records.
4. Pass the list to your `count_function()` and store the returned dictionary.

### Challenge 3 — Print a category summary

Using a `for` loop and `.items()` on your dictionary, print a clean summary:

```text
Category Summary
----------------
Food: 4
Fuel: 3
Travel: 2
Shopping: 1
Entertainment: 2
Medical: 3
Internet: 1
Rent: 1
Education: 1
Groceries: 1
```

---

# ⭐ Bonus — Data validation thinking

Think about edge cases:
- What if `expenses.txt` is completely empty? Does your code crash or handle it gracefully?
- How can you check if the list has records before attempting to process and display it?

---

# 🚫 Don't do this today

Don't jump into:
* `collections.Counter` from Python's standard library (we want to understand the dictionary mechanics manually first!)
* Writing output to a new file
* Complex error handling

Master the manual dynamic counting logic first.

---

## 📝 Your Day 9 report

When you're finished, send:

```text
Day 9:
Time:
Habit battle:
What I built:
What confused me:
What I learned:
```

And paste your code.

### Today's mindset:

> **Good code doesn't hardcode assumptions about the data. It lets the data define the structure.**

Let's go. 🔥
