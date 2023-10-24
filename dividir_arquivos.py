from os import sep
import pandas as pd
import chardet

arquivo = '/Users/ianrcsd/Desktop/ian/ian_scripts/file.csv'

def descobrir_encoding(arquivo):
    with open(arquivo, 'rb') as f:
      
        resultado = chardet.detect(f.read())
    return resultado['encoding']

encoding_file = descobrir_encoding(arquivo)
print(f'O encoding do arquivo {arquivo} é {encoding_file}')


number_lines = sum(1 for row in (open(arquivo, encoding=encoding_file)))

rowsize = 500

for i in range(1,number_lines,rowsize):
      df = pd.read_csv(arquivo,header=None,nrows = rowsize, skiprows = i,sep=';', encoding=encoding_file)  
      out_csv = 'output\output' + str(i) + '.csv'
      df.to_csv(out_csv,index=False,header=False,mode='a', chunksize=rowsize, sep=';')
