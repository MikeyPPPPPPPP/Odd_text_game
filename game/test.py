print("\033[0;37;40m Normal text\n")
print("\033[2;37;40m Underlined text\033[0;37;40m \n")
print("\033[1;37;40m Bright Colour\033[0;37;40m \n")
print("\033[3;37;40m Negative Colour\033[0;37;40m \n")
print("\033[5;37;40m Negative Colour\033[0;37;40m\n")

print("\033[1;37;40m \033[2;37:40m TextColour BlackBackground          TextColour GreyBackground                WhiteText ColouredBackground\033[0;37;40m\n")
print("\033[1;30;40m Dark Gray      \033[0m 1;30;40m            \033[0;30;47m Black      \033[0m 0;30;47m               \033[0;37;41m Black      \033[0m 0;37;41m")
print("\033[1;31;40m Bright Red     \033[0m 1;31;40m            \033[0;31;47m Red        \033[0m 0;31;47m               \033[0;37;42m Black      \033[0m 0;37;42m")
print("\033[1;32;40m Bright Green   \033[0m 1;32;40m            \033[0;32;47m Green      \033[0m 0;32;47m               \033[0;37;43m Black      \033[0m 0;37;43m")
print("\033[1;33;40m Yellow         \033[0m 1;33;40m            \033[0;33;47m Brown      \033[0m 0;33;47m               \033[0;37;44m Black      \033[0m 0;37;44m")
print("\033[1;34;40m Bright Blue    \033[0m 1;34;40m            \033[0;34;47m Blue       \033[0m 0;34;47m               \033[0;37;45m Black      \033[0m 0;37;45m")
print("\033[1;35;40m Bright Magenta \033[0m 1;35;40m            \033[0;35;47m Magenta    \033[0m 0;35;47m               \033[0;37;46m Black      \033[0m 0;37;46m")
print("\033[1;36;40m Bright Cyan    \033[0m 1;36;40m            \033[0;36;47m Cyan       \033[0m 0;36;47m               \033[0;37;47m Black      \033[0m 0;37;47m")
print("\033[1;36;48m White          \033[0m 1;36;48m            \033[0;37;40m Light Grey \033[0m 0;37;40m               \033[0;37;48m Black      \033[0m 0;37;48m")

from tkinter import *#Tk, Text, TOP, BOTH, X, N, LEFT
from tkinter.ttk import *


class Example(Frame):

    def __init__(self):
        super().__init__()

        #self.initUI()


    #def initUI(self):
        self.newMessage = ""
        self.master.title("Michael")
        self.pack(fill=BOTH, expand=True)

        self.frame52 = Frame(self)
        self.frame52.pack(fill=BOTH)

        self.brutforce = Button(self.frame52, text="Brutforce", command=self.topbrute)
        self.brutforce.pack(side=LEFT)

        self.lbl42 = Button(self.frame52, text="shift",
                            command=self.shift_test)  # shiftcipher2)  # , command=shiftcipher)
        self.lbl42.pack(side=LEFT, anchor=N, padx=5, pady=5)



    def test(self):
        self.lisbox2.insert(1, str(self.entry1.get()))

    def shiftcipher(self):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        partialOne = ""
        partialTwo = ""
        newAlphabet = ""

        message = str(self.entry1.get())
        key = int(self.entry2.get())
        if key == 0:
            newAlphabt = alphabet
        elif key > 0:
            partialOne = alphabet[:key]
            partialTwo = alphabet[key:]

            newAlphabet = partialTwo + partialOne


        else:
            partialOne = alphabet[:(26 + key)]
            partialTwo = alphabet[(26 + key):]
            newAlphabet = partialTwo + partialOne

        myMessage = message

        for i in range(0, len(myMessage)):
            index = alphabet.find(myMessage[i])
            if index < 0:
                self.newMessage += myMessage[i]
                # print(newMessage)
            else:
                self.newMessage += newAlphabet[index]

        for k in range(len(alphabet)):
            newAlphabet = alphabet[k:] + alphabet[:k]
            attempt = ""
            for i in range(len(myMessage)):
                index = alphabet.find(myMessage[i])
                if index < 0:
                    attempt += myMessage[i]
                else:
                    attempt += newAlphabet[index]

            if k == key:
                self.lisbox.insert(0, "Key: " + str(k) + " - " + attempt)  # print("Key: " + str(k) + " - " + attempt)
            else:
                pass


    def shiftcipher2(self):
        """
        top = Toplevel()
        top.title("About this application...")
        top.geometry("200x100")

        msg = Message(self, text='about_message')
        msg.pack()

        button = Button(top, text="Dismiss")#, command=top.destroy)
        button.pack()
        """
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        partialOne = ""
        partialTwo = ""
        newAlphabet = ""

        message = str(self.entry1.get())
        key = 26 - int(self.entry2.get())
        if key == 0:
            newAlphabt = alphabet
        elif key > 0:
            partialOne = alphabet[:key]
            partialTwo = alphabet[key:]

            newAlphabet = partialTwo + partialOne


        else:
            partialOne = alphabet[:(26 + key)]
            partialTwo = alphabet[(26 + key):]
            newAlphabet = partialTwo + partialOne

        myMessage = message

        for i in range(0, len(myMessage)):
            index = alphabet.find(myMessage[i])
            if index < 0:
                self.newMessage += myMessage[i]
                # print(newMessage)
            else:
                self.newMessage += newAlphabet[index]

        for k in range(len(alphabet)):
            newAlphabet = alphabet[k:] + alphabet[:k]
            attempt = ""
            for i in range(len(myMessage)):
                index = alphabet.find(myMessage[i])
                if index < 0:
                    attempt += myMessage[i]
                else:
                    attempt += newAlphabet[index]
            if k == 0:
                self.lisbox2.insert(0, "Key: " + str(
                    k) + " - " + attempt)  # print("Key: " + str(k) + " - " + attempt)
            else:
                pass

    def shift_test(self):
        top = Toplevel(self)
        top.title("shift")
        top.geometry("350x350")



        self.master.title("Michael")
        self.pack(fill=BOTH, expand=True)

        self.frame1 = Frame(top)
        self.frame1.pack(fill=X)

        self.lbl1 = Label(self.frame1, text="shift cipher", width=16)
        self.lbl1.pack(side=LEFT, padx=5, pady=5)

        self.entry1 = Entry(self.frame1)
        self.entry1.pack(fill=X, padx=5, expand=True)

        self.frame2 = Frame(top)
        self.frame2.pack(fill=X)

        self.lbl2 = Label(self.frame2, text="num of shifts", width=16)
        self.lbl2.pack(side=LEFT, padx=5, pady=5)

        self.entry2 = Entry(self.frame2)
        self.entry2.pack(fill=X, padx=5, expand=True)

        self.frame3 = Frame(top)
        self.frame3.pack(fill=BOTH, expand=True)

        self.lbl3 = Button(self.frame3, text="Encrypt", command=self.shiftcipher)  # , command=shiftcipher)
        self.lbl3.pack(side=LEFT, anchor=N, padx=5, pady=5)

        self.lisbox = Listbox(self.frame3)
        self.lisbox.pack(fill=BOTH, pady=5, padx=5, expand=True)

        self.frame52 = Frame(top)
        self.frame52.pack(fill=BOTH)

        self.lbl42 = Button(self.frame52, text="Decrypt",
                            command=self.shiftcipher2)  # shiftcipher2)  # , command=shiftcipher)
        self.lbl42.pack(side=LEFT, anchor=N, padx=5, pady=5)

        self.lisbox2 = Listbox(self.frame52)
        self.lisbox2.pack(fill=BOTH, pady=5, padx=5, expand=True)





    def topbrute(self):
        topb = Toplevel(self)
        topb.title("Brute Force")
        topb.geometry("350x200")
        self.frameb1 = Frame(topb)
        self.frameb1.pack(fill=X)

        self.lab1 = Label(self.frameb1, text="Word to try:", width=16)
        self.lab1.pack(side=LEFT, padx=5, pady=5)

        self.entryb1 = Entry(self.frameb1)
        self.entryb1.pack(fill=X, padx=5, expand=True)

        self.frameb2 = Frame(topb)
        self.frameb2.pack(fill=X)

        self.butb2 = Button(self.frameb2, text="BruteForce", command=self.bruteF)#,command=self.shiftcipher2)  # shiftcipher2)  # , command=shiftcipher)
        self.butb2.pack(side=LEFT, anchor=N, padx=5, pady=5)

        self.lisbox3 = Listbox(self.frameb2)
        self.lisbox3.pack(fill=BOTH, pady=5, padx=5, expand=True)


    def bruteF(self):
        b1secretMessage = ""
        b1alphabet = 'abcdefghijklmnopqrstuvwxyz'
        b1partialOne = ""
        b1partialTwo = ""
        b1newAlphabet = ""

        b1message = str(self.entryb1.get())

        b1key = int(5)

        if b1key == 0:
            b1newAlphabt = b1alphabet
        elif b1key > 0:
            b1partialOne = b1alphabet[:b1key]
            b1partialTwo = b1alphabet[b1key:]

            b1newAlphabet = b1partialTwo + b1partialOne
            #print(b1newAlphabet)


        else:
            b1partialOne = b1alphabet[:(26 + b1key)]
            b1partialTwo = b1alphabet[(26 + b1key):]
            b1newAlphabet = b1partialTwo + b1partialOne

            # print(newAlphabet)

        b1myMessage = b1message
        b1newMessage = ""
        for i in range(0, len(b1myMessage)):
            index = b1alphabet.find(b1myMessage[i])
            if index < 0:
                b1newMessage += b1myMessage[i]
                # print(newMessage)
            else:
                b1newMessage += b1newAlphabet[index]
                # print(newMessage)



        for b1key in range(len(b1alphabet)):
            b1newAlphabet = b1alphabet[b1key:] + b1alphabet[:b1key]
            b1attempt = ""
            for i in range(len(b1myMessage)):
                index = b1alphabet.find(b1myMessage[i])
                if index < 0:
                    b1attempt += b1myMessage[i]
                else:
                    b1attempt += b1newAlphabet[index]
                    if len(b1attempt) == len(b1secretMessage):
                        self.lisbox3.insert(0, "Key: " + str(b1key) + " - " + b1attempt)
                        print("Key: " + str(b1key) + " - " + b1attempt)
                    else:
                        pass


def main():

    root = Tk()
    root.geometry("200x100")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()