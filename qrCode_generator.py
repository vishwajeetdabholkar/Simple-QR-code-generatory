import pyqrcode 
import png 
from pyqrcode import QRCode
#from IPython.display import Image
link_to_convt = "https://github.com/vishwajeetdabholkar?tab=repositories"
#link_to_convt = input("Enter the link for which you want to genrate QR code:")
def createQr(link):
    
    url = pyqrcode.create(link_to_convt)

    # Create and save the svg file naming "qrcd.svg" 
    url.svg("qrcd.svg", scale = 8) 
    # Create and save the png file naming "qrcd.png" 
    url.png('qrcd.png', scale = 6)
    #return Image(filename='qrcd.png')  To rpint QR in jupyter notebook
    
if __name__=="__main__":
    createQr(link_to_convt)