import qrcode
import os

website_link = input('Paste website link: ')
input_version = int(input("Size (pick between 1-40): "))
input_border = int(input('Border thickness (pick between 1-40): '))

qr = qrcode.QRCode(version=input_version, box_size=5, border=input_border)
qr.add_data(website_link)
qr.make()

img = qr.make_image(fill_color='black', back_color='white')

os.makedirs('qr_code', exist_ok=True)
img.save('qr_code/qr_output.png')

print("QR code saved to qr_code/qr_output.png")

