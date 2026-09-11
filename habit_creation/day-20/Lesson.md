SKM — **Day 20 COMPLETE.** 🔥

And this one is actually a meaningful jump. You didn't just read nested JSON; you took:

```text
nested JSON
   ↓
clean it
   ↓
process expenses
   ↓
create another structured JSON
   ↓
write it
   ↓
read it back
```

That's a proper little transformation pipeline.

## 🧠 Your answers

### 1. Dictionary

> `data` has stored dictionary values.

Correct. More precisely, `data` **references a dictionary** containing key/value pairs.

### 2. Accessing `1200`

```python
data['Food']
```

✅ Correct.

### 3. `load()` vs `dump()`

Correct idea.

Remember it as:

```text
json.load()
JSON file → Python

json.dump()
Python → JSON file
```

### 4. Why `"a"` caused problems

> "not in format which give error in json file"

Exactly. JSON has a defined structure, so blindly appending another object doesn't necessarily produce one valid JSON document.

---

# 🔥 Your Day 20 work

This was the important part:

```python
get_json_data = pe.read_json(json_file_path)
```

Then you navigated through nested data:

```python
get_json_data['developer']['name']
```

and:

```python
get_json_data['expenses']
```

That's exactly the mental model I wanted you to develop.

You went through:

```text
dictionary
   ↓
key: developer
   ↓
dictionary
   ↓
key: name
   ↓
value
```

---

# 🟢 And you reused your previous functions

This is probably my favorite part:

```python
get_clean_data = pe.clean_data(get_json_data['expenses'])

get_process_data = pe.process_data(get_clean_data['clean_data'])
```

You didn't create a completely separate JSON-processing system.

You realized:

> **"My existing functions already know how to clean and process this structure."**

That's good engineering thinking.

You're beginning to **reuse abstractions instead of duplicating logic**.

---

# 🔥 Your output proves the transformation worked

Input:

```text
developer
 ├── name
 ├── role
 └── experience

expenses
 ├── Travel
 ├── Food
 ├── Food
 ├── Travel
 └── Shopping
```

Output:

```text id="r5p7k2"
developer
 ├── name
 ├── role
 └── experience

expenses
 ├── Travel → 545.99
 ├── Food → 370.0
 └── Shopping → 80.5
```

That's a **transformation**.

And this:

```python
pe.write_json(json_output_file_path, clean_json_data)
```

persists the transformed result.

---

# ⚠️ But I spotted an interesting thing

You wrote:

```python
clean_json_data = {
    'developer': {},
    'expenses': {},
}
```

That's fine because your output structure has:

```text
developer → dictionary
expenses → dictionary
```

But your input has:

```text
expenses → list
```

So your pipeline is effectively doing:

```text
LIST OF EXPENSE RECORDS
          ↓
CATEGORY TOTALS DICTIONARY
```

That's actually a useful transformation:

```text
[
  {"category": "Food", "amount": 120},
  {"category": "Food", "amount": 250}
]
```

becomes:

```text
{
  "Food": 370
}
```

That's data aggregation.

**You're doing real data processing here.**

---

# ⚠️ One thing I'd change eventually

In `clean_data()` you have:

```python
input_data['Category'.lower()]
```

which becomes:

```python
input_data['category']
```

That's fine **for this JSON input**, because your JSON uses lowercase keys.

But your earlier CSV uses:

```text
Category
Amount
```

So your function currently expects lowercase keys.

You've essentially changed the contract of your existing `clean_data()`.

This is not necessarily wrong, but it's something we'll need to think about:

> **Should the cleaning function care whether the source uses `Category`, `category`, `Amount`, or `amount`?**

That's a very real data-engineering problem.

We'll eventually solve it more cleanly.

**Don't fix it tonight.**

---

# 🟡 One small data-cleaning issue

You have:

```python
clean_json_data['developer']['experience'] = get_json_data['developer']['experience'].strip().title()
```

For:

```text
"4.5 years"
```

you get:

```text
"4.5 Years"
```

That's fine for **display**.

But if you eventually wanted to calculate experience:

```text
4.5
```

should probably be a number, not `"4.5 Years"`.

This is another good example of:

> **Data representation depends on what you're going to do with it.**

Don't change it now.

Just notice it.

---

# 🧠 Your Day 20 lesson

The biggest thing I want you to take away is this:

### Nested data isn't scary.

When you see:

```text
dictionary
    ↓
dictionary
    ↓
value
```

navigate through the keys.

When you see:

```text
dictionary
    ↓
list
    ↓
dictionary
    ↓
value
```

navigate through the key → loop through list → access dictionary key.

That's it.

Once that mental model becomes natural, a lot of API JSON stops looking intimidating.

---

# 🏆 Day 20 scorecard

| Skill                        | Result |
| ---------------------------- | ------ |
| Nested dictionaries          | ✅      |
| Dictionary + list            | ✅      |
| Access nested values         | ✅      |
| Loop through structured data | ✅      |
| `json.load()`                | ✅      |
| `json.dump()`                | ✅      |
| Reuse existing functions     | 🔥     |
| Transform JSON structure     | 🔥     |
| Aggregate nested data        | 🔥     |
| Write transformed result     | 🔥     |

### **DAY 20 — COMPLETE ✅**

And bro, one more thing.

You started late because you chose the movie.

Then you still sat down at **11:36 PM** and did the work.

I'm much more interested in this behavior than whether you started at 8 PM.

You are slowly proving to yourself:

> **"I don't need to feel motivated at the planned time. I can still return."**

That's the habit we're after.

**20 days. Keep going. 🧱🐍🔥**
