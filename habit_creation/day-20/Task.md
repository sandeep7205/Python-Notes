# 🚀 Day 19 — Let's Attack JSON

SKM, Day 19. 🔥

You've worked with **CSV → dictionaries** for several days. Today we're going to learn another format you'll see constantly in real Data Engineering:

> **JSON**

And we're going to connect it directly to what you already know instead of learning it as random syntax.

---

# 🎯 Today's goal

Understand:

* What JSON is
* JSON object vs Python dictionary
* `json.load()`
* `json.dump()`
* Reading JSON
* Writing JSON
* Why JSON is useful in data pipelines

Your mental model:

```text id="8zj4v2"
CSV
 ↓
DictReader
 ↓
Python dictionaries
```

Today:

```text id="7w2k5n"
JSON
 ↓
json.load()
 ↓
Python dictionaries/lists
```

---

# 🧠 0–4 min — Recall

Answer these **without looking at your previous code**.

### 1.

What Python data structure are you using here?

```python
category_dict_amount = {}
```

---

### 2.

What does `csv.DictReader` do?

---

### 3.

What's the difference between:

```python
return data
```

and:

```python
print(data)
```

---

### 4.

Imagine you have:

```text
Food → 1200
Travel → 550
Shopping → 800
```

Why might we want to save this result to a file instead of only printing it?

Think from a **Data Engineering** perspective.

---

# 🔨 4–7 min — What is JSON?

JSON stands for:

**JavaScript Object Notation**

Don't let the name scare you.

It's simply a common way to represent structured data.

For example:

```json
{
    "Food": 1200,
    "Travel": 550,
    "Shopping": 800
}
```

Looks familiar, right?

Because Python has:

```python
{
    "Food": 1200,
    "Travel": 550,
    "Shopping": 800
}
```

They're conceptually very similar.

But here's the important distinction:

```text id="x5q1nz"
JSON file
    ↓
data stored as JSON text

Python dictionary
    ↓
data currently represented inside Python
```

You need a conversion between them.

---

# 🔄 The two directions

### JSON → Python

You want to **read** JSON:

```text id="8j3w2x"
JSON file
   ↓
json.load()
   ↓
Python object
```

### Python → JSON

You want to **save** Python data:

```text id="q4m7yc"
Python object
   ↓
json.dump()
   ↓
JSON file
```

Remember this pair:

> **load = bring data into Python**

> **dump = send Python data into a file**

---

# 🛠️ 7–15 min — Your mission

We're going to extend your expense project.

### Task 1 — Create a JSON file

Create something like:

```text id="n6f8q2"
expense_summary.json
```

Put some category data inside it manually.

For example:

```json
{
    "Food": 1200,
    "Travel": 550
}
```

Don't copy my exact values if you don't want to.

---

### Task 2 — Read the JSON with Python

Create a small function:

```text id="p4z1x8"
read_json()
```

Its responsibility:

> Open the JSON file and return the data as a Python object.

Your target mental flow:

```text id="2h7wq5"
JSON file
   ↓
read_json()
   ↓
Python dictionary
```

**Don't ask me for the exact code yet.**

You already know:

```python
with open(...)
```

and you've seen:

```python
csv.DictReader(...)
```

Now investigate the `json` module and find the equivalent operation.

---

### Task 3 — Save your processed result

This is the fun part.

Your existing pipeline already produces:

```text id="k8v2pd"
get_process_data
```

which is a dictionary.

Instead of only:

```python
print(category_str)
```

save the dictionary into:

```text id="j6r3w9"
expense_summary.json
```

Your pipeline becomes:

```text id="m4t8q1"
expenses.csv
      ↓
read_data()
      ↓
clean_data()
      ↓
process_data()
      ↓
dictionary
      ↓
JSON file
```

🔥 **That's a real data pipeline.**

---

# 🧩 One important challenge

You have two operations:

```text id="y5x2kd"
Python → JSON
JSON → Python
```

Try to figure out which one uses:

```text id="v7c3nm"
json.load()
```

and which uses:

```text id="r2f8qa"
json.dump()
```

Don't memorize blindly.

Think about the English:

**load** something into Python.

**dump** something out into a file.

---

# ⭐ Bonus

Once your JSON writing works, open the generated file manually.

Look at it.

Ask yourself:

> "Does the data stored in the JSON represent the same information as my Python dictionary?"

Then modify the JSON file manually and use your `read_json()` function to bring it back into Python.

That's optional.

---

# ⚠️ Don't go down these rabbit holes today

Not yet:

* JSON Schema
* APIs
* nested JSON transformations
* pandas
* REST APIs
* serialization theory
* complex JSON structures

Today is simply:

```text
JSON
 ↓
Python
 ↓
JSON
```

---

# ⏱️ Minimum

**15 minutes.**

If you understand `load()` and `dump()` and get one working example:

### Day 19 = success.

If you get stuck, that's okay.

Try:

> Think → search → experiment → debug → understand.

Don't immediately copy a solution.

---

## 📝 Your Day 19 report

When finished:

```text
Day 19:
Time:
Habit battle:
What I built:
What confused me:
What I learned:
```

And paste your code.

I'll review it and we'll attack **Day 20** from there.

### Today's principle:

> **Data isn't useful only when you calculate it. It becomes much more useful when you can store it, move it, and read it again.**

Let's attack it. 🐍🔥
