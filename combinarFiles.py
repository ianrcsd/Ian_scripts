#Powered by -> I@n Rodrigues ( https://linktr.ee/ianredes )
import os, pandas as pd
from pandas.core.frame import DataFrame
from pandas.io import excel
cwd = os.path.abspath('') 
files = os.listdir(cwd) 
## files.remove('combinarFiles.py')

print(files)

df = pd.DataFrame()

def agruparApenas1Sheet(df) -> excel:
    for file in files:
        if file.endswith('.xlsx'):
            print(f'Agrupando arquivo -> {file}')
            df = df.append(pd.read_excel(file), ignore_index=True)
    df.to_excel('Output_Agrupamento.xlsx',index=False)

agruparApenas1Sheet(df) 

'''
def agrupaTodasSheets(df) -> excel:
    for file in files:                         
        if file.endswith('.xlsx'):
            print(f'Agrupando arquivo -> {file}')
            excel_file = pd.ExcelFile(file)
            sheets = excel_file.sheet_names
            for sheet in sheets:               
                print(f'Agrupando a Sheet -> {sheet}')
                df_aux = excel_file.parse(sheet_name = sheet)
                df = df.append(df_aux)
    df.to_excel('Output_Agrupamento_Geral.xlsx',index=False)
'''
