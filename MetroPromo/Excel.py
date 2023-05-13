import openpyxl
import os
from MetroPromo import FILE_PATH

def save_to_excel(title, price):
    file = FILE_PATH
    
    if (os.path.isfile(file)):
        wb_append = openpyxl.load_workbook(file)
        sheet = wb_append.active
        sheet.append([title, price])
        wb_append.save(file)
        wb_append.close()   
    else:
        wb = openpyxl.Workbook()
        sheet = wb.active
        sheet.append([title, price])
        wb.save(file)
        wb.close()