import pandas as pd

def import_questions_from_excel(file_path):
    df = pd.read_excel(file_path)

    questions = []
    for _, row in df.iterrows():
        questions.append({
            'question': row['Question Text'],
            'answers': [row['Answer 1'], row['Answer 2'], row['Answer 3'], row['Answer 4']],
            'correct_index': int(row['Correct Answer Index']),
            'correct_feedback': row['Correct Feedback'],
            'incorrect_feedback': row['Incorrect Feedback']
        })
    return questions
