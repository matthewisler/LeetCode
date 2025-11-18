import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    df = examinations.groupby(['student_id','subject_name']).size().reset_index(name='attended_exams')
    all_id_subjects = pd.merge(students, subjects, how='cross')
    ret = pd.merge(df, all_id_subjects, on = ['student_id','subject_name'], how='right')

    ret['attended_exams'] = ret['attended_exams'].fillna(0).astype(int)

    ret.sort_values(['student_id', 'subject_name'], inplace=True)

    return ret[['student_id', 'student_name', 'subject_name', 'attended_exams']]