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
See the console output after running the tool.

## Stand-Out Features
- Context-aware tone
- Style guide links (e.g., PEP 8 for Python)
- Holistic summary and encouragement

## Requirements
- Python 3.7+

## Customization
You can extend `empathetic_reviewer.py` to improve language detection, explanations, or code suggestions.
