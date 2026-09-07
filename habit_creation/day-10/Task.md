# 🚀 Day 10 — CSV Manual Parsing

SKM, yesterday on Day 9 you built a dynamic frequency counter using a dictionary.

Up until now, your files contained only a single piece of information per line (just a category name).

In the real world, data rarely comes as a single column. Data comes in tables and CSVs (Comma-Separated Values) with multiple columns:

```text
Date,Category,Amount
Monday,Food,250
Monday,Travel,100
...
```

Today we take our first step into **multi-column data processing**:

> **Reading and parsing CSV data manually before learning automated tools.**

---

## 🎯 Today's goal

You have `expenses.csv` in your `day-10` folder:

```text
Date,Category,Amount
Monday,Food,250
Monday,Travel,100
Tuesday,Food,300
Tuesday,Shopping,800
Wednesday,Food,150
Thursday,Entertainment,450
Thursday,Travel,450
```

By the end of today, you will:
1. Open and read a CSV file line by line.
2. Separate the header row from the data rows.
3. Split each line using `.split(',')` and extract Date, Category, and Amount.
4. Convert Amount from string to integer (`int()`).
5. Calculate the grand total of all expenses.
6. Filter and print expenses where the amount is greater than ₹300.
7. Build dynamic aggregations: total amount spent per **Category** and per **Date**.

---

# ⏱️ Your 15-minute mission

### 🧠 0–3 min — Recall

Before touching code, answer these from memory:

1. What does `readlines()` return?
2. Why do we use `.strip()`?
3. What is a dictionary?
4. What does `+= 1` do?
5. What does `.items()` give you?
6. What does `.append()` do?
7. What does a function do?

Keep your answers short.

---

# 🔨 3–5 min — Understand Manual CSV Parsing

When you read a line like `"Monday,Food,250\n"`:

```text
"Monday,Food,250\n"
         │
      .strip()          ──► "Monday,Food,250"
         │
     .split(',')        ──► ["Monday", "Food", "250"]
         │
  Extract fields        ──► Date: "Monday"
                        ──► Category: "Food"
                        ──► Amount: int("250") → 250
```

Notice two critical things:
1. The first line of a CSV is the **header** (`Date,Category,Amount`), not data! We must handle or skip it so it doesn't break calculations.
2. All values read from a text or CSV file start as **strings**. You must convert numeric fields with `int()` before calculating totals.

---

# 🛠️ 5–12 min — Your challenge

You already have `expenses.csv` in your `day-10` folder.

### Challenge 1 — Read and parse the CSV

1. Open `expenses.csv` and read all lines using `.readlines()`.
2. Extract the header line (the first line) and separate it from the data rows.
3. For each data row:
   - Remove the trailing newline using `.strip()`.
   - Split the row by commas using `.split(',')`.
   - Extract `date = split_content[0]`, `category = split_content[1]`, and convert `amount = int(split_content[2])`.

### Challenge 2 — Running total & Filtering

1. Accumulate a `total` amount across all records.
2. Filter: If `amount > 300`, print the expense (e.g. `Shopping → ₹800`).

### Challenge 3 — Dynamic Aggregations (Category & Date)

Instead of just counting frequencies, aggregate the actual **amounts spent**:

1. **Category aggregation**:
   - Create an empty dictionary `things_dict_summary = {}`.
   - For each row, if the category is not yet in the dictionary, initialize it with `amount`.
   - If it already exists, add `amount` to the category's running total.

2. **Date aggregation**:
   - Create an empty dictionary `date_dict_summary = {}`.
   - For each row, aggregate `amount` by `date`.

3. Print the formatted breakdowns:
   ```text
   Category Breakdown:
   Food → ₹700
   Travel → ₹550
   Shopping → ₹800
   Entertainment → ₹450

   Daily Breakdown:
   Monday → ₹350
   Tuesday → ₹1100
   Wednesday → ₹150
   Thursday → ₹900

   Total → ₹2500
   ```

---

# ⭐ Bonus — The limitations of manual `.split(',')`

Think about this scenario:

> What happens if an expense description in a CSV contains a comma inside quotes, like `"Dinner, with team",450`?
> What will `.split(',')` do to that row?

Notice why manual string splitting has limitations, and why Data Engineers eventually use specialized CSV tools!

---

# 🚫 Don't do this today

Don't jump into:
* Python's built-in `csv` module (that is coming tomorrow in Day 11!)
* `pandas`
* Writing modified data back to disk

Master the manual mechanics of parsing and aggregating first.

---

## 📝 Your Day 10 report

When you're finished, send:

```text
Day 10:
Time:
Habit battle:
What I built:
What confused me:
What I learned:
```

And paste your code.

### Today's mindset:

> **A CSV is just text with delimiters. Once you understand how to slice and convert it manually, automated tools will make complete sense.**

Let's go. 🔥
