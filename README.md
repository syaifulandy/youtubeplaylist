# Youtubeplaylist Downloader
Downloader ini dapat digunakan untuk download video di youtube playlist, termasuk memilih video yang tidak perlu di download dalam suatu playlist.
Downloader ini merupakan pengembangan dari https://github.com/svass/youtube-playlist-downloader

# Requirement
1. Python v2.7x (https://www.python.org/downloads/)
2. Install Pytube: pip install pytube
  
Note: Untuk di windows, menginstal pytube dapat dilakukan dengan menggunakan command line (CMD), lalu pindah ke directory Script di folder  python ( cd C:\Python27\Scripts ), kemudian di CMD jalankan perintah : pip.exe install pytube

# How to Use
1. Download kode playlistdownloader.py, proses editing kode program sebaiknya dilakukan dengan program IDLE (setelah install Python v2.7x). Untuk memudahkan, kode program ini bisa diletakkan di folder tempat video playlist akan di download.
2. Ubah link youtube ke playlist yang diinginkan pada kode program : Link_playlist_url = "https://www.youtube.com/playlist?list=PLUYZIGi0rAXBBTLhdVPFTd6XvbTnTS2EG" 
3. Tuliskan playlist yang tidak mau di download pada kode program: jangandonlod = [1, 2, 3, 4, 5 , 6] --> tidak mendownload video ke 1-6 dalam playlist.
4. Untuk mengatur kualitas video, Ubah nilai pada kode program (0 biasanya kualitas terbaik). List kualitas bisa dilakukan dengan: melakukan "print yt.streams.all()".
5. Untuk menjalankan program dari IDLE, klik menu run, pilih  run module (atau langsung tekan F5). Bila mengunakan cara ini, video akan tersimpan di folder yang sama dengan kode program.

# Notes
1. Dokumentasi lebih lengkap untuk pengembangan lebih jauh (nambah caption, progress bar, dll):  https://python-pytube.readthedocs.io/en/latest/.
2. Semoga bermanfaat dan mohon tidak disalahgunakan.
