#python -m pickletools -a .\out.pickle

import pickle

class FlagPrinter():
    def __str__(self):
        print(bytes(self.flag))


output = pickle.load(open("out.pickle", "rb"))

print(output)