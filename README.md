# Empathetic Code Reviewer

## Overview
This tool transforms code review comments into empathetic, constructive, and educational feedback. It generates a Markdown report with rewrites, explanations, suggestions, and a summary, and links to relevant style guides based on the detected programming language.

## Features
- Empathetic rewrites of review comments
- Severity-based tone adjustment
- Technical explanations for each suggestion
- Suggested code improvements
- Automatic language detection and style guide linking
- Holistic summary and encouragement

## Usage
1. Place your code and comments in a JSON file (see `sample_input.json`).
2. Run the tool:
   ```
   python main.py sample_input.json
   ```
3. The Markdown report will be printed to the console.

## Example Input
```
{
  "code": "def add(a, b):\nreturn a+b\n",
  "comments": [
    { "comment": "No space around operators.", "severity": "minor" },
    { "comment": "Function lacks a docstring.", "severity": "major" },
    { "comment": "No input validation for types.", "severity": "critical" }
  ]
}
```


## Example Output
```
# Empathetic Code Review

## Code Snippet

```python
def add(a, b):
return a+b
```

## Positive Feedback

- Great use of function definitions to organize your code.
- Good job using return statements to output results.

## Review Comments

### Comment 1

**Original:** No space around operators. (See line 2: `return a+b`)

**Empathetic Rewrite:** Nice job! Here's a minor improvement you could consider: No space around operators.

**Why:** Following style guidelines for spacing around operators makes code more readable.

**Suggested Improvement:** Add spaces around operators, e.g., change 'a+b' to 'a + b'.

### Comment 2

**Original:** Function lacks a docstring. (See line 1: `def add(a, b):`)

**Empathetic Rewrite:** Great progress! Here's an important suggestion: Function lacks a docstring.

**Why:** Adding a docstring improves code documentation and helps others understand the function's purpose.

**Suggested Improvement:** Add a descriptive docstring at the beginning of your function.

### Comment 3

**Original:** No input validation for types.

**Empathetic Rewrite:** Thank you for your effort! I noticed something that could significantly impact your code: No input validation for types.

**Why:** Validating input types helps prevent runtime errors and makes your code more robust.

**Suggested Improvement:** Add type checks or input validation to ensure correct usage.

---

## Summary

You addressed some critical issues—great learning opportunity! Keep up the effort and always review for robustness. Also, excellent work on the following: Great use of function definitions to organize your code., Good job using return statements to output results.
Refer to the official style guide for more details: [PEP 8](https://peps.python.org/pep-0008/)

Thank you for your hard work and dedication to improvement! 🚀

## Project Structure

- `main.py` — Entry point, loads JSON and prints the Markdown report
- `empathetic_reviewer.py` — Core logic for review, feedback, and suggestions
- `sample_input.json` — Example input file
- `requirements.txt` — Python requirements (none needed for base version)
- `README.md` — Documentation and instructions

## How it Works

1. Reads a code snippet and review comments from a JSON file.
2. Detects the programming language and links to the relevant style guide.
3. Generates empathetic, educational, and actionable feedback for each comment.
4. Highlights positive aspects of the code and references specific lines where possible.
5. Outputs a professional Markdown report.

## Repository

GitHub: https://github.com/riyamoun1310/Mentor-Bot

---

## Stand-Out Features
- Context-aware tone
- Style guide links (e.g., PEP 8 for Python)
- Holistic summary and encouragement

## Requirements
- Python 3.7+

## Customization
You can extend `empathetic_reviewer.py` to improve language detection, explanations, or code suggestions.
