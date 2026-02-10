
import qrcode
import sys
import os

def create_qr(url, filename="qr_code.png"):
    # Create qr code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add data
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save it somewhere, change the extension as needed
    img.save(filename)
    print(f"QR code successfully saved to: {os.path.abspath(filename)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python create_qr_code.py <URL> [filename]")
        print("Example: python create_qr_code.py 'https://google.com' 'my_qr.png'")
        sys.exit(1)
    
    url = sys.argv[1]
    filename = sys.argv[2] if len(sys.argv) > 2 else "qr_code.png"
    
    # Ensure filename has extension
    if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        filename += '.png'
        
    try:
        create_qr(url, filename)
    except Exception as e:
        print(f"Error creating QR code: {e}")
