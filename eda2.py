import pandas as pd
import numpy as np

data = pd.read_csv('states_per_student.csv')
output = {
    'YEAR': [],
    'MAX_REVENUE_STATE': [],
    'MAX_REVENUE': [],
    'MIN_REVENUE_STATE': [],
    'MIN_REVENUE': [],
    'MAX_TOTAL_STATE': [],
    'MAX_TOTAL': [],
    'MIN_TOTAL_STATE': [],
    'MIN_TOTAL': [],
    'MAX_INSTRUCTION_STATE': [],
    'MAX_INSTRUCTION': [],
    'MIN_INSTRUCTION_STATE': [],
    'MIN_INSTRUCTION': [],
    'MAX_SUPPORT_STATE': [],
    'MAX_SUPPORT': [],
    'MIN_SUPPORT_STATE': [],
    'MIN_SUPPORT': [],
    'MAX_OTHER_STATE': [],
    'MAX_OTHER': [],
    'MIN_OTHER_STATE': [],
    'MIN_OTHER': [],
    'MAX_CAPITAL_STATE': [],
    'MAX_CAPITAL': [],
    'MIN_CAPITAL_STATE': [],
    'MIN_CAPITAL': []
}
odf = pd.DataFrame(output)

for x in range(2003, 2017):
    year = data[data['YEAR'] == x]
    buffer = np.min(year['INDEX'])
    revMaxIdx = np.argmax(year['REVENUE_PER_STUDENT'])
    rxS = year['STATE'][revMaxIdx + buffer]
    rxV = year['REVENUE_PER_STUDENT'][revMaxIdx + buffer]
    revMinIdx = np.argmin(year['REVENUE_PER_STUDENT'])
    rnS = year['STATE'][revMinIdx + buffer]
    rnV = year['REVENUE_PER_STUDENT'][revMinIdx + buffer]
    totMaxIdx = np.argmax(year['TOTAL_EXPENDITURE_PER_STUDENT'])
    txS = year['STATE'][totMaxIdx + buffer]
    txV = year['TOTAL_EXPENDITURE_PER_STUDENT'][totMaxIdx + buffer]
    totMinIdx = np.argmin(year['TOTAL_EXPENDITURE_PER_STUDENT'])
    tnS = year['STATE'][totMinIdx + buffer]
    tnV = year['TOTAL_EXPENDITURE_PER_STUDENT'][totMinIdx + buffer]
    insMaxIdx = np.argmax(year['INSTRUCTION_EXPENDITURE_PER_STUDENT'])
    ixS = year['STATE'][insMaxIdx + buffer]
    ixV = year['INSTRUCTION_EXPENDITURE_PER_STUDENT'][insMaxIdx + buffer]
    insMinIdx = np.argmin(year['INSTRUCTION_EXPENDITURE_PER_STUDENT'])
    inS = year['STATE'][insMinIdx + buffer]
    inV = year['INSTRUCTION_EXPENDITURE_PER_STUDENT'][insMinIdx + buffer]
    supMaxIdx = np.argmax(year['SUPPORT_SERVICES_EXPENDITURE_PER_STUDENT'])
    sxS = year['STATE'][supMaxIdx + buffer]
    sxV = year['SUPPORT_SERVICES_EXPENDITURE_PER_STUDENT'][supMaxIdx + buffer]
    supMinIdx = np.argmin(year['SUPPORT_SERVICES_EXPENDITURE_PER_STUDENT'])
    snS = year['STATE'][supMinIdx + buffer]
    snV = year['SUPPORT_SERVICES_EXPENDITURE_PER_STUDENT'][supMinIdx + buffer]
    othMaxIdx = np.argmax(year['OTHER_EXPENDITURE_PER_STUDENT'])
    oxS = year['STATE'][othMaxIdx + buffer]
    oxV = year['OTHER_EXPENDITURE_PER_STUDENT'][othMaxIdx + buffer]
    othMinIdx = np.argmin(year['OTHER_EXPENDITURE_PER_STUDENT'])
    onS = year['STATE'][othMinIdx + buffer]
    onV = year['OTHER_EXPENDITURE_PER_STUDENT'][othMinIdx + buffer]
    capMaxIdx = np.argmax(year['CAPITAL_OUTLAY_EXPENDITURE_PER_STUDENT'])
    cxS = year['STATE'][capMaxIdx + buffer]
    cxV = year['CAPITAL_OUTLAY_EXPENDITURE_PER_STUDENT'][capMaxIdx + buffer]
    capMinIdx = np.argmin(year['CAPITAL_OUTLAY_EXPENDITURE_PER_STUDENT'])
    cnS = year['STATE'][capMinIdx + buffer]
    cnV = year['CAPITAL_OUTLAY_EXPENDITURE_PER_STUDENT'][capMinIdx + buffer]
    
    odf.loc[len(odf.index)] = [x, rxS, rxV, rnS, rnV, txS, txV, tnS, tnV, ixS, ixV, inS, inV, sxS, sxS, snS, snV, oxS, oxV, onS, onV, cxS, cxV, cnS, cnV]

odf.to_csv('year_max_min.csv')
