import qrcode

data = "https://www.linkedin.com/in/surajchaudhari2003/"
qr = qrcode.make(data)
qr.save("test_qr.png")