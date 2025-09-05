import qrcode

# take input
data = input("Enter the text or URL: ")
filename = input("Enter the filename : ") + ".png"

# create qr object
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

qr.add_data(data)
qr.make(fit=True)

# generate image
image = qr.make_image(fill_color="black", back_color="white")

# save image
image.save(filename)

print(f" QR Code saved as {filename}")
