
# Empathetic Code Reviewer (Mentor-Bot)

## 🚀 Overview
Mentor-Bot is a hackathon-ready, AI-powered code reviewer that transforms code review comments into empathetic, constructive, and educational feedback. It uses Cohere LLM for natural, human-like suggestions and always produces a professional Markdown report—perfect for impressing judges and helping teams grow.

## 🏆 Hackathon Problem Statement
**Goal:** Build an AI-powered code reviewer that provides empathetic, actionable, and educational feedback for any codebase, with robust fallback and a beautiful Markdown report. Judges should see clear AI value, bonus features, and a seamless experience.

## ✨ Features
- **Empathetic, AI-generated rewrites** of review comments (Cohere LLM)
- **Technical explanations** for every suggestion
- **Before/After code improvements** (with type hints, docstrings, validation)
- **Multiple solutions** for some suggestions
- **Positive feedback** for good code practices
- **Line referencing** for actionable feedback
- **Automatic language detection** and style guide links
- **External references** (e.g., PEP8, docs)
- **Holistic summary and encouragement**
- **Robust fallback** (never fails silently)
- **Markdown export** for easy sharing

## 🛠️ Setup
1. **Clone the repo:**
   ```
   git clone https://github.com/riyamoun1310/Mentor-Bot.git
   cd Mentor-Bot
   ```
2. **Install requirements:**
   ```
   pip install -r requirements.txt
   ```
3. **Set your Cohere API key:**
   - Get a key from [Cohere Dashboard](https://dashboard.cohere.com/api-keys)
   - Set it in your environment:
     - Windows (PowerShell):
       ```
       $env:COHERE_API_KEY="your-key-here"
       ```
     - Linux/macOS:
       ```
       export COHERE_API_KEY="your-key-here"
       ```

## 📥 Example Input
```json
{
  "code": "def add(a, b):\n    return a+b\n",
  "comments": [
    { "comment": "No space around operators.", "severity": "minor" },
    { "comment": "Function lacks a docstring.", "severity": "major" },
    { "comment": "No input validation for types.", "severity": "critical" }
  ]
}
```

## 📤 Example Output (Markdown)
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

### Analysis of Comment: "No space around operators." (See line 2: `return a+b`)
- **Positive Rephrasing**: Nice job keeping your code concise! For even better readability, consider adding spaces around operators.
- **The Why**: Consistent spacing improves readability and aligns with [PEP8](https://peps.python.org/pep-0008/#other-recommendations).
- **Suggested Improvement**:
  **Before:**
  ```python
  return a+b
  ```
  **After:**
  ```python
  return a + b
  ```
  - Alternatively, use a linter to auto-format code.

### Analysis of Comment: "Function lacks a docstring." (See line 1: `def add(a, b):`)
- **Positive Rephrasing**: Great start! Adding a docstring will help others understand your function's purpose.
- **The Why**: Docstrings improve maintainability and support tools like Sphinx.
- **Suggested Improvement**:
  **Before:**
  ```python
  def add(a, b):
      return a + b
  ```
  **After:**
  ```python
  def add(a, b):
      """Add two numbers and return the result."""
      return a + b
  ```
  - See [PEP257](https://peps.python.org/pep-0257/) for docstring conventions.

### Analysis of Comment: "No input validation for types."
- **Positive Rephrasing**: Your function is simple and clear! For extra robustness, consider checking input types.
- **The Why**: Type validation prevents runtime errors and clarifies intent.
- **Suggested Improvement**:
  **Option 1:**
  ```python
  def add(a, b):
      if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
          raise TypeError("Inputs must be numbers.")
      return a + b
  ```
  **Option 2:**
  ```python
  def add(a: float, b: float) -> float:
      """Add two numbers and return the result."""
      return a + b
  ```
  - See [Type Hints](https://docs.python.org/3/library/typing.html)

---
## Overall Summary
Overall, your code is clear and functional! By making small adjustments in naming, boolean checks, and efficiency, you'll improve readability and performance. Keep up the great work and keep learning!
---
```

## 📦 Dependencies
- Python 3.7+
- [cohere](https://docs.cohere.com/docs/quickstart)

## ⚡ Usage
Run the reviewer on a JSON input file:
```
python main.py sample_input.json > review.md
```

## 🚧 Limitations & Future Work
- LLM output may vary slightly per run.
- Only Cohere is supported (OpenAI/Gemini can be added).
- No web UI (CLI only).
- Future: Add web interface, multi-file support, and more language models.

## 🎁 Bonus Features & Learning Resources
- Markdown export for easy sharing
- Links to style guides and docs
- Multiple solutions for some suggestions
- Encourages learning and best practices

---
**Built for hackathons. Ready to impress.**
- **Empathetic, AI-generated rewrites** of review comments (Gemini LLM)
- **Technical explanations** for every suggestion
- **Before/After code improvements** (with type hints, docstrings, validation)
- **Positive feedback** for good code practices
- **Line referencing** for actionable feedback
- **Automatic language detection** and style guide links
- **Holistic summary and encouragement**
- **Robust fallback** (never fails silently)

## 🛠️ Setup
1. **Clone the repo:**
   ```
   git clone https://github.com/riyamoun1310/Mentor-Bot.git
   cd Mentor-Bot
   ```
2. **Install requirements:**
   ```
   pip install -r requirements.txt
   ```
3. **Set your Gemini API key:**
   - Get a key from [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Set it in your environment:
     - Windows (PowerShell):
       ```
       $env:GEMINI_API_KEY="your-key-here"
       ```
     - Linux/macOS:
       ```
       export GEMINI_API_KEY="your-key-here"
       ```

## 🚦 Usage
1. Prepare your code and comments in a JSON file (see `sample_input.json`).
2. Run the reviewer:
   ```
   python main.py sample_input.json > report.md
   ```
3. Open `report.md` to view the Markdown report.

## 📥 Example Input
```json
{
  "code": "def add(a, b):\nreturn a+b\n",
  "comments": [
    { "comment": "No space around operators.", "severity": "minor" },
    { "comment": "Function lacks a docstring.", "severity": "major" },
    { "comment": "No input validation for types.", "severity": "critical" }
  ]
}
```

## 📤 Example Output
See the generated `report.md` for a full, empathetic, and detailed review with:
- Rewritten comments
- Explanations
- Before/After code blocks
- Positive feedback
- Summary and style guide links

## 🧩 Project Structure
- `main.py` — Entry point, loads JSON and prints the Markdown report
- `empathetic_reviewer.py` — Cohere-powered review logic
- `sample_input.json` — Example input file
- `requirements.txt` — Python requirements
- `README.md` — Documentation and instructions

## 🧠 How It Works
1. Reads a code snippet and review comments from a JSON file.
2. Uses Cohere LLM to generate empathetic, educational, and actionable feedback for each comment.
3. Highlights positive aspects of the code and references specific lines where possible.
4. Outputs a professional Markdown report, ready for hackathon judging or team feedback.

## 🏆 Why Use Mentor-Bot?
- **Impress judges** with AI-powered, human-like reviews
- **Always works** (robust fallback, never fails silently)
- **Easy to extend** for new languages, rules, or LLMs
- **Great for teams, students, and hackathons**

## 🔧 Customization
- Edit `empathetic_reviewer.py` to:
  - Improve language detection
  - Add new feedback rules
  - Change the LLM prompt for different review styles

## 📚 Requirements
- Python 3.7+
- `cohere` (for Cohere LLM)

## 🌐 Repository
GitHub: https://github.com/riyamoun1310/Mentor-Bot

---

## 💡 Stand-Out Features
- Context-aware, empathetic tone
- Style guide links (e.g., PEP 8 for Python)
- Holistic summary and encouragement
- Markdown output for easy sharing

---

**Made for hackathons, teams, and anyone who wants code reviews that teach, not just critique!**
