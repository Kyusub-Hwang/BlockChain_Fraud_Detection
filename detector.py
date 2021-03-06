import tkinter
import hashlib
import binascii

window=tkinter.Tk()

window.title("Blockchain Header Checker")
window.geometry("640x400")
window.resizable(False, False)
    
def check():  
    version = binascii.hexlify(binascii.unhexlify(str(e1.get()))[::-1])
    hashPrevBlock = binascii.hexlify(binascii.unhexlify(e2.get())[::-1])
    hashMerkleRoot = binascii.hexlify(binascii.unhexlify(e3.get())[::-1])
    time = binascii.hexlify(binascii.unhexlify(e4.get())[::-1])
    bits = binascii.hexlify(binascii.unhexlify(e5.get())[::-1])
    nonce = binascii.hexlify(binascii.unhexlify(hex(int(0x100000000)+int(e6.get()))[-8:])[::-1])
    header = version+hashPrevBlock+hashMerkleRoot+time+bits+nonce
    header = binascii.unhexlify(header)
    hash = hashlib.sha256(hashlib.sha256(header).digest()).digest()
    hash = binascii.hexlify(hash)
    hash = binascii.hexlify(binascii.unhexlify(hash)[::-1])
    l7.config(text="Block Hash: "+str(hash))

label = tkinter.Label(window, text="Please enter correct values")
l1 = tkinter.Label(window, text="version: ")
l2 = tkinter.Label(window, text="hashPrevBlock: ")
l3 = tkinter.Label(window, text="hashMerkleRoot: ")
l4 = tkinter.Label(window, text="time: ")
l5 = tkinter.Label(window, text="bits: ")
l6 = tkinter.Label(window, text="nonce: ")
l7 = tkinter.Label(window, text="")
l8 = tkinter.Label(window, text="POC: kyusub.hwang.dev@gmail.com")

e1 = tkinter.Entry(window)
e2 = tkinter.Entry(window)
e3 = tkinter.Entry(window)
e4 = tkinter.Entry(window)
e5 = tkinter.Entry(window)
e6 = tkinter.Entry(window)

label.grid(row=0, column=0)

l1.grid(row=1, column=0)
l2.grid(row=2, column=0)
l3.grid(row=3, column=0)
l4.grid(row=4, column=0)
l5.grid(row=5, column=0)
l6.grid(row=6, column=0)
l7.grid(row=8, column=0, columnspan=3)
l8.grid(row=9, column=0)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)
e5.grid(row=5, column=1)
e6.grid(row=6, column=1)

button1 = tkinter.Button(window, command = check, width=15, text="check")
button1.grid(row=7, column=0)

window.mainloop()
