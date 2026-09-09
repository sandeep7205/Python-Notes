# 🚀 Day 18 — Let's Build Configuration

SKM, let's build Day 18. 🔥

You've reached a nice point in your project.

Right now `main.py` contains this:

```python
input_file = "habit_creation/day-17/expenses.csv"
```

It works.

But there's a problem:

> **Your program's logic is now mixed with configuration.**

Today we're going to separate them.

---

# 🎯 Day 18 Goal

Learn:

* What configuration means
* Environment variables
* `.env` files
* `os.environ`
* `python-dotenv`
* Why secrets/configuration shouldn't be hardcoded

And we'll apply it to your expense pipeline.

The flow will eventually look like:

```text
.env
 ↓
configuration
 ↓
main.py
 ↓
expense_pipeline.py
 ↓
CSV
```

---

# 🧠 0–4 min — Recall

Answer these before coding.

### 1. What's the difference between:

```python
import expense_pipeline
```

and:

```python
from src import expense_pipeline
```

---

### 2. Why did we separate `main.py` and `expense_pipeline.py`?

---

### 3. Look at this:

```python
input_file = "habit_creation/day-17/expenses.csv"
```

Is this:

**A. Business logic**

or

**B. Configuration**

Think carefully.

---

### 4. Imagine your program needs:

```text
CSV file location
database password
API key
database host
```

Would you want these values directly inside your Python code?

Why or why not?

---

# 🔨 4–7 min — Understand configuration

Configuration means:

> **Values that control how your program runs, rather than the actual logic of what the program does.**

For example:

```text
Configuration
----------------
CSV_FILE = expenses.csv
DATABASE_HOST = localhost
DATABASE_PORT = 5432
```

While:

```text
Program logic
----------------
read CSV
clean data
calculate totals
```

These are different things.

---

# 🌱 Environment variables

You've probably seen things like:

```text
PATH
TEMP
USERNAME
```

in your operating system.

Those are environment variables.

Python can access them using the `os` module.

Conceptually:

```text
Operating System
       ↓
Environment variable
       ↓
Python
       ↓
Your program
```

For example, conceptually:

```text
CSV_FILE = "expenses.csv"
```

can live outside your Python code.

---

# 🔐 Why this matters

Imagine you eventually connect your Data Engineering project to a database.

You might need:

```text
username
password
host
API key
```

You **do not** want:

```python
password = "MySuperSecretPassword123"
```

inside your source code.

Why?

Because your code may eventually go into:

* Git
* GitHub
* a company repository
* Docker
* CI/CD

You don't want secrets sitting there.

---

# 🛠️ 7–15 min — Today's challenge

We're going to keep this simple.

### Step 1 — Create `.env`

Inside your Day 18 project, create:

```text
.env
```

Put your CSV path in it.

For example:

```text
EXPENSE_FILE=habit_creation/day-18/expenses.csv
```

**You choose the exact path based on your project structure.**

---

### Step 2 — Install/use `python-dotenv`

You need to understand the role of this package.

It allows Python to load values from:

```text
.env
```

into environment variables.

Conceptually:

```text
.env
 ↓
load_dotenv()
 ↓
os.getenv()
 ↓
Python variable
```

---

### Step 3 — Modify `main.py`

Your goal is to remove the hardcoded:

```python
input_file = "..."
```

and instead get the path from your environment.

Your final flow should conceptually be:

```text
.env
 ↓
EXPENSE_FILE
 ↓
main.py
 ↓
read_data(EXPENSE_FILE)
```

**I am deliberately not giving you the exact code.**

You've already learned enough Python to investigate this.

Try:

1. Think.
2. Search.
3. Experiment.
4. Debug.
5. Ask me if you're genuinely stuck.

---

# ⭐ Bonus challenge

Once it works, add another configuration:

```text
APP_NAME=Expense Tracker
```

Then retrieve it from the environment and display:

```text
Expense Tracker
---------------
Total rows: ...
Valid rows: ...
Invalid rows: ...

Food → ...
Travel → ...
```

This isn't about making a fancy application.

It's about understanding:

> **configuration lives outside your logic.**

---

# ⚠️ One important `.env` rule

If you eventually use Git:

```text
.env
```

should generally **not be committed** when it contains secrets.

You'll eventually learn:

```text
.gitignore
```

and how teams manage configuration safely.

For today's exercise, don't worry about Git yet.

---

# 🧩 Your Day 18 architecture

You're moving toward:

```text
day-18/
│
├── .env
├── main.py
├── expenses.csv
│
└── src/
    └── expense_pipeline.py
```

And:

```text
              .env
                │
                ↓
        configuration
                │
                ↓
             main.py
                │
                ↓
       expense_pipeline.py
                │
                ↓
              result
```

That's becoming a real little Python project.

---

## ⏱️ The rule

**15 minutes minimum.**

Don't spend an hour making the project beautiful.

Your only required victory today is:

> **Remove the hardcoded CSV path and successfully load it from `.env`.**

If you finish that in 15 minutes:

**Day 18 is a success.**

If you naturally want to investigate more, go ahead.

---

## 📝 When you're done

Send me:

```text
Day 18:
Time:
Habit battle:
What I built:
What confused me:
What I learned:
```

And show me:

* `.env`
* `main.py`
* anything you changed in `src/`

I'll review the whole flow.

### Today's principle:

> **Keep configuration outside your code so your code can change without changing the program's logic.**

Let's build it. 🐍🔥
