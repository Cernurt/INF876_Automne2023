"""
Cek status https://ivoting.iaitb.or.id

Dependency: pip install requests

Cara pakai: python cek_status_ivoting.py input.csv

Format file input (csv):
nama1,jurusan1,angkatan1
nama2,jurusan2,angkatan2
nama3,jurusan3,angkatan3

Hasil (csv):
nama1,jurusan1,angkatan1,status
nama2,jurusan2,angkatan2,status
nama3,jurusan3,angkatan3,status

@Author yohanes.gultom@gmail.com
"""

import csv
import requests
import sys

# ambil lagi via browser jika kadaluarsa
api_key = 'bsgcyfgveyujeygfefc387r34ybr39brnr3r3'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36',
    'Origin': 'https://ivoting.iaitb.or.id/',
    'api-key': api_key,
}
url_template = 'https://ivoting.iaitb.or.id/api/open/alumnee/simple/all?name={}&page=1&perPage=10&studyprogram={}&generation={}'

input_file = sys.argv[1]
print(f'Membaca input {input_file}...')
input_rows = []
with open(input_file) as f:
    reader = csv.reader(f)
    for row in reader:
        nama = row[0]
        jurusan = row[1]
        angkatan = int(row[2])
        input_rows.append((nama, jurusan, angkatan))

print('Memutakhirkan status...')
with open(input_file, 'w') as f:
    writer = csv.writer(f)
    for row in input_rows:
        nama, jurusan, angkatan = row
        try:
            res = requests.get(url_template.format(nama, jurusan, angkatan), headers=headers)
            body = res.json()
            status = body['data'][0]['verificationStatus']
        except Exception as e:
            status = str(e)
        finally:
            writer.writerow((nama, jurusan, angkatan, status))
            print(f'{nama}| {jurusan} | {angkatan} | {status}')
