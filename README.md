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



# Empathetic Code Reviewer (Mentor-Bot)

## 🚀 Overview
Mentor-Bot is a hackathon-ready, AI-powered code reviewer that transforms code review comments into empathetic, constructive, and educational feedback. It uses Google Gemini LLM for natural, human-like suggestions and always produces a professional Markdown report—perfect for impressing judges and helping teams grow.

## ✨ Features
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
- `empathetic_reviewer.py` — Gemini-powered review logic
- `sample_input.json` — Example input file
- `requirements.txt` — Python requirements
- `README.md` — Documentation and instructions

## 🧠 How It Works
1. Reads a code snippet and review comments from a JSON file.
2. Uses Gemini LLM to generate empathetic, educational, and actionable feedback for each comment.
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
- `google-genai` (for Gemini LLM)

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
