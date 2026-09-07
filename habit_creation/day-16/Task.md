# 🚀 Day 16 — Let's Handle Real-World Data

SKM, let's ride. 🔥

You've now built a small pipeline:

```text
CSV
 ↓
read_data()
 ↓
clean_data()
 ↓
process_data()
 ↓
dictionary
 ↓
display
```

Today we're going to make one important improvement:

# 🎯 Day 16: Separate **Data Cleaning** from **Data Quality Reporting**

Right now your `clean_data()` function does several things:

* cleans the data
* validates the data
* counts valid/invalid rows
* prints messages

That's starting to become too much responsibility for one function.

Today we'll learn how to make functions **more focused**.

---

## 🧠 0–3 min — Recall

Answer these before coding:

### 1.

Your `process_data()` now returns:

```python
{"Food": 1200, "Travel": 550}
```

Why is this better than returning:

```text
Food → 1200
Travel → 550
```

---

### 2.

What is the purpose of `try/except`?

---

### 3.

If this happens:

```python
amount = float("abc")
```

which exception do you expect?

---

### 4.

In your current `clean_data()` function, how many different jobs is the function doing?

Look carefully. Don't just say "cleaning."

---

# 🔨 3–6 min — Today's idea

Imagine your pipeline has two responsibilities:

```text
             RAW DATA
                ↓
        ┌───────────────┐
        │ clean_data()  │
        └───────────────┘
                ↓
          CLEAN DATA
                ↓
        ┌───────────────┐
        │ process_data()│
        └───────────────┘
                ↓
             RESULT
```

But we also want to know:

```text
Valid rows: 10
Invalid rows: 3
```

That's **data quality information**.

So conceptually:

```text
Clean the data
      ↓
Produce clean data

AND

Track data quality
      ↓
Produce quality information
```

The question is:

> **Should one function be responsible for both?**

That's what I want you to think about today.

---

# 🛠️ 6–15 min — Your challenge

Take your existing Day 15 code.

### Task 1 — Remove unnecessary printing from `clean_data()`

Currently you have things like:

```python
print('Skip the invalid data')
```

and:

```python
print(f"Total rows: ...")
```

Today, try to make `clean_data()` **return information instead of printing it**.

Think about what information the caller might need.

For example, conceptually:

```text
clean_data()
      ↓
clean rows
+
quality information
```

**You decide the structure.**

Maybe a dictionary?

Maybe something else?

Don't ask me yet. Think first.

---

### Task 2 — Keep `process_data()` focused

`process_data()` should continue doing only this:

> Take clean data → calculate category totals → return the result.

Don't add printing there.

You've already learned this yesterday.

---

### Task 3 — Display everything at the end

Your main program should eventually be responsible for deciding what gets displayed:

```text
Valid rows: ...
Invalid rows: ...

Food → ...
Travel → ...

Total Expense → ...
```

Notice the architecture:

```text
read_data()
     ↓
clean_data()
     ↓
process_data()
     ↓
display
```

Each stage has a clearer responsibility.

---

# 🧩 Important challenge

You need to decide:

> **What should `clean_data()` return?**

You need both:

```text
clean rows
```

and:

```text
valid/invalid counts
```

So ask yourself:

> "Can Python return more than one thing?"

Don't Google the answer immediately.

**Think for a couple of minutes first.**

This is exactly the kind of question I want you to learn to solve independently.

---

# ⭐ Bonus — only if the main task is done

Remember your Day 15 bug:

```python
total_amount += int(value)
```

Your amounts are floats.

Fix the calculation so:

```text
250.75
```

doesn't become:

```text
250
```

And if you want an additional challenge, format your final amounts to **2 decimal places**.

---

# ⏱️ Time rule

**15 minutes is enough.**

If you're stuck for 5 minutes on one thing:

1. Think.
2. Try.
3. Search/documentation.
4. Try again.

Don't sit staring at the screen for 30 minutes.

And don't immediately ask me for the answer.

I want you to experience the little:

> **"Ohhh... that's how Python does it."**

moment yourself.

---

## 📝 When finished

Send me:

```text
Day 16:
Time:
Habit battle:
What I built:
What confused me:
What I learned:
```

And your code.

I'll review it with you.

### Today's principle:

> **A good function doesn't just work. It has a clear responsibility.**

Let's ride Day 16. 🐍🔥
