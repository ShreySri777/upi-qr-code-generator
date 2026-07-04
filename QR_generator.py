import qrcode

#Taking upi id as an input from user
upi_id = input("Enter your UPI ID ")

#Payment url format =  upi://pay?pa=UPI_ID&apn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

#Definig the payment url based on the pament ap and UPI ID
#You can modify these URLs basede on the payment apps you want to support
phonePe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
googlePay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#Create QR codes for each payment apps
phonePe_qr = qrcode.make(phonePe_url)
googlePay_qr = qrcode.make(googlePay_url)

#Save the QR code as image file in the system
phonePe_qr.save('phonePe_qr.png')
googlePay_qr.save('googlePay_qr.png')

#Diaplay the QR codes (pillow library is needed)
phonePe_qr.show()
googlePay_qr.show()