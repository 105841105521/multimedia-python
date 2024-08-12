
from PIL import Image, ImageFilter

# 1. Memuat gambar dari file
gambar = Image.open('example.jpeg')

# Menyimpan gambar
gambar.save('hasil.jpg')

# 2. Memotong gambar
gambar_terpotong = gambar.crop((10, 10, 200, 200))

# 3. Mengubah ukuran gambar
gambar_ukuran_baru = gambar_terpotong.resize((100, 100))

# 4. Menerapkan filter blur pada gambar
gambar_terfilter = gambar_ukuran_baru.filter(ImageFilter.BLUR)

# 5. Mengonversi gambar dari mode RGBA ke RGB jika diperlukan
if gambar_terfilter.mode == 'RGBA':
    gambar_terfilter = gambar_terfilter.convert('RGB')

# 6. Menyimpan gambar sebagai JPEG atau PNG
gambar_terfilter.save('hasil_akhir.jpg') 
