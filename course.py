import json
import pandas as pd

university_id = []
university_name = []
campus = []
faculty = []
program = []
language_type = []

with open('course.json') as f:
    courses = json.load(f)
    for course in courses:
        university_id.append(course["university_id"])
        university_name.append(course["university_name_en"])
        campus.append(course["campus_name_en"])
        faculty.append(course["faculty_name_en"])
        program.append((course["program_name_en"]))
        language_type.append((course["program_type_name_th"]))

uni = pd.DataFrame([university_id, university_name, campus, faculty, program, language_type]).transpose()
uni.columns = ['UNI_ID', 'UNI_NAME', 'CAMPUS, FACULTY, PROGRAM, LANGUAGE_TYPE']
uni.dropna(inplace=True)
uni.to_csv(r'/Users/thanapatpiyamssakul/coding/first_year/de141/course.csv', index=False)
