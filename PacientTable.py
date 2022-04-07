from asyncio.windows_events import NULL
from msilib.schema import Class
import pandas as pd
import numpy as np

class PacientTable(object):
    cdata = pd.DataFrame 
    pdata = pd.DataFrame 
    def __init__(self, df):
        PacientTable.cdata = df
        PacientTable.pdata=pd.read_csv('out.csv', index_col = "Unnamed: 0")
        print(PacientTable.pdata)
        PacientTable.pdata['curMed'] =PacientTable.pdata['curMed'].str.replace("[", "")
        PacientTable.pdata['curMed'] =PacientTable.pdata['curMed'].str.replace("]", "")
        PacientTable.pdata['curMed'] =PacientTable.pdata['curMed'].str.replace("'", "")
        PacientTable.pdata['curMed'] =PacientTable.pdata['curMed'].str.replace("dtype: int64", "")
        PacientTable.pdata['curMed'] =PacientTable.pdata['curMed'].str.split(", ")
        #PacientTable.pdata['age']    =pd.to_numeric(PacientTable.pdata['age'])
        print(PacientTable.pdata)
        

        for i in range(PacientTable.pdata['curMed'].size):
            if PacientTable.pdata['curMed'].loc[i] != [""]:  
                PacientTable.pdata['curMed'].loc[i] = [int(item) for item in PacientTable.pdata['curMed'].loc[i]]  #pd.to_numeric(pd.Series(PacientTable.pdata['curMed'].loc[i]))#
        
        print(PacientTable.pdata)
        print(PacientTable.pdata.curMed.loc[0][0])

    

    def addPacient(self, family, name, sname, age, smcn, alchl, curMed):
        family  = 'Не указано' if family    == '' else family
        name    = 'Не указано' if name      == '' else name
        sname   = 'Не указано' if sname     == '' else sname
        print(type(family))
        PacientTable.pdata = PacientTable.pdata.append({'family':family,'name':name,'sname':sname,'age':age,'smcn':smcn,'alchl':alchl,'curMed':curMed}, ignore_index=True)
        return PacientTable.pdata.index.max()
    def editPacient(self, family, name, sname, age, smcn, alchl, curMed, ind):
        family  = 'Не указано' if family    == '' else family
        name    = 'Не указано' if name      == '' else name
        sname   = 'Не указано' if sname     == '' else sname
        PacientTable.pdata.loc[ind]= {'family':family,'name':name,'sname':sname,'age':age,'smcn':smcn,'alchl':alchl,'curMed':PacientTable.pdata["curMed"].loc[ind]}
    def addCurMedPac(self, addMed, ind):
        curMed = PacientTable.pdata["curMed"].loc[ind]
        print(curMed)
        if curMed == []:
            PacientTable.pdata["curMed"].loc[ind] = [addMed]
        else:
            PacientTable.pdata["curMed"].loc[ind] = curMed + [addMed]
    def getPacient(self, ind):
       return [ PacientTable.pdata['family' ].values[ind],
                PacientTable.pdata['name'   ].values[ind],
                PacientTable.pdata['sname'  ].values[ind],
                PacientTable.pdata['age'    ].values[ind],
                True  if PacientTable.pdata['smcn'   ].values[ind] == np.bool_(True) else False,
                True  if PacientTable.pdata['alchl'   ].values[ind] == np.bool_(True) else False,
                PacientTable.pdata['curMed' ].values[ind] 
              ]
    def save(self):
        PacientTable.pdata.to_csv("out.csv")
        print(PacientTable.pdata)

    def print(self):
        print(PacientTable.pdata)

    def getPacCurMed(self, ind):
        return PacientTable.pdata["curMed"].loc[ind]
        
            
    def delMed(self, ind, mdind):
        PacientTable.pdata["curMed"].loc[ind].pop(mdind)
    def delPacient(self, ind):
        PacientTable.pdata = PacientTable.pdata.drop(ind).reset_index(drop=True)
    def getPacients(self):
        return PacientTable.pdata['family'] + " " + PacientTable.pdata['name'] + " " + PacientTable.pdata['sname']





















