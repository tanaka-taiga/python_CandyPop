import os 
import qrcode

dir_path = os.path.join("./","files","mynavi.png")
img = qrcode.make("https://www.mynavi.jp/")

img.save(dir_path)

# def create_qr_code(url, qr_path):
#     qr = qrcode.QRCode(
#         version=1,
#         error_correction=qrcode.constants.ERROR_CORRECT_L,
#         box_size=10,
#         border=4,
#     )
#     qr.add_data(url)
#     qr.make(fit=True)

#     img = qr.make_image(fill='black', back_color='white')
#     img.save(qr_path)

# image_url = 'https://www.imdb.com/title/tt0213370/'  # 이미지 파일 URL
# qr_path = './files/Qrcode.png'  # 생성할 QR 코드 파일 경로

# create_qr_code(image_url, qr_path)
