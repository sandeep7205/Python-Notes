# 🚀 Day 7 — Week 1 Review & Functions

SKM, congratulations on reaching Day 7!

You have completed an entire week of daily, consistent progress.

Over the last 6 days, you've built:

```text
Day 1: Variables & Data Types
  ↓
Day 2: Conditions (if/else)
  ↓
Day 3: Loops (for)
  ↓
Day 4: Filtering & Membership (in, %)
  ↓
Day 5: Dictionaries (.items(), .update())
  ↓
Day 6: Structured Data Processing (list of dicts, sum())
```

Today is your **Week 1 Review & Integration Day**.

Instead of learning isolated syntax, we're bringing everything together. And we're introducing two foundational concepts in programming: **Functions** and **Tuples/Sets**.

---

## 🎯 Today's goal

By the end of today, you will:

1. Test your recall across all 10 core concepts learned in Week 1.
2. Understand how **functions** package logic for reuse (`def`, `return`).
3. Understand what **sets** and **tuples** are, and how sets effortlessly find unique values.
4. Build a complete expense reporting program that calculates totals using a function.
5. Display formatted results cleanly using f-strings.

---

# ⏱️ Your 15-minute mission

### 🧠 0–4 min — The 10-Question Week 1 Recall

Before writing code or looking back at previous notes, test your memory. Answer these 10 questions:

1. **Variables**: What is a variable?
2. **List**: What is a list?
3. **Dictionary**: What is a dictionary?
4. **`if`**: What does `if` do?
5. **`for`**: What does a `for` loop do?
6. **`in`**: What does `in` check?
7. **`%`**: What does `%` return?
8. **`.items()`**: What does `.items()` give you?
9. **`.append()`**: What does `.append()` do?
10. **`sum()`**: What does `sum()` do?

---

# 🔨 4–7 min — New Concepts: Functions & Sets

### 1. Functions (`def`)
In Day 6, you wrote logic directly inside your loop. But what happens when you need the same logic across different categories or multiple datasets?

You don't copy-paste code. You write a **function**:

```python
def sumation_fun(amount, t_amount):
    t_amount += int(amount)
    return t_amount
```

* `def` tells Python you are defining a function.
* `(amount, t_amount)` are the **parameters** (inputs).
* `return` sends the result back to whoever called the function.

```text
Inputs ──→ [ Function Logic ] ──→ Return Value
```

### 2. Sets and Tuples
* **Tuple** `(1, 2)`: An ordered collection that is **immutable** (cannot be changed after creation).
* **Set** `{1, 2, 3}`: An unordered collection of **unique** elements. It automatically discards duplicates!

In Data Engineering, finding unique values is an everyday task:

```python
categories = ["Food", "Travel", "Food", "Shopping", "Food"]
unique_categories = set(categories)
# Result: {'Food', 'Travel', 'Shopping'}
```

---

# 🛠️ 7–13 min — Your challenge: Week 1 Integration

Write a program that combines everything from Days 1–6:

### Step 1 — Store expense data
Create a list of expense dictionaries `expenses`:

```python
expenses = [
    {"Date": "Monday", "Category": "Food", "Amount": 250},
    {"Date": "Monday", "Category": "Travel", "Amount": 100},
    {"Date": "Tuesday", "Category": "Food", "Amount": 300},
    {"Date": "Tuesday", "Category": "Shopping", "Amount": 800},
    {"Date": "Wednesday", "Category": "Food", "Amount": 150},
    {"Date": "Thursday", "Category": "Entertainment", "Amount": 450},
    {"Date": "Thursday", "Category": "Travel", "Amount": 450}
]
```

### Step 2 — Create an accumulation function
Write a function `sumation_fun(amount, t_amount)` that takes an amount and an accumulator total, adds them, and returns the updated total.

### Step 3 — Process data and calculate category totals
Initialize accumulators for:
* `total_amount = 0`
* `total_food_amount = 0`
* `total_travel_amount = 0`
* `total_entertainment_amount = 0`
* `total_shopping_amount = 0`

Loop through `expenses`, calling your function to update `total_amount` and the corresponding category total whenever a match occurs.

### Step 4 — Formatted display
Use string formatting (`f"..."`) to cleanly print your summary report:

```text
Total expenses: ₹2500
Food expenses: ₹700
Travel expenses: ₹550
Entertainment expenses: ₹450
Shopping expenses: ₹800
```

### Step 5 — Reflect on your function
Answer these three questions in comments:
* A function is:
* My function takes:
* My function returns:

---

# ⭐ Bonus — Unique Categories with Sets

Notice how in Step 3 you had to write separate `if` checks for each category (`if category == 'Food'`, etc.). What if you had 50 categories?

1. Extract all category values from `expenses` and convert them into a `set()` to find all unique categories:
```python
unique_categories = set(expense['Category'] for expense in expenses)
print(unique_categories)
```
2. Think: How could this set eliminate hardcoded `if` statements in the future?

---

# ⏱️ Time rule

Your minimum commitment is **15 minutes**.
Phone physically away before you begin.
Take pride in completing Week 1—7 consecutive days of showing up and coding.

---

## 📝 Your Day 7 report

When you're done, send:

```text
Day 7:
Time:
Habit battle:
What I built:
What confused me:
What I learned:
```

And paste your code.

### Today's mindset:
> **Write logic once, reuse it everywhere. Functions turn scripts into software.** 🔥
