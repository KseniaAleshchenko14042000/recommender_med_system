import pandas as pd
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import MedProcessing as MP
import PacientTable as  PT


Form, Window = uic.loadUiType("gui.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
FormSel, WindowSel = uic.loadUiType("guisel.ui")
appSel = QApplication([])
windowSel = WindowSel()
formSel = FormSel()
formSel.setupUi(windowSel)
windowSel.show()
windowSel.hide()
print(pd.__version__ + "*******************************************************")

diagL = ["адинамия",
"артериальная гипотензия",
"астения",
"атонические запоры",
"атония",
"атопический дерматит",
"бактериальная этиология",
"болезнь Рейно",
"выпадение волос",
"гастродуоденит",
"геморрой",
"геморрой",
"гепатит",
"гипертонические кризы",
"гипотония",
"грибкая этиология",
"двенадцатиперстной кишки",
"депрессия",
"детская экзема",
"дефицит кальция",
"дискинезия желчевыводящих путей",
"дислипидемия",
"дуодениты",
"железодефицитная анемия",
"инфекции органов ЖКТ",
"инфекции органов мочеполовой системы",
"инфекционно-воспалительное заболевание",
"истинная экзема",
"кардиогенный ожог",
"кожные тофусы",
"контузии",
"крапивница",
"купирование пароксизмов наджелудочковой тахикардии",
"лучевая болезнь",
"метастатический немелкоклеточный рак",
"метеоризм",
"микробная экзема",
"нарушение систолической функции левого желудочка",
"неврастения",
"неврастения",
"неврогенная анорексия",
"недостаток минеральных веществ",
"нейродермит",
"нефролитиаз",
"облитерирующий тромбангиит",
"ожоги",
"операция кесарево сечение ",
"ОРВИ",
"острый пародонтит",
"острый язвенно-некротический гингивит Венсана",
"перемежающаяся хромота",
"переутомление",
"перхоть",
"пигментная дегенерация сетчатки",
"пневмоцистная инфекция",
"полименорея",
"полиомиелит",
"послеоперационная паралитическая кишечная непроходимость",
"постгриппозный арахноидит",
"постоперационнное состояние",
"постоперация",
"постхолецистэктомический синдром ",
"раны",
"рассеянный склероз",
"резидуальные органические поражения мозга",
"реконвалесценция",
"сенильная деменция",
"синдромом Леннокса-Гасто",
"синусит",
"снижение либидо",
"спастические колиты",
"субинволюция матки",
"сухость кожи",
"токсический ожог",
"токсоплазмоз",
"травма",
"травматическая энцефалопатия",
"физическое истощение",
"холангит",
"холецистит",
"хроническая сердечная недостаточность",
"хронический гастрит",
"хронический гингивит",
"хронический пародонтит",
"церебральная органическая недостаточность",
"ЧМТ",
"шизоаффектие расстройства",
"энтероколиты",
"энурез",
"язвенная болезнь желудка",
"язвы",
"минингит"
]

diagLdig = list
form.Diag.addItems(diagL)
mp = MP.MedProcessing()
pt = PT.PacientTable(mp.getFrame)
pcntCurID =  None

#def addPreparEV():

#form.addPrepar.clicked.connect(addPreparEV)

def processBTNEV():
    global pcntCurID
    print(form.Diag.currentText())
    if pcntCurID == None:
        print("Пациэнт не указан")
        pcntCurID = pt.addPacient(form.PNTfamil.text(), form.PNTname.text(), form.PNTsname.text(), form.age.value(), form.smcng.isChecked(), form.alchl.isChecked(), [])
    result = mp.prcessАppoint(form.Diag.currentText(), form.smcng.isChecked(), form.alchl.isChecked(), pt.getPacCurMed(pcntCurID))
    form.MedSH.clear()
    form.MedOpSH.clear()
    form.MedDosSH.clear()
    form.prdpSH.clear()
    form.smkngSH.setCheckState( False)
    form.AlchlSH.setCheckState( False)
    form.MedSH.append(          result[0])
    form.MedOpSH.append(        result[1])
    form.MedDosSH.append(       result[2])
    form.prdpSH.append(         result[3])
    form.smkngSH.setCheckState( result[4])
    form.AlchlSH.setCheckState( result[5])
    print(result[6])
    if result[6] != '':
        pt.addCurMedPac(result[6], pcntCurID)
    updCurMed()
    pt.print()

form.processBTN.clicked.connect(processBTNEV)

def saveBTNEV():
   pt.save()
   print("pcntCurID - - " + str(pcntCurID))
form.saveBTN.clicked.connect(saveBTNEV)


def addPacientBTNEV(): 
   global pcntCurID
   pcntCurID =  pt.addPacient(form.PNTfamil.text(), form.PNTname.text(), form.PNTsname.text(), form.age.value(), form.smcng.isChecked(), form.alchl.isChecked(), [])
   print("pcntCurID" + str(pcntCurID))
   updCurMed()
   updSelPac()
   pt.print()
form.addPacientBTN.clicked.connect(addPacientBTNEV)

def editPacientBTNEV():
   if pcntCurID != None:
        print(form.smcng.isChecked())
        pt.editPacient(form.PNTfamil.text(), form.PNTname.text(), form.PNTsname.text(), form.age.value(), form.smcng.isChecked(), form.alchl.isChecked(),[], pcntCurID)
        updSelPac()
        pt.print()
form.editPacientBTN.clicked.connect(editPacientBTNEV)


def delPacBTNEV():
    if pcntCurID != None:
        pt.delPacient(pcntCurID)
        pt.print()
        updSelPac()
form.delPacBTN.clicked.connect(delPacBTNEV)

def updCurMed():
    if pcntCurID != None:
        form.CurMedSH.clear()
        curmed =mp.getMedNameFList(pt.getPacCurMed(pcntCurID))
        print(curmed)
        form.CurMedSH.addItems( ["Не принимает препараты"] if curmed == [] else curmed)


def updSelPac():
    formSel.PacientSH.clear()
    formSel.PacientSH.addItems(pt.getPacients())

def delMedBTNEV():
    if pcntCurID != None:
        if pt.getPacCurMed(pcntCurID)!= []:
            pt.delMed(pcntCurID, form.CurMedSH.currentRow())
            updCurMed()
form.delMedBTN.clicked.connect(delMedBTNEV)

def selectBTNEV():
    windowSel.show()
    updSelPac()
    pt.print()
form.selectBTN.clicked.connect(selectBTNEV)

def selectBTNEV():
    global pcntCurID
    pcntCurID = formSel.PacientSH.currentRow() 
    print("pcntCurID - - " + str(pcntCurID))
    pacienD = pt.getPacient(pcntCurID)
    form.PNTfamil.setText(pacienD[0])
    form.PNTname.setText(pacienD[1])
    form.PNTsname.setText(pacienD[2])
    form.age.setValue(pacienD[3])
    form.smcng.setCheckState(pacienD[4])
    form.alchl.setCheckState(pacienD[5])
    updCurMed()
    pt.print()
formSel.selBTN.clicked.connect(selectBTNEV)

def delBTNEV():
    pt.delPacient(formSel.PacientSH.currentRow())
    updSelPac()
    pt.print()
formSel.delBTN.clicked.connect(delBTNEV)


app.exec_()