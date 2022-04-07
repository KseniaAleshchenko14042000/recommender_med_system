from asyncio.windows_events import NULL
from msilib.schema import Class
import re
import pandas as pd
import numpy as np
print(np.__version__ + "*******************************************************")
class MedProcessing(object):
    cdata = pd.DataFrame  
    def __init__(self):
        MedProcessing.cdata=pd.read_excel("БД темп.xlsx")
        MedProcessing.cdata['Indication'] = MedProcessing.cdata['Indication'].str.split(", ")

        for i in range(MedProcessing.cdata['Indication'].size):
            MedProcessing.cdata['Indication'].loc[i] =  pd.Series(MedProcessing.cdata['Indication'] .loc[i])

    def prcessАppoint(self, diag, smcng, alchl, curMed):
        c = pd.Series(dtype=np.bool)
        for i in range(MedProcessing.cdata['Indication'].size):
            c= pd.concat([c,pd.Series(np.any(MedProcessing.cdata['Indication'].loc[i] ==  diag))], ignore_index=True)
        fltrd = MedProcessing.cdata.loc[c]

        if smcng:
            fltrd = fltrd.loc[fltrd['Smoking']== True] 
        if alchl:
            fltrd = fltrd.loc[fltrd['Alhocol']== True]

        medGeneric = 0
        n = []
        for i in curMed:
            if i not in n:
                n.append(i)
        curMed = n
        for i in range(len(curMed)):
            if fltrd.index.size  > i:
                if fltrd.index[i] == curMed[i]:
                    medGeneric += 1
            else: 
                    return ["Не возможен выбор лекарств при текущем списке употребляемых препаратов. Попробуйте убедить пациента отказаться от курения или алкоголя.",
                            " ",
                            " ",
                            " ",
                            False,
                            False,
                            ''
                            ]

        fltrd = MedProcessing.cdata.loc[c]
        print(fltrd.index.values[0])
        return [fltrd['RusName'].values[0],
                fltrd['PhInfluence'].values[0],
                fltrd['Dosage'].values[0],
                fltrd['SideEffects'].values[0],
                fltrd['Smoking'].values[0] == "Can",
                fltrd['Alhocol'].values[0] == "Can",
                fltrd.index.values[medGeneric]
                ]
    def getFrame(self):
        return MedProcessing.cdata
    def getMedNameFList(self, listN):
        listSTR = []
        if listN == ['']:
            return ["Не принимает препараты"]
        for i in listN:
            listSTR =listSTR + [MedProcessing.cdata['RusName'].loc[i]]
            print(listSTR)
        return listSTR
    



   
        
























