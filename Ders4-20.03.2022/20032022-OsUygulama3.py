import os
try:
    os.mkdir("Elma")
except FileExistsError:
    print("Zaten bu isimle bir klasör bulunmakta.")