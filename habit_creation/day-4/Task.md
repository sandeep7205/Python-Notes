# 🚀 Day 4 — Lists + Data Processing

SKM, welcome to Day 4!

In the first three days, you built:
* Variables to store data (Day 1)
* Conditionals to make decisions (Day 2)
* Loops to handle repetition (Day 3)

Today, we take our first real step into **Data Engineering**:

```text
Raw Data
   ↓
Filter
   ↓
Process / Calculate
   ↓
Output
```

Data engineering isn't just about printing values; it's about inspecting data, filtering out what doesn't belong, and transforming what remains.

---

## 🎯 Today's goal

Process lists of data using loops and conditionals: filter tech stacks by category and learning status, and filter numbers based on thresholds and mathematical properties.

---

# ⏱️ Your 15-minute mission

### 🧠 0–3 min — Recall

Without looking at your previous code, answer these:

1. What is a list?
2. What does a `for` loop do?
3. What does `if` do?
4. What does `in` do?
5. What does `enumerate()` give you?

---

# 🔨 3–5 min — The Data Processing Pipeline

In data engineering, pipelines frequently follow this pattern:

```text
Collection of items (List)
         ↓
Check each item against criteria (`in`, `>`, `==`)
         ↓
Process matching items (Transform / Accumulate)
         ↓
Final Result
```

Using `in` allows you to test for membership in reference sets, while comparison operators let you filter numeric thresholds.

---

# 🛠️ 5–12 min — Your challenge

Complete two data processing exercises:

### Part 1: Filter and Classify a Tech Stack
1. Create a master list of technologies:
   ```python
   tech_list = ['Python', 'SQL', 'AWS', 'Docker', 'Git', 'JavaScript', 'HTML', 'CSS']
   ```
2. Create reference lists:
   ```python
   DE_tech_list = ['Python', 'SQL', 'AWS', 'Docker']
   learning_list = ['Python', 'SQL']
   ```
3. Loop through `tech_list`:
   * Filter only the technologies that belong to `DE_tech_list`.
   * For each DE technology, check if it's in `learning_list` (status: `"Learning"`) or not (status: `"Later"`).
   * Print or build an output string showing the classified technologies.

### Part 2: Number Filtering (Thresholds)
1. Create a list of numbers:
   ```python
   num_list = [5, 12, 3, 20, 8, 15, 2]
   ```
2. Set a boundary threshold:
   ```python
   boundary = 10
   ```
3. Loop through `num_list` and print only the numbers that are **greater than the boundary**.

---

# ⭐ Bonus — Even Number Filter

Add another data filtering pass on `num_list`:
* Loop through `num_list` and identify all **even numbers**.
* *Hint:* Use the modulo operator `%` (`num % 2 == 0`).
* Print a clear message for each even number found.

---

# ⏱️ Time rule

Your minimum commitment is **15 minutes**.
Focus on the logic flow: list → loop → condition → output.
If you finish in 15 minutes, stop and enjoy your evening.

---

## 📝 Your Day 4 report

When you're done, record:

```text
Day 4:
Time:
Habit battle:
What I built:
What confused me:
What I learned:
```

And paste your code.

### Today's mindset:

> **"Data Engineering is about taking raw collections, applying rules, and extracting clean, meaningful output."** 🔥
