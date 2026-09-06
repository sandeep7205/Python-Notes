# 🚀 Day 15 — Separate Data from Presentation

SKM, let's do it. Today is a **small but important engineering step**.

You've already learned:

```text
CSV
 ↓
read_data()
 ↓
clean_data()
 ↓
process_data()
```

But your `process_data()` currently does **two jobs**:

1. Calculates the totals.
2. Formats those totals into a string for printing.

Today we're going to separate those responsibilities.

---

# 🎯 Today's concept

Think about this:

```python
process_data()
```

should ideally **process data**.

It shouldn't care whether the result will be:

* printed in the terminal
* written to a CSV
* saved to a database
* displayed on a website
* sent to an API

That's the difference between:

```text
DATA
```

and

```text
PRESENTATION
```

---

# 🧠 0–3 min — Quick recall

Before coding, answer these:

### 1.

What is the difference between:

```python
return
```

and:

```python
print()
```

### 2.

What does this function currently return?

```python
def process_data(...):
    ...
    return category_str
```

Is it returning:

```text
A. dictionary
B. string
C. list
```

### 3.

Why might returning the dictionary be more useful than returning a formatted string?

Don't worry if #3 takes some thinking.

---

# 🔨 3–5 min — The idea

Currently your function eventually does this:

```text id="q6y1qp"
category_dict_amount
        ↓
convert to string
        ↓
return string
```

We're going to think about:

```text id="r0c6l3"
category_dict_amount
        ↓
return dictionary
```

Then **outside** the processing function:

```text id="0d9t8k"
dictionary
   ↓
print / display
```

So:

```text id="f7k6q2"
PROCESSING
    ↓
{"Food": 1200, "Travel": 550}
    ↓
PRESENTATION
    ↓
Food → 1200
Travel → 550
```

That's today's entire lesson.

---

# 🛠️ 5–12 min — Your challenge

Take your **Day 14 code**.

### Task 1 — Change `process_data()`

Make `process_data()` return the **dictionary of category totals**.

For example, conceptually:

```text id="r0y7wq"
{
    "Food": 1200,
    "Travel": 550,
    "Shopping": 800
}
```

Don't convert it into a string inside `process_data()`.

---

### Task 2 — Move presentation outside

After:

```python
get_process_data = process_data(get_clean_data)
```

you now have a dictionary.

Use another loop to display it:

```text id="m8v3x1"
Food → 1200
Travel → 550
Shopping → 800
```

**You write the actual code.**

---

# ⭐ Bonus — Data Engineer thinking

Once that works, calculate:

### Total expense

For example:

```text id="1y8q3p"
Food       → 1200
Travel     → 550
Shopping   → 800
Entertainment → 450

Total Expense → 3000
```

But don't create another function yet.

First get the main task working.

---

# 🧩 One question I want you to think about

Imagine tomorrow your manager says:

> "Don't print the category totals anymore. Save them into another CSV file."

Would you have to change `process_data()`?

If you separate processing from presentation correctly, the answer should be:

**No.**

That's why we're doing this.

---

## ⏱️ Time rule

Your minimum is still **15 minutes**.

If you finish in 15:

**STOP.**

If you're enjoying it and want to continue:

**Continue.**

But don't turn today's task into another accidental 1-hour session just because Day 14 went long.

---

## 📝 Send me this afterward

```text
Day 15:
Time:
Habit battle:
What I built:
What confused me:
What I learned:
```

And paste your code.

I'll review it and then we'll decide whether you're ready for **Day 16**.

**Today's principle:**

> **Process data first. Decide how to display it later.**

That's a small change in code, but a big change in how you think about software. 🔥
