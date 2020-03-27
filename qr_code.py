# py 3.8.1
# import QR code libz
import pyqrcode
from pyqrcode import QRCode

# data for encoding
data = "Python FOR THE WIN"

# create qr code
qr = pyqrcode.QRCode( content = data )
qr.png(file='test.svg', scale=8)
qr.show()
# print(qr.terminal())

code = pyqrcode.create('test')
code.show()
text = code.terminal()
# print(text)

