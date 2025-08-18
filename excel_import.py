import pandas as pd

def import_questions_from_excel(file_path):
    df = pd.read_excel(file_path)

    # Normalize column names: strip spaces and lowercase
    df.columns = df.columns.str.strip().str.lower()

    questions = []
    for _, row in df.iterrows():
        questions.append({
            'question': row['question text'],
            'answers': [
                row['answer 1'],
                row['answer 2'],
                row['answer 3'],
                row['answer 4']
            ],
            'correct_index': int(row['correct answer index']),
            'correct_feedback': row['correct feedback'],
            'incorrect_feedback': row['incorrect feedback']
        })
    return questions
