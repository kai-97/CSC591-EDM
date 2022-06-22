import pandas as pd
import numpy as np

data = pd.read_csv('naep_states_summary.csv')
data = data[data['YEAR'] >= 2003]
data = data[data['YEAR'] <= 2016]
avgTotal = []

for index, row in data.iterrows():
    sum = row['AVG_MATH_4_SCORE'] + row['AVG_MATH_8_SCORE'] + row['AVG_READING_4_SCORE'] + row['AVG_READING_8_SCORE']
    avgTotal.append(sum / 4)

output = {
    'STATE': data['STATE'],
    'YEAR': data['YEAR'],
    'AVERAGE_SCORE': avgTotal
}

odf = pd.DataFrame(output)
odf.to_csv('states_scores.csv')
    
    
