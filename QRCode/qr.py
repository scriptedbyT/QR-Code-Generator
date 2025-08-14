import qrcode

infor = "scriptedbyT"
qrr = qrcode.make(infor)
qrr.save('qr.png')
print('QR Code Generated!') 
