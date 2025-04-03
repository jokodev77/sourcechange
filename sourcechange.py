import requests
from bs4 import BeautifulSoup

def change_source_code(url, target_tag, new_content):
    """
    Mengubah source code suatu website dengan mengganti konten dari tag yang ditargetkan.

    Args:
        url (str): URL website yang ingin diubah.
        target_tag (str): Nama tag yang ingin diubah.
        new_content (str): Konten baru yang akan diganti.

    Returns:
        str: Source code website yang telah diubah.
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
    for tag in tags:
        tag.string = new_content

    # Mengembalikan source code yang telah diubah
    return str(soup)

Contoh penggunaan
url = "http://example.com"
target_tag = "h1"
new_content = "Judul Baru"

new_source_code = change_source_code(url, target_tag, new_content)

if new_source_code:
    print(new_source_code)