
import requests
import urllib3
import pandas
from pandas import ExcelFile
import numpy as np
import openpyxl
import xlrd

f = open("diemthiTHPTQG.xlsx", 'a')

loc = ("SBD.xlsx")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
 
sheet.cell_value(0, 0)
 
for i in range(sheet.nrows):
    if (i==0): continue
    x= (sheet.cell_value(i, 0))
    scraping_url = 'https://dantri.com.vn/thpt/1/0/99/'+format(x)+'/2022/0.2/search-gradle.htm'
    payload = {}
    headers = {}
    response = requests.get(scraping_url, allow_redirects=False,verify=False)
    info = response.json()['student']
    diem = "SBD {} Toan {} Van {} Ngoaingu {} Vatly {} Hoahoc {} Sinhhoc {} KHTN {} Lichsu {} Dialy {} GDCD {} KHXH {}".format(
        info['sbd'], info['toan'], info['van'], info['ngoaiNgu'], info['vatLy'], info['hoaHoc'], info['sinhHoc'], info['diemTBTuNhien'], info['lichSu'], info['diaLy'], info['gdcd'], info['diemTBXaHoi'])   
    diemthi = str(diem) +'\n'
    f.write(diemthi)
f.close
         
