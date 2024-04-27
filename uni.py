import json
import pandas as pd

university_id = []
university_name = []

with open('uni.json') as f:
    universities = json.load(f)
    for university in universities:
        university_id.append(university["university_id"])
        university_name.append(university["university_name_en"])

uni = pd.DataFrame([university_id, university_name]).transpose()
uni.columns = ['UNI_ID', 'UNI_NAME']
uni.dropna(inplace=True)
uni.to_csv(r'/Users/thanapatpiyamssakul/coding/first_year/de141/uni.csv', index=False)
