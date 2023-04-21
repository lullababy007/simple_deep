import pandas as pd

# 1. 엑셀 파일 읽기

#내 참조하고싶은 엑셀파일 저장위치 
file_path = 'your_excel_file.xlsx'

df = pd.read_excel(file_path, engine='openpyxl')

# 데이터 가공하기 (예: 모든 숫자에 10을 더하기)
df = df.applymap(lambda x: x + 10 if isinstance(x, (int, float)) else x)

# 엑셀 파일에 저장하기
output_file_path = 'output_excel_file.xlsx'
df.to_excel(output_file_path, index=False, engine='openpyxl')