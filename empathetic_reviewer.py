# Helper functions for positive feedback and line referencing
def extract_positive_feedback(code: str) -> list:
    """Simple positive feedback based on code features."""
    feedback = []
    if 'def ' in code:
        feedback.append("Great use of function definitions to organize your code.")
    if 'return' in code:
        feedback.append("Good job using return statements to output results.")
    if 'import ' in code:
        feedback.append("Nice use of imports to leverage existing libraries.")
    # Add more as needed
    return feedback

def find_line_for_comment(comment: str, code: str) -> str:
    """Try to reference a line or fragment in the code related to the comment."""
    lines = code.split('\n')
    if 'docstring' in comment.lower():
        for i, line in enumerate(lines):
            if 'def ' in line:
                return f"(See line {i+1}: `{line.strip()}`)"
    if 'operator' in comment.lower():
        for i, line in enumerate(lines):
            if '+' in line or '-' in line or '*' in line or '/' in line:
                return f"(See line {i+1}: `{line.strip()}`)"
    return ""
# Empathetic Code Reviewer Core Logic

import re
from typing import Dict, List

def detect_language(code: str) -> str:
    """Detects the programming language from the code snippet."""
    if 'def ' in code or 'import ' in code:
        return 'python'
    if 'function ' in code or 'console.log' in code:
        return 'javascript'
    if '#include' in code or 'int main' in code:
        return 'c/c++'
    return 'unknown'

STYLE_GUIDES = {
    'python': '[PEP 8](https://peps.python.org/pep-0008/)',
    'javascript': '[JavaScript Style Guide](https://github.com/airbnb/javascript)',
    'c/c++': '[C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines)',
}


def empathetic_rewrite(comment: str, severity: str) -> str:
    """Rewrite the comment to be empathetic and constructive, with flexible templates."""
    templates = {
        'critical': [
            "Thank you for your effort! I noticed something that could significantly impact your code: {comment}",
            "Let's address a critical issue: {comment}"
        ],
        'major': [
            "Great progress! Here's an important suggestion: {comment}",
            "Consider this key improvement: {comment}"
        ],
        'minor': [
            "Nice job! Here's a minor improvement you could consider: {comment}",
            "Just a small tip: {comment}"
        ]
    }
    chosen = templates.get(severity, templates['minor'])
    # Pick the first template for now, can randomize or improve later
    return chosen[0].format(comment=comment)


def explain_why(comment: str) -> str:
    """Flexible explanation for why the suggestion matters."""
    # Simple keyword-based logic for demo; can be extended
    if 'docstring' in comment.lower():
        return "Adding a docstring improves code documentation and helps others understand the function's purpose."
    if 'space' in comment.lower() and 'operator' in comment.lower():
        return "Following style guidelines for spacing around operators makes code more readable."
    if 'validate' in comment.lower() or 'input' in comment.lower():
        return "Validating input types helps prevent runtime errors and makes your code more robust."
    return "This suggestion helps improve code quality, readability, or performance."


def suggest_improvement(comment: str, code: str) -> str:
    """Flexible suggestion for code improvement."""
    # Simple keyword-based logic for demo; can be extended
    if 'docstring' in comment.lower():
        return "Add a descriptive docstring at the beginning of your function."
    if 'space' in comment.lower() and 'operator' in comment.lower():
        return "Add spaces around operators, e.g., change 'a+b' to 'a + b'."
    if 'validate' in comment.lower() or 'input' in comment.lower():
        return "Add type checks or input validation to ensure correct usage."
    return "Consider revising the code as per the suggestion above."

def generate_review_report(data: Dict) -> str:
    code = data.get('code', '')
    comments = data.get('comments', [])
    language = detect_language(code)
    style_guide = STYLE_GUIDES.get(language, None)
    report = ["# Empathetic Code Review\n"]
    report.append("## Code Snippet\n")
    report.append(f"```{language}\n{code}\n```")
    # Positive feedback section
    positives = extract_positive_feedback(code)
    if positives:
        report.append("\n## Positive Feedback\n")
        for pos in positives:
            report.append(f"- {pos}")
    report.append("\n## Review Comments\n")
    for idx, item in enumerate(comments, 1):
        comment = item.get('comment', '')
        severity = item.get('severity', 'minor')
        line_ref = find_line_for_comment(comment, code)
        report.append(f"### Comment {idx}\n")
        report.append(f"**Original:** {comment} {line_ref}\n")
        report.append(f"**Empathetic Rewrite:** {empathetic_rewrite(comment, severity)}\n")
        report.append(f"**Why:** {explain_why(comment)}\n")
        report.append(f"**Suggested Improvement:** {suggest_improvement(comment, code)}\n")
        report.append("")
    report.append("---\n")
    report.append("## Summary\n")
    # Dynamic summary based on severities
    severities = [item.get('severity', 'minor') for item in comments]
    if 'critical' in severities:
        summary = "You addressed some critical issues—great learning opportunity! Keep up the effort and always review for robustness."
    elif 'major' in severities:
        summary = "You handled some important suggestions well. Keep refining your code for even better quality!"
    else:
        summary = "Your code is in great shape! Just a few minor improvements to consider."
    if positives:
        summary += " Also, excellent work on the following: " + ", ".join(positives)
    report.append(summary + "\n")
    if style_guide:
        report.append(f"Refer to the official style guide for more details: {style_guide}\n")
    report.append("Thank you for your hard work and dedication to improvement! 🚀\n")
    return '\n'.join(report)
    """Simple positive feedback based on code features."""
    feedback = []
    if 'def ' in code:
        feedback.append("Great use of function definitions to organize your code.")
    if 'return' in code:
        feedback.append("Good job using return statements to output results.")
    if 'import ' in code:
        feedback.append("Nice use of imports to leverage existing libraries.")
    # Add more as needed
    return feedback
    """Try to reference a line or fragment in the code related to the comment."""
    lines = code.split('\n')
    if 'docstring' in comment.lower():
        for i, line in enumerate(lines):
            if 'def ' in line:
                return f"(See line {i+1}: `{line.strip()}`)"
    if 'operator' in comment.lower():
        for i, line in enumerate(lines):
            if '+' in line or '-' in line or '*' in line or '/' in line:
                return f"(See line {i+1}: `{line.strip()}`)"
    return ""
    """Simple positive feedback based on code features."""
    feedback = []
    if 'def ' in code:
        feedback.append("Great use of function definitions to organize your code.")
    if 'return' in code:
        feedback.append("Good job using return statements to output results.")
    if 'import ' in code:
        feedback.append("Nice use of imports to leverage existing libraries.")
    # Add more as needed
    return feedback
    """Try to reference a line or fragment in the code related to the comment."""
    lines = code.split('\n')
    if 'docstring' in comment.lower():
        for i, line in enumerate(lines):
            if 'def ' in line:
                return f"(See line {i+1}: `{line.strip()}`)"
    if 'operator' in comment.lower():
        for i, line in enumerate(lines):
            if '+' in line or '-' in line or '*' in line or '/' in line:
                return f"(See line {i+1}: `{line.strip()}`)"
    return ""
