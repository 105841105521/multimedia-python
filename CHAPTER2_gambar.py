
# 2.1 Manipulasi Gambar dengan Pillow
# ===============================

from PIL import Image, ImageFilter

# 2.1.1 Memuat Gambar
image = Image.open('gambar.jpeg')

# 2.1.2 Pemotongan Gambar
cropped_image = image.crop((10, 10, 200, 200))
cropped_image.save('cropped_result.jpg')

# 2.1.3 Pengubahan Ukuran Gambar
resized_image = cropped_image.resize((100, 100))
resized_image.save('resized_result.jpg')

# 2.1.4 Penerapan Filter
filtered_image = resized_image.filter(ImageFilter.BLUR)
filtered_image.save('filtered_result.jpg')

# 2.1.5 Konversi Mode Warna (RGBA ke RGB)
if filtered_image.mode == 'RGBA':
    filtered_image = filtered_image.convert('RGB')
filtered_image.save('converted_result.jpg')
