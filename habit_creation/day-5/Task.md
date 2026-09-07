# 🚀 Day 5 — Dictionaries and Key-Value Pairs

SKM, welcome to Day 5.

Yesterday on Day 4, you combined lists, loops, conditions, and filtering (`tech_list`, `DE_tech_list`). You started thinking about data flowing through logic.

Today we take a crucial step toward real Data Engineering.

A list is an ordered sequence indexed by numbers:

```text
index:    0        1       2
value:  Python    SQL     AWS
```

That's great for lists of items, but real-world data is labeled and structured:

```text
name → Sandeep
role → SDE-1
experience → 4.6 years
learning → Python
```

Today's focus: **Dictionaries (`dict`) and key-value pairs**.

---

## 🎯 Today's goal

By the end of today, you will:

1. Understand how Python dictionaries store structured data using key-value pairs.
2. Build a developer profile dictionary representing your professional background.
3. Access and iterate over keys and values using `.items()`.
4. Update existing keys and add new fields using direct assignment and `.update()`.
5. Combine lists and dictionaries to represent multiple records of data.

---

# ⏱️ Your 15-minute mission

### 🧠 0–3 min — Recall

Before touching any code, answer these from memory:

1. What is a list?
2. What does a `for` loop do?
3. What does `in` do?
4. What does `%` do?
5. What is the difference between `if` and `else`?

---

# 🔨 3–5 min — Understand Key-Value Pairs

In a list, you look up items by position (`list[0]`).

In a dictionary, you look up values by their **key**:

```python
developer = {
    "name": "SKM",
    "role": "SDE-1",
    "experience": "4.6 years"
}
```

Keys are like descriptive labels. Values are the data behind those labels.

To loop through both keys and values together, Python gives us `.items()`:

```python
for key, value in developer.items():
    print(f"{key}: {value}")
```

And to update a dictionary or add new keys:

```python
# Option 1: Direct assignment
developer["role"] = "Data Engineer"

# Option 2: .update() method
developer.update({"status": "Active"})
```

---

# 🛠️ 5–12 min — Your challenge

### Task 1 — Create your developer profile dictionary
Create a dictionary named `developer` representing yourself with at least 5–6 fields:
* `"name"`
* `"role"`
* `"experience"`
* `"python_experience"`
* `"currently_learning"`
* `"daily_habit"`

### Task 2 — Print all details using `.items()`
Use a `for` loop with `.items()` to iterate through `developer` and print each key and value:

```text
name: SKM
role: SDE-1 in PHP
experience: 4.6 years Continuous
...
```

### Task 3 — Update existing keys and add new keys
Explore modifying your dictionary:
1. Update `"currently_learning"` using direct key assignment (`developer['currently_learning'] = ...`).
2. Use `.update()` to update an existing key (e.g. `'experience'`).
3. Use `.update()` to add a new key that wasn't there before (e.g. `'current_day'`: `"Day 5"`).
4. Loop through and print the updated dictionary to verify your changes.

---

# ⭐ Bonus — A List of Records

In Data Engineering, datasets and database tables are conceptually a **list of dictionaries** (rows of records):

```text
developers_list (List)
 ├── Dictionary 1 → Developer Alice
 ├── Dictionary 2 → Developer Bob
 └── Dictionary 3 → Developer Clara
```

1. Create `developers_list` containing 3 dictionaries representing different developers (fields: `"name"`, `"experience"`, `"role"`).
2. Loop through the list using `enumerate(developers_list, start=1)`.
3. Inside, use a nested loop with `.items()` to print every developer's fields cleanly.

---

# ⏱️ Time rule

Your minimum commitment is **15 minutes**.
Phone physically away before you begin.
Don't rush to master everything today—focus on understanding the relationship between keys and values.

---

## 📝 Your Day 5 report

When you're done, send:

```text
Day 5:
Time:
Habit battle:
What I built:
What confused me:
What I learned:
```

And paste your code.

### Today's mindset:
> **Lists give order. Dictionaries give meaning. Together, they create structured data.** 🔥
