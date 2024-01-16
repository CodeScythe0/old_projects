import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

#barcode content
qr.add_data("""
https://forms.gle/KXFNttvvUtZMmX2A8
""")

#auto adjust the size
qr.make(fit=True)

#specifying barcode color
img = qr.make_image(fill_color="#000000", back_color="#f7f7fa")

img.save("QR CODE.png")
