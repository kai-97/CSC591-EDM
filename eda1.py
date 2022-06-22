import pandas as pd
from numpy import mean, std

data = pd.read_csv('states_all_extended.csv')

revPerStudent = []
totExPerStudent = []
insExPerStudent = []
supExPerStudent = []
othExPerStudent = []
capExPerStudent = []

for index, row in data.iterrows():
    if row['ENROLL'] is not None and row['TOTAL_REVENUE'] is not None:
        revPerStudent.append(row['TOTAL_REVENUE'] / row['ENROLL'])
    else:
        revPerStudent.append(None)
    if row['ENROLL'] is not None and row['TOTAL_EXPENDITURE'] is not None:
        totExPerStudent.append(row['TOTAL_EXPENDITURE'] / row['ENROLL'])
    else:
        totExPerStudent.append(None)
    if row['ENROLL'] is not None and row['INSTRUCTION_EXPENDITURE'] is not None:
        insExPerStudent.append(row['INSTRUCTION_EXPENDITURE'] / row['ENROLL'])
    else:
        insExPerStudent.append(None)
    if row['ENROLL'] is not None and row['SUPPORT_SERVICES_EXPENDITURE'] is not None:
        supExPerStudent.append(row['SUPPORT_SERVICES_EXPENDITURE'] / row['ENROLL'])
    else:
        supExPerStudent.append(None)
    if row['ENROLL'] is not None and row['OTHER_EXPENDITURE'] is not None:
        othExPerStudent.append(row['OTHER_EXPENDITURE'] / row['ENROLL'])
    else:
        othExPerStudent.append(None)
    if row['ENROLL'] is not None and row['CAPITAL_OUTLAY_EXPENDITURE'] is not None:
        capExPerStudent.append(row['CAPITAL_OUTLAY_EXPENDITURE'] / row['ENROLL'])
    else:
        capExPerStudent.append(None)

data['REVENUE_PER_STUDENT'] = revPerStudent
data['TOTAL_EXPENDITURE_PER_STUDENT'] = totExPerStudent
data['INSTRUCTION_EXPENDITURE_PER_STUDENT'] = insExPerStudent
data['SUPPORT_SERVICES_EXPENDITURE_PER_STUDENT'] = supExPerStudent
data['OTHER_EXPENDITURE_PER_STUDENT'] = othExPerStudent
data['CAPITAL_OUTLAY_EXPENDITURE_PER_STUDENT'] = capExPerStudent

output = {
    'STATE': data['STATE'],
    'YEAR': data['YEAR'],
    'REVENUE_PER_STUDENT': revPerStudent,
    'TOTAL_EXPENDITURE_PER_STUDENT': totExPerStudent,
    'INSTRUCTION_EXPENDITURE_PER_STUDENT': insExPerStudent,
    'SUPPORT_SERVICES_EXPENDITURE_PER_STUDENT': supExPerStudent,
    'OTHER_EXPENDITURE_PER_STUDENT': othExPerStudent,
    'CAPITAL_OUTLAY_EXPENDITURE_PER_STUDENT': capExPerStudent
}
odf = pd.DataFrame(output)
odf.to_csv('states_per_student.csv')