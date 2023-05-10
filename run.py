# from openpyxl import Workbook
from openpyxl import load_workbook
# wb = Workbook()
wb2 = load_workbook('C:/My websites/Project_3_Test/test_e_i.xlsx')
print(wb2.sheetnames)