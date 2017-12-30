# Youtubeplaylist Downloader
Downloader ini dapat digunakan untuk download video di youtube playlist, termasuk memilih video yang tidak perlu di download dalam suatu playlist.
Downloader ini merupakan pengembangan dari https://github.com/svass/youtube-playlist-downloader

# Requirement
1. Python v2.7x
2. Pytube: pip install pytube

# How to Use
1. Ubah link youtube ke playlist yang diinginkan : Link_playlist_url = "https://www.youtube.com/playlist?list=PLUYZIGi0rAXBBTLhdVPFTd6XvbTnTS2EG" 
2. Tuliskan playlist yang tidak mau di download: jangandonlod = [1, 2, 3, 4, 5 , 6] --> tidak mendownload video ke 1-6 dalam playlist
3. Untuk mengatur kualitas video, nilai 0 biasanya kualitas terbaik. List kualitas bisa dilakukan dengan: melakukan "print yt.streams.all()"
4. Bisa ditambah kalau mau download caption: https://python-pytube.readthedocs.io/en/latest/

# Notes
1. Dokumentasi lebih lengkap untuk pengembangan lebih jauh:  https://python-pytube.readthedocs.io/en/latest/.
2. Semoga bermanfaat dan mohon tidak disalahgunakan.
