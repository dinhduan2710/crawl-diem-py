
import requests
for x in range(27000001,27011000):
    scraping_url = "https://diemthi.laodong.vn/tra-cuu-diem-thi-thpt-xem-diem-thi-dai-hoc-2022.html?sbd=" + str(x)
    payload = {}
    headers = {}
    response = requests.request(
        "GET",scraping_url, headers=headers, data=payload
    )
    info = response.json()['student']
    diem = "sbd {} Toan {} Van {} NoaiNgu {} Vatly {} HoaHoc {} SinhHoc {} TBKHTN {} LichSu {} DiaLy {} GDCD {} TBKHXH {}".format(
        info['sbd'],info['toan'],info['van'],info['ngoaingu'],info['vatli'],info['hoahoc'],info['sinhhoc'],info['fiemtbtn'],info['lichsu'],info['diali'],info['gdcd'],info['tbkhxh']
    ),
    diemthi = str(diem)
    print(diemthi)