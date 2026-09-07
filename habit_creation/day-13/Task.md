# 🚀 Day 13 — Let’s Build a Mini Data Pipeline

SKM, today we **refactor**, not start something completely new.

You've already built the logic on Day 12. Today we're going to make that logic **clean, reusable, and pipeline-like**.

### 🎯 Today's goal

Turn this:

```text
CSV
 ↓
one big block of code
 ↓
result
```

into this:

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

That's an important Data Engineering mindset: **separate responsibilities instead of putting everything into one block.**

---

## ⏱️ Your 15-minute mission

### 0–3 min → Recall

Without looking at your old code, explain to yourself:

1. What does `csv.DictReader` give you?
2. Why do we use `.strip()`?
3. Why do we use `int()` on Amount?
4. What does a function `return`?
5. What's the difference between a function's **input** and **output**?

Don't write code yet.

---

### 3–5 min → Understand today's concept

Imagine a restaurant kitchen.

You don't want one person to:

> buy ingredients → wash them → chop them → cook them → serve them

inside one giant operation.

Instead:

```text
Get ingredients
      ↓
Prepare ingredients
      ↓
Cook
      ↓
Serve
```

Same idea with data.

Each function should ideally have **one clear responsibility**.

---

# 🔨 5–12 min → Your actual task

Take your **Day 12 expense tracker**.

Don't create a new project.

Refactor it into **at least 3 functions**.

### Function 1 — Read

Think:

```text
read_data()
```

Its job:

> Open the CSV and get the data.

**Question for you:**
What should this function `return`?

---

### Function 2 — Clean

Think:

```text
clean_data()
```

Its job is things you've already learned:

* remove unwanted spaces
* normalize category names
* convert amount from string → integer
* handle invalid/missing data

**Question for you:**

If you give this function one row:

```text
{"Category": " food ", "Amount": "250"}
```

what should come out?

You decide the structure.

---

### Function 3 — Process

Think:

```text
process_data()
```

Its job:

> Calculate category totals.

For example:

```text
Food → 700
Travel → 1200
Shopping → 500
```

Again, decide:

**What should this function receive?**
**What should it return?**

---

## 🧠 One rule for today

Don't copy a solution from me.

I specifically want you to struggle a little with:

> **"What should this function take, and what should it return?"**

That's the important lesson today.

You already know enough Python syntax to attempt it.

---

### ⭐ Bonus — only if the main task is finished

Add:

```text
try / except
```

around the amount conversion so that something like:

```text
Amount = "abc"
```

doesn't crash your entire pipeline.

But **bonus means bonus**. Don't let it turn today's 15 minutes into a 90-minute project.

---

## 📝 When you're done, send me

```text
Day 13:
Time:
Habit battle:
What I built:
What confused me:
What I learned:
```

And paste your code.

I'll review it like a mentor/code reviewer — **I won't rewrite everything for you.** I'll point out what's correct, what's weak, and what you should improve.

**Today's target isn't a perfect pipeline. It's learning to think:**

> **Input → Transform → Output**

Let's go. 🔥
