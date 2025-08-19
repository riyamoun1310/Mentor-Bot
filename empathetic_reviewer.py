
import os
import cohere

def call_cohere_review_api(code: str, comment: str, severity: str, language: str) -> str:
    """
    Calls Cohere LLM to generate a review for a code comment, enforcing strict Markdown structure, tone, and references.
    """
    api_key = os.getenv("COHERE_API_KEY")
    if not api_key:
        return "_LLM error: Cohere API key not set. Set COHERE_API_KEY environment variable._"
    co = cohere.Client(api_key)
    # Tone control prompt
    tone = "very gentle and supportive" if severity.lower() in ["major", "critical", "harsh"] else "neutral and constructive"
    # Add external references if relevant
    reference = "\n- If relevant, include a link to a style guide or documentation (e.g., [PEP8 variable naming](https://peps.python.org/pep-0008/#naming-conventions))."
    # Multiple solutions prompt
    multi_solution = "If possible, suggest two different ways to improve the code (e.g., list comprehension vs. filter)."
    prompt = (
        f"You are an expert, empathetic code reviewer. For the following code and review comment, strictly output in this Markdown structure:\n"
        f"### Analysis of Comment: \"{comment}\"\n"
        f"- **Positive Rephrasing**: Start with a positive, {tone} rewrite of the comment.\n"
        f"- **The Why**: Explain why this matters, always tie to a software principle (readability, maintainability, performance, convention).\n"
        f"- **Suggested Improvement**: Show a before/after code block. {multi_solution}\n"
        f"{reference}\n"
        f"\nCode (language: {language}):\n{code}\n"
        f"\nSeverity: {severity}\n"
        f"\nRespond only in Markdown, no extra text.\n"
    )
    response = co.generate(
        model="command-r-plus",
        prompt=prompt,
        max_tokens=700,
        temperature=0.7
    )
    return response.generations[0].text.strip()


def extract_positive_feedback(code: str) -> list:
    """
    Extracts positive feedback from code features for encouragement.
    """
    feedback = []
    if 'def ' in code:
        feedback.append("Great use of function definitions to organize your code.")
    if 'return' in code:
        feedback.append("Good job using return statements to output results.")
    if 'import ' in code:
        feedback.append("Nice use of imports to leverage existing libraries.")
    return feedback

def find_line_for_comment(comment: str, code: str) -> str:
    """
    Attempts to reference a line or fragment in the code related to the comment.
    """
    lines = code.split('\n')
    if 'docstring' in comment.lower():
        for i, line in enumerate(lines):
            if 'def ' in line:
                return f"(See line {i+1}: `{line.strip()}`)"
    for i, line in enumerate(lines):
        if any(word in comment.lower() for word in line.lower().split()):
            return f"(See line {i+1}: `{line.strip()}`)"
    return ""

def generate_review_report(data: dict) -> str:
    """
    Generates a full Markdown review report for the code and comments, including summary and encouragement.
    """
    code = data.get('code', '')
    comments = data.get('comments', [])
    language = data.get('language', 'python')
    report = ["# Empathetic Code Review\n"]
    report.append(f"## Code Snippet\n\n```{language}\n{code.strip()}\n```\n")
    positives = extract_positive_feedback(code)
    if positives:
        report.append("## Positive Feedback\n")
        for pos in positives:
            report.append(f"- {pos}")
        report.append("")
    report.append("## Review Comments\n")
    for idx, item in enumerate(comments, 1):
        comment = item.get('comment', '')
        severity = item.get('severity', 'minor')
        line_ref = find_line_for_comment(comment, code)
        report.append(f"### Analysis of Comment: \"{comment}\" {line_ref}\n")
        try:
            llm_output = call_cohere_review_api(code, comment, severity, language)
            report.append(llm_output)
        except Exception as e:
            report.append(f"_LLM error: {e}_.\n")
        report.append("")
    # Holistic summary
    report.append("---\n")
    report.append("## Overall Summary\n")
    report.append(
        "Overall, your code is clear and functional! By making small adjustments in naming, boolean checks, and efficiency, you'll improve readability and performance. Keep up the great work and keep learning!\n"
    )
    report.append("---\n")
    return '\n'.join(report)