from google import genai

def call_gemini_review_api(code: str, comment: str, severity: str, language: str) -> str:
    prompt = (
        f"You are an expert, empathetic code reviewer. Given the following code and a review comment, do the following:\n"
        "1. Rewrite the comment in a genuinely empathetic, constructive, and educational way, as if you are a human mentor.\n"
        "2. Explain WHY this suggestion matters, mentioning readability, performance, or team impact as appropriate.\n"
        "3. Suggest a significant code improvement, showing a before/after code block if possible.\n"
        "4. Use Markdown formatting for all output.\n\n"
        f"Code (language: {language}):\n{code}\n\n"
        f"Review comment (severity: {severity}):\n{comment}\n"
    )
    client = genai.Client()
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

def extract_positive_feedback(code: str) -> list:
    feedback = []
    if 'def ' in code:
        feedback.append("Great use of function definitions to organize your code.")
    if 'return' in code:
        feedback.append("Good job using return statements to output results.")
    if 'import ' in code:
        feedback.append("Nice use of imports to leverage existing libraries.")
    return feedback

def find_line_for_comment(comment: str, code: str) -> str:
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
        report.append(f"### Comment {idx}\n")
        report.append(f"**Original:** {comment} {line_ref}\n")
        try:
            llm_output = call_gemini_review_api(code, comment, severity, language)
            report.append(llm_output)
        except Exception as e:
            report.append(f"_LLM error: {e}_\n")
        report.append("")
    report.append("---\n")
    return '\n'.join(report)