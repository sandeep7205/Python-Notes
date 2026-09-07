# 🚀 Day 11 — Python CSV Module

SKM, yesterday on Day 10 you built something very close to a real data pipeline by manually splitting CSV lines with `.split(',')`.

Today we're taking the next step:

> **Why manually split strings when Python has a built-in module designed specifically for CSVs?**

Delimited data in real life can have commas inside quotes, complex delimiters, and varied row structures. Python provides the `csv` module to handle this reliably.

---

## 🎯 Today's goal

You have `expenses.csv` in your folder:

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
1. Use `csv.reader` to read rows as lists (position-based access).
2. Use `csv.DictReader` to read rows as dictionaries (column-name-based access).
3. Understand the difference between accessing data by index vs by column header name.
4. Calculate the grand total and category totals using `csv.DictReader`.

---

# ⏱️ Your 15-minute mission

### 🧠 0–3 min — Recall

Without looking at Day 10 code, answer these from memory:

1. What does `readlines()` return?
2. Why did we use `.strip()`?
3. What does `.split(',')` do?
4. Why did we use `int()` on Amount?
5. What is a dictionary?
6. What does `.items()` give you?
7. What does `+=` do?

Keep your answers short.

---

# 🔨 3–5 min — Understand `csv.reader` vs `csv.DictReader`

Yesterday you did:

```python
line.strip().split(',')
```

And mapped:
- `row[0]` → Date
- `row[1]` → Category
- `row[2]` → Amount

Python's built-in `csv` module gives you two ways to read files:

```text
expenses.csv
     │
     ├─► csv.reader()      ──► rows as LISTS        ──► row[1]
     │
     └─► csv.DictReader()  ──► rows as DICTIONARIES ──► row['Category']
```

| | `csv.reader` | `csv.DictReader` |
|---|---|---|
| **Row type** | List | Dictionary |
| **Access** | By position (`row[2]`) | By column name (`row['Amount']`) |
| **Readability** | Relies on column order | Self-documenting |

---

# 🛠️ 5–12 min — Your challenge

You already have `expenses.csv` in your `day-11` folder.

### Challenge 1 — Understand the row type

1. Open `expenses.csv` using `with open(...)`.
2. Pass the file object to `csv.reader()`.
3. Loop through the rows and print each row along with its `type()`.
4. Now open the file with `csv.DictReader()`. Print each row and its `type()`.
5. Observe: What does `DictReader` use as dictionary keys?

### Challenge 2 — Calculate the grand total

Using `csv.DictReader`:
1. Initialize `total_amount = 0`.
2. In the loop, extract `row['Amount']` and convert it with `int()`.
3. Add it to `total_amount` using `+=`.
4. Print the total amount.

### Challenge 3 — Category summary

Reuse your dictionary aggregation logic from Day 9 & Day 10:
1. Create an empty dictionary `cat_dict_amount = {}`.
2. For each row, check if the category already exists in the dictionary.
3. If not, add it; if it does, add the amount to the existing category total.
4. Print the category totals formatted cleanly:
   ```text
   Food → ₹700
   Travel → ₹550
   Shopping → ₹800
   Entertainment → ₹450
   ```

---

# ⭐ Bonus — Position vs Name

Think about this scenario:

> What happens if tomorrow someone rearranges the CSV columns to `Amount,Date,Category`?

- How would that affect your `csv.reader` code?
- How would that affect your `csv.DictReader` code?

Which approach is more robust for data engineering?

---

# 🚫 Don't do this today

Don't jump into:
* `pandas`
* Writing CSV files (`csv.writer` / `csv.DictWriter`)
* Complex exception handling

Master the basics of reading and dictionary-based row access first.

---

## 📝 Your Day 11 report

When you're finished, send:

```text
Day 11:
Time:
Habit battle:
What I built:
What confused me:
What I learned:
```

And paste your code.

### Today's mindset:

> **Position-based code breaks when columns move. Name-based code expresses meaning.**

Let's go. 🔥
