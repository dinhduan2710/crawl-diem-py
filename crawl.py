
import requests
import urllib3
import pandas
from pandas import ExcelFile
import numpy as np

f = open("diemthiTHPTQG.txt", 'a')
movies_sheet1 = pandas.read_excel("SBD.xlsx",index_col=0)
print(movies_sheet1)
col = movies_sheet1.iloc[:, :0]
for x in movies_sheet1:
    urllib3.disable_warnings()
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
