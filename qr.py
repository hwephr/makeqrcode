import qrcode

value = input("Type something here...  ")
img = qrcode.make(value)

img.save('qrcode.png')
#Please, follow me on GitHub!)
