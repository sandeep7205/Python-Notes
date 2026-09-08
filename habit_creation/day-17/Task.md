# 🚀 Day 17 — Let's Split the Pipeline

SKM, let's grab Day 17. 🔥

You've reached a point where your script is doing enough that keeping **everything in one file** starts becoming inconvenient.

Today we're going to learn something very important for real projects:

# 🎯 Day 17: Modules & Imports

You've already created functions:

```text id="r9u3c2"
read_data()
clean_data()
process_data()
```

Today we're going to understand:

> **How can I put these functions in another Python file and use them from my main program?**

This is the beginning of organizing Python projects properly.

---

## 🧠 0–3 min — Recall

Before coding, answer these:

### 1.

What is the benefit of putting your code into functions?

### 2.

Suppose you have:

```text id="b1g4x8"
expense_pipeline.py
main.py
```

If `read_data()` is inside `expense_pipeline.py`, what do you think `main.py` needs to do to use it?

Don't Google yet. Think first.

### 3.

What do you think this means?

```python id="k7q2pd"
import csv
```

You already used it several times.

What is Python actually doing when you write `import csv`?

---

# 🔨 3–6 min — Understand the idea

You've already been using modules without really focusing on them.

For example:

```python id="6q5r1n"
import csv
```

`csv` isn't a function.

It's a **module** — a collection of Python code that provides functionality you can use.

Think:

```text id="h4n8wx"
Python
 │
 ├── csv
 ├── datetime
 ├── os
 └── json
```

You import a module when you want to use its functionality.

---

# 🧩 Your own module

Now imagine:

```text id="e7w2pa"
expense_pipeline.py
```

contains:

```text id="8m2f0s"
read_data()
clean_data()
process_data()
```

And:

```text id="c4k6vz"
main.py
```

is responsible for running the program.

Conceptually:

```text id="5w9r3a"
expense_pipeline.py
        │
        │ functions
        ↓
     main.py
        │
        ↓
      output
```

That's what we're building today.

---

# 🛠️ 6–15 min — Your challenge

Take your existing Day 16 project.

### Step 1

Create a new Python file.

Something like:

```text id="w5g0rm"
expense_pipeline.py
```

Move these functions into it:

```text id="6z8f2k"
read_data()
clean_data()
process_data()
```

**Don't move the actual execution code yet.**

---

### Step 2

Create another file:

```text id="z2c7vb"
main.py
```

This becomes your program's entry point.

It should contain the code that:

1. defines the CSV path
2. calls `read_data()`
3. calls `clean_data()`
4. calls `process_data()`
5. displays the result

---

### Step 3 — The important part

Now figure out how `main.py` can use:

```text id="8h2m1v"
read_data()
clean_data()
process_data()
```

from:

```text id="p4v6ka"
expense_pipeline.py
```

**I am deliberately not giving you the import syntax yet.**

Try to figure it out.

You already know:

```python id="w2z9jc"
import csv
```

So ask yourself:

> "If `csv` can be imported, can my own Python file also be imported?"

That's today's little puzzle.

---

# ⭐ Bonus

Once you get it working, look at your project and ask:

> "Which code belongs to the pipeline, and which code belongs to running/displaying the application?"

You might discover that:

```text id="c1s8qv"
expense_pipeline.py
```

doesn't need to know anything about:

```text id="9z7v3k"
print()
```

That's a good sign.

---

# ⚠️ One thing to watch for

You currently have:

```python id="5g8w2m"
import csv
```

**inside** `read_data()`.

Today, think about whether that import belongs:

```text id="h5u4kd"
inside the function
```

or:

```text id="j7v3px"
at the top of the module
```

Don't overthink it. Just notice it.

---

# ⏱️ Your rule

**15 minutes minimum.**

If the import/module stuff takes longer because you're experimenting, that's okay.

But don't turn today into:

> "I must completely redesign my project."

No.

Today's victory is simply:

```text id="4c9z1q"
ONE FILE
   ↓
TWO FILES
   ↓
IMPORT
   ↓
WORKING PROGRAM
```

---

## 📝 When you're done

Send me:

```text id="k6s1zp"
Day 17:
Time:
Habit battle:
What I built:
What confused me:
What I learned:
```

And show me **both files**.

I'll review how you've separated them.

### Today's principle:

> **A module lets you organize reusable code so other parts of your program can use it.**

Let's grab it. 🐍🔥
