import requests
from bs4 import BeautifulSoup

def change_source_code(url, target_tag):
    """
    Mengubah source code suatu website dengan mengganti konten dari tag yang ditargetkan.

    Args:
        url (str): URL website yang ingin diubah.
        target_tag (str): Nama tag yang ingin diubah.

    Returns:
        str: Konten dari tag yang telah diubah.
    """

    # Mengirimkan request GET ke website target
    response = requests.get(url)

    # Memastikan request berhasil
    if response.status_code != 200:
        print("Gagal mengakses website")
        return None

    # Mengubah source code dengan BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Mencari tag yang ditargetkan
    tags = soup.find_all(target_tag)

    # Mengganti konten dari tag yang ditargetkan
    new_content = input("Masukkan kata/script yang ingin ditulis: ")
    for tag in tags:
        tag.string = new_content

    # Mengembalikan konten dari tag yang telah diubah
    return str(soup), tags[0].text

url = input("Masukkan URL website yang ingin diubah: ")
target_tag = input("Masukkan nama tag yang ingin diubah (contoh: h1, p, etc.): ")

hasil_ubahan, new_content_tag = change_source_code(url, target_tag)

if hasil_ubahan:
    print("Konten dari tag telah diubah menjadi:", new_content_tag)
    print("Link hasil rubahan: ", url)
    print("Hasil rubahan:")
    print(hasil_ubahan)