import qrcode

data = "https://sharajman.com/"

img = qrcode.make(data)
img.save('QRCode.png')


