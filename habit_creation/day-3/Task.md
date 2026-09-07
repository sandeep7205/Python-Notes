# 🚀 Day 3 — Loops (The for Loop)

SKM, welcome to Day 3!

Over the last two days, you built variables and added decision-making with conditionals.

Today, we introduce a core building block of programming and Data Engineering: **repetition**.

Imagine you have a list of technologies or data records:

```text
Python
SQL
AWS
Docker
Git
```

Without a loop, you would have to write separate print statements or processing logic for each one manually.

A loop lets you tell Python:
> **"Take each item, one at a time, and do this."**

---

## 🎯 Today's goal

Create a list of technologies for Data Engineering and use a `for` loop to iterate through them and process each item.

---

# ⏱️ Your 15-minute mission

### 🧠 0–3 min — Recall

Without opening your previous code, answer these:

1. What is a variable?
2. What does `if` do?
3. What does `elif` do?
4. What does `else` do?
5. What does `experience > 2 and experience < 4` mean?

---

# 🔨 3–5 min — Why Loops?

Without a loop:

```python
print("I want to learn Python")
print("I want to learn SQL")
print("I want to learn AWS")
```

With a `for` loop:

```python
tech_list = ['Python', 'SQL', 'AWS']

for tech in tech_list:
    print(f"I want to learn {tech}")
```

The mental model:

```text
tech_list: ['Python', 'SQL', 'AWS']
                ↓
    Iteration 1: tech = 'Python' → execute block
    Iteration 2: tech = 'SQL'    → execute block
    Iteration 3: tech = 'AWS'    → execute block
```

---

# 🛠️ 5–12 min — Your challenge

1. Create a list named `tech_list` containing **5+ technologies/tools** you want to learn for Data Engineering (e.g., Python, SQL, AWS, Docker, Git).
2. Write a `for` loop to iterate through the list and print each technology in a sentence (e.g., `"I want to learn Python"`).

---

# ⭐ Bonus — Combine Loops and Conditions

Data Engineering is all about processing collections based on rules.

Try combining your loop with `if / elif / else`:
* Create sub-lists for learning phases, such as:
  ```python
  completed_phase = ['Program basics']
  learning_phase = ['Python', 'SQL']
  ```
* In your loop, check each technology:
  * If it's in `completed_phase` → mark as `"Completed"`
  * If it's in `learning_phase` → mark as `"Learning"`
  * Otherwise → mark as `"Later"`
* *Extra challenge:* Experiment with `enumerate(tech_list, start=1)` to display numbered items (e.g., `1. Python`).

---

# ⏱️ Time rule

Your minimum commitment is **15 minutes**.
Don't use a countdown timer that stresses you out. Just note your start time and code.
If you're enjoying it at the 15-minute mark, keep going. If not, stop.

---

## 📝 Your Day 3 report

When you're done, record:

```text
Day 3:
Time:
Habit battle:
What I built:
What confused me:
What I learned:
```

And paste your code.

### Today's mindset:

> **"Repetition without copy-pasting is the first superpower of programming."** 🔥
