SKM, **Day 18 COMPLETE.** 🔥

And your project is now moving from "Python practice script" toward a small, structured application.

The most important thing today isn't `.env` itself. It's that you're starting to understand **separation of concerns**:

```text
Configuration
      ↓
main.py
      ↓
pipeline module
      ↓
data
```

## 🧠 Your answers

### 1. `import expense_pipeline` vs `from src import expense_pipeline`

Your answer is **mostly right**, but there's one correction.

It's not about using an alias.

The difference is about **where Python finds the module**.

For example:

```text
day-18/
├── main.py
└── expense_pipeline.py
```

You could use:

```python
import expense_pipeline
```

Whereas with:

```text
day-18/
├── main.py
└── src/
    └── expense_pipeline.py
```

you can use:

```python
import src.expense_pipeline
```

or:

```python
from src import expense_pipeline
```

The `as` keyword is specifically for an alias:

```python
import src.expense_pipeline as pe
```

Then you can write:

```python
pe.read_data()
```

So remember:

> **`import` / `from` → where/how you access the module.**
> **`as` → what shorter name you want to use.**

---

### 2. Why separate `main.py` and `expense_pipeline.py`?

Correct. ✅

You said:

> "we can reuse the module file somewhere else"

Exactly.

Your `expense_pipeline.py` doesn't care whether `main.py` uses it.

Another program could eventually do:

```text
another_program
      ↓
expense_pipeline
```

That's the power of modularity.

---

### 3. Hardcoded CSV path

Correct:

**B. Configuration** ✅

---

### 4. Password/API key/etc.

Your thinking is correct. ✅

One important refinement:

> `.env` is useful for keeping configuration/secrets **out of source code**, but it isn't magically a secure vault.

For local development it's common.

For production, teams often use proper secret-management systems.

You don't need to worry about those yet.

---

# 🔥 Your implementation

This is the important part:

```python id="m7v4qs"
app_name = os.getenv("APP_NAME")
input_file = os.getenv("EXPENSE_FILE")
```

Then:

```python id="w2x6a9"
get_csv_data = pe.read_data(input_file)
```

You successfully created:

```text id="l8k3pf"
.env
 ↓
os.getenv()
 ↓
main.py
 ↓
read_data()
```

That's exactly today's goal.

---

# 🟢 Good change in `expense_pipeline.py`

You also removed:

```python id="g7d2n1"
"total_data_cnt": 0
```

and you're calculating total rows from:

```python id="p8q4mx"
valid_data_cnt + invalid_data_cnt
```

That's perfectly reasonable for your current pipeline.

---

# ⚠️ One thing I'd clean up

You currently have:

```python id="f6c8w2"
load_dotenv()
load_dotenv(dotenv_path="habit_creation/day-18/config/.env")
```

You generally don't need **both**.

You're effectively telling dotenv:

> "Load the default `.env`."

and then:

> "Also load this other `.env`."

For today's experiment, it's fine.

But in a real project, I'd want **one clear source of configuration**.

For example:

```text
day-18/
├── main.py
├── config/
│   └── .env
└── src/
    └── expense_pipeline.py
```

Then explicitly load the intended configuration file.

**Don't change it just for the sake of changing it.** Your experiment helped you understand how `load_dotenv()` works.

---

# ⚠️ Another thing to understand

You wrote:

```python id="u4w7q2"
from dotenv import load_dotenv, find_dotenv
```

but you're not using:

```python id="q8s3n1"
find_dotenv
```

That's harmless, but unnecessary.

You can remove unused imports when you clean up.

---

# 🧠 One terminology correction

You said:

> "safe place where only i can see and use"

Be careful with this assumption.

A `.env` file is **not automatically safe**.

It's just a file.

The important practice is:

```text
.env
 ↓
.gitignore
 ↓
don't commit secrets to Git
```

And eventually:

```text
Production
 ↓
Secret Manager
```

We'll learn that later.

---

# 🏗️ Your project is now looking like this

```text id="4t9p8d"
day-18/
│
├── main.py
│
├── config/
│   └── .env
│
└── src/
    └── expense_pipeline.py
```

And responsibilities are becoming clear:

### `.env`

```text
Configuration
```

### `main.py`

```text
Application flow
```

### `expense_pipeline.py`

```text
Data processing
```

That's good architecture for where you are right now.

---

# 🏆 Day 18 scorecard

| Skill                  | Result |
| ---------------------- | ------ |
| Modules                | ✅      |
| Nested module import   | ✅      |
| Aliases                | ✅      |
| Configuration          | ✅      |
| Environment variables  | ✅      |
| `os.getenv()`          | ✅      |
| `.env`                 | ✅      |
| `python-dotenv`        | ✅      |
| Separation of concerns | 🔥     |
| Project structure      | 🔥     |

### **DAY 18 — COMPLETE ✅**

And I noticed something else:

Your habit battle wasn't even mentioned as a major struggle this time. You're now completing these sessions even when the timing isn't exactly 8 PM.

That's progress.

**The clock is becoming less important. Showing up is becoming more important.**

---

### Day 19 will be a little different.

We're going to take the next step with **JSON**.

You've already worked with CSV → dictionaries.

Now you'll learn another format you'll encounter constantly in Data Engineering:

```text
JSON
```

We'll use it practically rather than just memorizing syntax.

**One brick at a time. 🧱🐍**




Haha, no problem, SKM 😄. **Day 18 report officially recorded.**

And your summary captures the actual lesson well:

> **Configuration data should be separated from application logic.**

One small correction: `.env` improves **configuration management and helps keep secrets out of source code**, but `.env` itself isn't a secure vault.

### 🏁 Day 18 Final Record

|                  |                                                                     |
| ---------------- | ------------------------------------------------------------------- |
| **Time**         | ~23 min                                                             |
| **Habit battle** | Didn't start at 8 PM, but completed                                 |
| **Built**        | Real-world project configuration                                    |
| **Confused by**  | `find_dotenv`                                                       |
| **Learned**      | Separating configuration from logic for better security/reliability |
| **Status**       | ✅ COMPLETE                                                          |

And regarding `find_dotenv`: **don't worry about mastering it yet.** You experimented with it, which is enough for now. We'll revisit it when there's a practical reason to use it.

Most importantly:

**8 PM is a trigger, not a deadline.**

You didn't start at 8, but you finished Day 18. That's exactly the flexibility we want in this habit.

**18 days of building. Keep the streak of returning, not the streak of perfection. 🧱🐍**

