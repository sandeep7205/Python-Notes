# 🚀 Day 14 — Let's Make Your Pipeline Robust

SKM, today we're going one small step beyond Day 13.

Yesterday you built:

```text
CSV
 ↓
read_data()
 ↓
clean_data()
 ↓
process_data()
 ↓
result
```

Today we're going to deal with something **very real in Data Engineering**:

> **What happens when the data is bad?**

Real-world data is messy. Files can contain missing values, invalid numbers, extra spaces, unexpected formats, etc.

So today's focus is **error handling + data validation**.

---

## 🎯 Today's goal

By the end of today, your pipeline should be able to encounter something like:

```text
Category,Amount
Food,250
Travel,abc
Shopping,
 food ,500
,300
```

…and **not crash just because one row is bad**.

Instead, your pipeline should recognize the bad row and skip it.

---

# ⏱️ Your 15-minute mission

### 🧠 0–3 min — Recall

Before touching your code, answer these:

1. What is the difference between `return` and `print()`?
2. What does `float("250.50")` produce?
3. What happens if you execute `float("abc")`?
4. Why might `if input_data['Amount']` not be enough to validate an amount?
5. What problem does `try/except` solve?

Don't worry if #4 or #5 isn't clear yet.

---

# 🔨 3–5 min — Understand `try/except`

You've probably seen Python crash with something like:

```text
ValueError
```

For example, conceptually:

```text
"250" → float → ✅
"250.50" → float → ✅
"abc" → float → ❌
```

The problem is:

```text
one bad row
    ↓
exception
    ↓
entire program stops
```

We want:

```text
one bad row
    ↓
exception
    ↓
skip/report row
    ↓
continue processing remaining rows
```

That's where `try/except` comes in.

---

# 🛠️ 5–12 min — Your challenge

**Modify your Day 13 `clean_data()` function.**

Don't rewrite the whole project.

Your job is to make this part robust:

```text
Category
Amount
```

### Your cleaning function should:

**1. Check that Category exists**

```text
missing category → invalid
```

**2. Check that Amount exists**

```text
missing amount → invalid
```

**3. Clean whitespace**

```text
" food " → "Food"
```

**4. Convert Amount to `float`**

```text
"250.50" → 250.5
```

**5. Handle invalid amounts**

```text
"abc"
```

should **not crash your program**.

Instead, skip that row.

---

## 🧩 One important challenge

Remember the problem I pointed out yesterday?

You had:

```python
if input_data['Category'] and input_data['Amount'] and float(...):
```

Think about why that's not ideal.

I want you to separate:

```text
VALIDATION
     ↓
CONVERSION
```

rather than doing everything inside one `if`.

That's the main thinking exercise today.

---

# ⭐ Bonus — only if you finish early

Add a counter:

```text
Valid rows: 8
Invalid rows: 2
```

So your pipeline doesn't just silently throw bad data away.

That's a tiny step toward **data quality monitoring**.

---

# 🚫 Don't do this today

Don't jump into:

* pandas
* NumPy
* AWS
* Airflow
* databases
* advanced exception handling

Not yet.

We're building the foundation properly.

---

## 📝 Your Day 14 report

When you're done, send:

```text
Day 14:
Time:
Habit battle:
What I built:
What confused me:
What I learned:
```

And paste your code.

I'll review it without immediately giving you the corrected version.

### Today's mindset:

> **Don't try to write perfect code. Try to understand what happens when your code meets imperfect data.**

That's where the Data Engineer mindset starts. 🔥
