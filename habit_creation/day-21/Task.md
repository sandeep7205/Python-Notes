# 🚀 Day 21 — Let's Make Your Pipeline Tell the Truth

SKM, **Day 21.** 🐍🔥

You've now worked with:

```text
CSV
 ↓
Python
 ↓
cleaning
 ↓
processing
 ↓
JSON
 ↓
nested JSON
```

Today we're going to revisit something you've already touched but haven't properly mastered yet:

# 🎯 Day 21 — Data Validation: `None`, empty strings & `try/except`

This is important because **real data is rarely clean**.

Your Day 20 JSON already contained mixed data:

```json
"amount": 45.99
```

and:

```json
"amount": "120.00"
```

Your code handled both.

But what happens with:

```json
"amount": null
```

or:

```json
"amount": ""
```

or:

```json
"amount": "abc"
```

That's today's problem.

---

# 🧠 0–4 min — Recall

Before coding, answer these.

### 1. What does this mean?

```python
value = None
```

Is `None`:

* an empty string?
* zero?
* a missing/absent value?

---

### 2. What is the difference between:

```python
""
```

and:

```python
None
```

Think about what each one represents.

---

### 3. What happens here?

```python
float("")
```

What exception do you expect?

---

### 4. What happens here?

```python
float(None)
```

Do you think it's the same exception?

**Don't Google yet. Guess first.**

---

# 🔨 4–7 min — The concept

You currently have something like:

```python
if input_data['category']:
```

This is checking **truthiness**.

Python considers several things false:

```text id="1c5h5w"
None
""
0
False
[]
{}
```

But they're not the same thing.

For example:

```text id="4k2z9p"
None
```

usually means:

> **There is no value.**

While:

```text id="b8v1c4"
""
```

means:

> **There is a string, but it contains no characters.**

And:

```text id="x9m3q7"
"0"
```

means:

> **There is a string containing the number zero.**

That's why blindly using:

```python
if value:
```

can sometimes hide important differences.

---

# 🛠️ 7–15 min — Your challenge

Today we're going to make your `clean_data()` function more robust.

Use your **Day 20 JSON data** or create a few additional test records.

Add cases like:

```json
{
    "category": "",
    "amount": 100
}
```

```json
{
    "category": "Food",
    "amount": ""
}
```

```json
{
    "category": "Travel",
    "amount": "abc"
}
```

And:

```json
{
    "category": "Shopping",
    "amount": null
}
```

---

## Task 1 — Identify the bad data

Your function should distinguish between:

```text id="x6y8t1"
VALID
```

and:

```text id="c3p9m2"
INVALID
```

You don't need a complicated validation framework.

Just make your logic intentional.

---

## Task 2 — Handle conversion safely

Your current code has:

```python
float(...)
```

Make sure your function doesn't crash when the amount is:

```text id="1f0v6d"
"abc"
""
None
```

You already know `try/except`.

Now you're going to use it with a better understanding of **what you're actually catching**.

---

## Task 3 — Track WHY data was invalid

This is the interesting part.

Currently you have:

```text id="w5r3z8"
invalid_data_cnt
```

Try to make your quality information more useful.

Instead of only:

```text
Invalid rows: 4
```

think about:

```text id="v7x1c6"
Invalid rows: 4

Missing category: 1
Missing amount: 1
Invalid amount: 2
```

**You decide how to structure this.**

Hint:

> You've been using dictionaries for exactly this kind of problem.

---

# 🧩 Important constraint

Don't create a completely new project.

Modify your existing:

```text id="0r5h8n"
day-20/
```

project.

You're practicing **iterative improvement**, just like a real codebase.

---

# ⭐ Bonus

If the main task is finished, test this:

```text id="5f9w3a"
amount = 0
```

Ask yourself:

> Should `0` be considered invalid?

There's no universal answer.

For an expense tracker, you might decide it is invalid.

For another data pipeline, zero might be perfectly legitimate.

**The important thing is that your validation rule should be intentional.**

---

# 🧠 Today's deeper lesson

Yesterday you learned:

> Data can have different structures.

Today you're learning:

> **Data can have different meanings even when Python treats values as "false".**

For example:

```text id="k3j8q1"
None  → missing
""    → empty
"abc" → invalid format
"0"   → valid-looking numeric text
0     → actual numeric zero
```

That's **data quality thinking**.

And this becomes extremely important later when you work with:

* databases
* APIs
* CSV files
* pandas
* ETL pipelines
* AWS data services

---

## ⏱️ Your rule

**15 minutes minimum.**

Don't try to build a perfect validation framework.

Your minimum victory:

> **Handle missing/empty/invalid values without crashing and record useful information about them.**

If you naturally go beyond 15 minutes, fine.

But no punishment if you stop at 15.

---

## 📝 When you're done

Send me:

```text
Day 21:
Time:
Habit battle:
What I built:
What confused me:
What I learned:
```

And your updated `clean_data()` code.

I'll review **the validation logic**, not just whether the program runs.

### Today's principle:

> **A pipeline shouldn't merely avoid crashing. It should know when its data is bad — and tell you why.**

Let's cover Day 21. 🔥





---
---
---
---
---
---
---
---
---
---
---

Absolutely, SKM. **This is actually a very good real-world problem to discover on Day 21.**

You have:

```text
Laptop A
   ↓
.env exists locally
   ↓
GitHub
   ↓
Laptop B
   ↓
clone/pull project
   ↓
.env missing ❌
```

And that's expected if `.env` is in `.gitignore`.

The mistake would be to put the real `.env` into Git just to make the project work everywhere.

Instead, let's improve the project.

# 🚀 Day 21 — Configuration That Survives Different Machines

Today's original validation task is **postponed**.

We're going to solve this first because it's a real problem you're facing **right now**.

## 🎯 The goal

Your project should work on a new laptop with a simple setup process:

```text
GitHub
  ↓
clone project
  ↓
.env.example
  ↓
create your own .env
  ↓
run project
```

This is a standard development pattern.

---

# 🧠 First: understand the difference

### `.env`

Contains your **actual local values**:

```text
EXPENSE_CSV_FILE=...
EXPENSE_JSON_FILE=...
APP_NAME=Expense Tracker
```

This should generally stay out of Git if it contains secrets or machine-specific configuration.

### `.env.example`

Contains the **template**:

```text
EXPENSE_CSV_FILE=
EXPENSE_JSON_FILE=
APP_NAME=
```

This **can be committed to GitHub**.

So your repository tells another developer:

> "These are the configuration values you need."

But it doesn't expose your actual secrets.

---

# 🏗️ Your Day 21 project structure

I'd like you to move toward:

```text
day-21/
│
├── main.py
├── .env
├── .env.example
├── .gitignore
│
├── expenses.csv
│
└── src/
    └── expense_pipeline.py
```

Think:

```text
.env
   ↓
REAL LOCAL CONFIG
   ↓
NOT COMMITTED

.env.example
   ↓
CONFIG TEMPLATE
   ↓
COMMITTED TO GITHUB
```

---

# 🛠️ Your task

## Step 1 — Create `.env.example`

Take the variables you're currently using:

```text
APP_NAME
EXPENSE_CSV_FILE
EXPENSE_JSON_FILE
```

Put their **names** into `.env.example`.

Don't put your real secrets there.

---

## Step 2 — Make `.env` local

Your `.env` contains your actual values.

For example:

```text
APP_NAME=Expense Tracker
EXPENSE_CSV_FILE=...
EXPENSE_JSON_FILE=...
```

But `.env` should stay ignored by Git.

---

# 🧩 Step 3 — Think about the missing `.env`

Here's the next question:

What happens if someone clones your project and does:

```python
input_file = os.getenv("EXPENSE_CSV_FILE")
```

but the environment variable doesn't exist?

What will:

```python
os.getenv("EXPENSE_CSV_FILE")
```

return?

**Think before searching.**

That's today's little puzzle.

---

# 🔥 Step 4 — Handle missing configuration

Your program shouldn't fail later with something confusing like:

```text
TypeError
```

or:

```text
FileNotFoundError
```

Instead, you want your application to say something meaningful:

```text
Missing configuration: EXPENSE_CSV_FILE
Please create a .env file using .env.example
```

That's much better.

This is the exact kind of robustness I want you to start building.

---

# ⭐ Bonus — Configuration validation

You have three configuration values:

```text
APP_NAME
EXPENSE_CSV_FILE
EXPENSE_JSON_FILE
```

Think about creating something like:

```text
validate_config()
```

Its responsibility:

> Check that required configuration exists before the pipeline starts.

Then your program becomes:

```text
load configuration
       ↓
validate configuration
       ↓
     valid?
      /   \
    YES    NO
     ↓      ↓
 pipeline   clear error
```

That's a much better application flow.

---

# 🚨 Important: don't solve this by doing this

Don't put:

```text
password
API_KEY
database credentials
```

directly into GitHub just because another laptop needs them.

And don't blindly do:

```python
os.getenv("EXPENSE_CSV_FILE", "some-hardcoded-path")
```

for every configuration value.

Sometimes defaults are useful.

But for **required configuration**, it's often better to fail clearly.

---

# 🧠 Why I'm changing Day 21

You said:

> "we also need a way to handle these kind situation"

**Yes. Absolutely.**

This is actually better than blindly following the original exercise.

You're encountering the exact kind of problem that happens when software moves between:

```text
my laptop
   ↓
your laptop
   ↓
CI/CD
   ↓
server
   ↓
Docker
```

Configuration management becomes important very quickly.

So today we're turning that real problem into the lesson.

---

## 🎯 Minimum Day 21

You only need to accomplish:

```text
.env.example
       +
missing-config detection
       +
project still works with your local .env
```

**15 minutes is enough.**

Don't worry about secrets managers or Docker yet.

We'll get there later.

### Today's principle:

> **Your code should be portable; machine-specific configuration should not be hardcoded into it.**

And honestly, SKM — **this is exactly the kind of question I want you asking as you move toward Data Engineering.**

You didn't just ask *"why is my `.env` missing?"*

You asked:

> **"How should the system handle this situation?"**

That's the right question. 🔥
