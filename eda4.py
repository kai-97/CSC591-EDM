import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

financeData = pd.read_csv('states_per_student.csv')
gradeData = pd.read_csv('states_scores.csv')
financeData = financeData[financeData['YEAR'] == 2015]
financeData = financeData[financeData['STATE'] != 'NATIONAL']
financeData = financeData[financeData['STATE'] != 'DODEA']
gradeData = gradeData[gradeData['YEAR'] == 2015]
gradeData = gradeData[gradeData['STATE'] != 'NATIONAL']
gradeData = gradeData[gradeData['STATE'] != 'DODEA']

output = {
    'STATE': gradeData['STATE'].values,
    'AVERAGE_SCORE': gradeData['AVERAGE_SCORE'].values,
    'REVENUE_PER_STUDENT': financeData['REVENUE_PER_STUDENT'].values
}
odf = pd.DataFrame(output)

m, b = np.polyfit(odf['REVENUE_PER_STUDENT'], odf['AVERAGE_SCORE'], 1)


plt.plot(odf['REVENUE_PER_STUDENT'], odf['AVERAGE_SCORE'], 'o')
plt.plot(odf['REVENUE_PER_STUDENT'], m * odf['REVENUE_PER_STUDENT'] + b)
plt.show()