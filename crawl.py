
import requests
import urllib3
f = open("diemthiTHPTQG.txt", 'a')
for x in (27000001,27000002,27001203):
    urllib3.disable_warnings()
    # scraping_url = "https://diemthi.laodong.vn/tra-cuu-diem-thi-thpt-xem-diem-thi-dai-hoc-2022.html?sbd=" + 
    scraping_url = 'https://dantri.com.vn/thpt/1/0/99/'+str(x)+'/2021/0.2/search-gradle.htm'
    payload = {}
    headers = {}
    response = requests.get(scraping_url, allow_redirects=False,verify=False)
    info = response.json()['student']
    diem = "SBD {} Toan {} Van {} Ngoaingu {} Vatly {} Hoahoc {} Sinhhoc {} KHTN {} Lichsu {} Dialy {} GDCD {} KHXH {}".format(
        info['sbd'], info['toan'], info['van'], info['ngoaiNgu'], info['vatLy'], info['hoaHoc'], info['sinhHoc'], info['diemTBTuNhien'], info['lichSu'], info['diaLy'], info['gdcd'], info['diemTBXaHoi'])
    diemthi = str(diem) +'\n'
    f.write(diemthi)
f.close
