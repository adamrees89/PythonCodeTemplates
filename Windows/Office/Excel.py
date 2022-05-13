## Credit to Haider Imtiaz

# Automate Excel
# pip install xlrd
import xlrd
wb = xlrd.open_workbook('test.xlsx')
worksheet = wb.sheet_by_index(0)
# Read by row and col number
print(worksheet.cell_value(0, 0))
# read whole row
print(worksheet.row_values(0))
# read whole col
print(worksheet.col_values(1))
# Write to excel by row and col number
worksheet.write(0, 0, 'Hello')
wb.save('test.xlsx')

#---------------------------------------------------