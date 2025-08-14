# Empathetic Code Reviewer



import json
import sys
from empathetic_reviewer import generate_review_report

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_json_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    report = generate_review_report(data)
    print(report)

if __name__ == "__main__":
    main()
