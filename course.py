import json
import pandas as pd

# Load JSON data
with open('course.json') as f:
    courses = json.load(f)

# Create DataFrame from JSON data
uni = pd.DataFrame.from_records(courses)

# Select relevant columns
uni = uni[['university_id', 'university_name_en', 'campus_name_en', 'faculty_name_en', 'field_name_en',
           'program_name_en', 'program_type_name_th']]

# Rename columns
uni.columns = ['UNI_ID', 'UNI_NAME', 'CAMPUS', 'FACULTY', 'DEPT', 'PROGRAM', 'LANGUAGE_TYPE']

# Drop rows with missing values
uni.dropna(inplace=True)

# Save DataFrame to CSV
uni.to_csv('/Users/thanapatpiyamssakul/coding/first_year/de141/courses1.csv', index=True)
