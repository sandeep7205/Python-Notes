# 🚀 Day 6 — Data Processing with Structured Data

SKM, you've conquered variables, conditions, loops, lists, and dictionaries.

Yesterday on Day 5, you discovered how dictionaries give meaning to data and created your first list of dictionaries.

Today is a milestone: you transition from **learning Python syntax** to **processing real data**.

In Data Engineering, your core workflow is:

```text
Raw Dataset
     ↓
Inspect / Iterate
     ↓
Filter Records
     ↓
Aggregate / Calculate
     ↓
Output / Insights
```

Today you will build your first mini data processing pipeline using structured expense records.

---

## 🎯 Today's goal

By the end of today, you will:

1. Work with a list of dictionaries representing real-world expense records.
2. Iterate through records and inspect individual fields.
3. Calculate the overall total expense using an accumulator pattern.
4. Filter records by category (e.g. "Food") and aggregate using `sum()`.
5. Filter transactions based on a numeric condition (e.g. expenses > ₹200).

---

# ⏱️ Your 15-minute mission

### 🧠 0–3 min — Recall

Before touching code, answer these from memory:

1. What is a dictionary?
2. What does `.items()` do?
3. What does a `for` loop do?
4. What does `in` do?
5. What does `%` do?

---

# 🔨 3–5 min — The Data Processing Flow

Think about the structure of your data:

```text
expenses (List)
 ├── {"Date": "Monday", "Category": "Food", "Amount": 250}
 ├── {"Date": "Monday", "Category": "Travel", "Amount": 100}
 ├── {"Date": "Tuesday", "Category": "Food", "Amount": 300}
 └── ...
```

When you loop over `expenses`:
Each item in the loop is a dictionary representing a single record.

To aggregate totals, we use an **accumulator**:

```python
total = 0
for expense in expenses:
    total += expense['Amount']
```

To isolate a category, we inspect each record before aggregating:

```text
All Records (6 rows)
     ↓  filter: Category == 'Food'
[250, 300, 150]
     ↓  sum()
Total Food: 700
```

This pattern of **Inspect → Filter → Aggregate** is at the heart of all data pipelines.

---

# 🛠️ 5–12 min — Your challenge

### Task 1 — Create the expense dataset
Create a list called `expenses` containing 5–6 dictionaries representing daily expenses. Each dictionary must have:
* `"Date"` (e.g., `"Monday"`, `"Tuesday"`, `"Wednesday"`, `"Thursday"`)
* `"Category"` (e.g., `"Food"`, `"Travel"`, `"Shopping"`, `"Entertainment"`)
* `"Amount"` (e.g., `250`, `100`, `300`, `800`, `150`, `450`)

### Task 2 — Inspect and print every expense
Use a `for` loop to iterate through `expenses` and print each item:

```text
Food → 250
Travel → 100
Food → 300
...
```

### Task 3 — Calculate total expenses
Inside the loop, accumulate the total amount spent across all categories into a variable `total_amount`.
Print the total:

```text
Total Amount = 2050
```

### Task 4 — Filter by category ("Food") and use `sum()`
Calculate the total amount spent on **Food** only:
* When `expense['Category'] == 'Food'`, collect the amount into a list `total_food_amount`.
* Use Python's built-in `sum()` function on that list to calculate and print:

```text
Total Food Amount = 700
```

---

# ⭐ Bonus — Threshold Filtering

In data engineering, detecting high-value transactions is common:
* Write another loop with a condition to filter and print only expenses where `Amount` is **greater than 200**:

```text
Food → 250
Food → 300
Shopping → 800
Entertainment → 450
```

---

# ⚠️ Watch out for PHP habits!

In Python, appending to a list is done via `.append()`:

```python
total_food_amount.append(expense['Amount'])   # ✅ Python
# total_food_amount[] = ...                  # ❌ PHP syntax (causes SyntaxError)
```

Also notice: if amounts are already integers (`250`), you don't need `int(expense['Amount'])`. Python already knows it's an integer!

---

# ⏱️ Time rule

Your minimum commitment is **15 minutes**.
Phone physically away before you begin.
If you finish in 15 minutes, stop. If you're in the flow, continue.

---

## 📝 Your Day 6 report

When you're done, send:

```text
Day 6:
Time:
Habit battle:
What I built:
What confused me:
What I learned:
```

And paste your code.

### Today's mindset:
> **You're no longer just learning syntax. You are inspecting, filtering, and aggregating structured data.** 🔥
