import pandas as pd

def import_questions_from_excel(file_path):
    df = pd.read_excel(file_path)

    # Normalize column names
    df.columns = df.columns.str.strip().str.lower()

    questions = []
    for i, row in df.iterrows():
        try:
            correct_index = int(row['correct answer index']) - 1
            if correct_index not in range(4):
                raise ValueError("Index out of range")
        except (ValueError, TypeError):
            print(f"Row {i}: Invalid correct answer index → {row['correct answer index']}")
            correct_index = 0  # Default to first answer

        correct_feedback = row.get('correct feedback', '').strip()

        questions.append({
            'question': row['question text'],
            'answers': [
                row['answer 1'],
                row['answer 2'],
                row['answer 3'],
                row['answer 4']
            ],
            'correct_index': correct_index,
            'correct_feedback': correct_feedback,
            'incorrect_feedback': row.get('incorrect feedback', '').strip()
        })
    return questions
