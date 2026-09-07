# 🚀 Day 8 — File Reading

SKM, welcome to **Week 2**!

In Week 1, all your data lived directly inside your Python code as hardcoded lists and dictionaries:

```python
expenses = [{"Category": "Food", "Amount": 250}, ...]
```

That was great for learning fundamentals, but real Data Engineering never works like that. Data lives in **external files, databases, APIs, and data lakes**.

Today we take our first step into the real world:

> **Reading data from external files into Python.**

---

## 🎯 Today's goal

You have two text files in your `day-8` folder:
1. `learning.txt` — a list of Data Engineering learning topics.
2. `expenses.txt` — a list of expense categories.

By the end of today, you will:
1. Open and read files using Python's built-in `open()`.
2. Understand the difference between `.read()`, `.readline()`, and `.readlines()`.
3. Discover how `.strip()` handles hidden newline characters (`\n`).
4. Read `expenses.txt` and count how many times `"Food"` appears.

---

# ⏱️ Your 15-minute mission

### 🧠 0–3 min — Recall

Before touching file code, answer these from memory:

1. What is a variable?
2. What is a list?
3. What is a dictionary?
4. What does a `for` loop do?
5. What does a function do?
6. What does `.append()` do?
7. What does `.items()` do?
8. What does `sum()` do?

Keep your answers short.

---

# 🔨 3–5 min — Understand the 3 ways to read a file

When you open a file in Python:

```python
with open("habit_creation/day-8/learning.txt", "r") as f:
    ...
```

Python provides three primary reading methods:

```text
learning.txt
     │
     ├─► .read()       ──► "Line 1\nLine 2\nLine 3" (one single string)
     │
     ├─► .readline()   ──► "Line 1\n" (one line at a time)
     │
     └─► .readlines()  ──► ["Line 1\n", "Line 2\n", "Line 3\n"] (list of lines)
```

| Method | What it returns | When to use |
|---|---|---|
| `.read()` | One single string containing the whole file | Small files where you want all text at once |
| `.readline()` | A single line as a string | Reading large files line by line without loading all into memory |
| `.readlines()` | A list of strings (one per line) | When you want to loop over lines using index or `for` loop |

> [!NOTE]
> Each line returned by `.readline()` or `.readlines()` ends with an invisible newline character: `\n`.
> That is why `.strip()` is essential when comparing text!

---

# 🛠️ 5–12 min — Your challenge

You already have `learning.txt` and `expenses.txt` in your `day-8` folder.

### Challenge 1 — Experiment with `learning.txt`

1. Open `learning.txt` using `open("habit_creation/day-8/learning.txt", "r")` or `with open(...) as f:`.
2. Read and print the entire contents using `.read()`.
3. Experiment with `.readline()`: call it multiple times and observe how Python reads one line after another.
4. Read the file using `.readlines()`.
   - Store the result in a variable.
   - Print that variable and observe what each element looks like (look for `\n`).
   - Print its `len()` to see how many lines are in the file.

### Challenge 2 — Count "Food" in `expenses.txt`

Now switch to `expenses.txt`:

1. Open `expenses.txt` and read all lines into a list using `.readlines()`.
2. Initialize a counter variable `f_cnt = 0`.
3. Loop through each line with a `for` loop:
   - Use `.strip()` on each line to remove trailing whitespace and `\n`.
   - If the category is `"Food"`, increment your counter (`f_cnt += 1`).
4. Print the final count:
   ```text
   Food appears 4 times.
   ```

---

# ⭐ Bonus — Count other categories

Extend your loop to count the other categories present in `expenses.txt` (`Travel`, `Shopping`, `Entertainment`):

```text
Food appears 4 times.
Travel appears 2 times.
Shopping appears 1 times.
Entertainment appears 1 times.
```

Notice what happens:
- You had to create `f_cnt`, `t_cnt`, `s_cnt`, `e_cnt`...
- **Think:** What happens if tomorrow there are 50 different categories? Would you want to create 50 separate counter variables?
- Keep this question in mind for Day 9!

---

# 🚫 Don't do this today

Don't jump into:
* Writing or modifying files (`"w"` or `"a"` mode)
* `try/except FileNotFoundError` error handling
* External libraries like `pandas`

Focus on mastering the fundamentals of reading files cleanly.

---

## 📝 Your Day 8 report

When you're finished, send:

```text
Day 8:
Time:
Habit battle:
What I built:
What confused me:
What I learned:
```

And paste your code.

### Today's mindset:

> **Real data lives in files, not inside code. Once you can read files, Python becomes a real-world tool.**

Let's go. 🔥
