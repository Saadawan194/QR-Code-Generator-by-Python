# QR Code Generator
# Step 1: Install the qrcode library
# You can install it using pip:
import qrcode

# Enter url of your website/youtube channel etc.
url = input("Enter the URL: ").strip()

# Enter File path here
file_path = "D:\\Python Projects\\Qr Code Generator\\qr_code.png"

# Generate the QR code
qr = qrcode.QRCode()
qr.add_data(url)

# Create an image from the QR code and save it to the specified file path
img = qr.make_image()
img.save(file_path)

# Inform the user that the QR code has been generated and saved
print("QR code generated and saved to {file_path}")