import qrcode

website_link = input('paste website link plz: ')

input_version = int(input("size (pick between 1-40): "))
input_border = int(input('border thickness (pick between 1-40): '))


qr = qrcode.QRCode(version = input_version, box_size = 5, border = input_border)
qr.add_data(website_link)
qr.make()
 
img = qr.make_image(fill_color = 'black', black_color = 'white ')
img.save('qr_code/youtube_qr.png')

