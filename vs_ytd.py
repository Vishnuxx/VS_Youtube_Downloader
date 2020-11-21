import pafy
import os
import shutil as sh

os.system('clear')

print(r"""░░░░░░░░░░░░░░░░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄░░
██░░██░░░░░░░░░░░▄█░░░░░░████░░████████▄
██▄▄██░░░░░░░░░░░████░░██████░░█████████
▀████▀░████░█░░█░████░░█░██░█░▄▄░█░░▄▄██
░░██░░░█░░█░█▄▄█░████░░█░░░░█░▀▀░█░░▄▄██
░░██░░░████░████░▀███▄▄█▄▄▄▄█▄▄▄▄█▄▄▄▄█▀
░░░░░░░░░░░░░░░░░░░▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀░░
""")
print(r"""
█▀▄ █▀█ █░█░█ █▄░█ █░░ █▀█ ▄▀█ █▀▄ █▀▀ █▀█
█▄▀ █▄█ ▀▄▀▄▀ █░▀█ █▄▄ █▄█ █▀█ █▄▀ ██▄ █▀▄
""")
print("\n Developer : V!$#nuxx")
print("\n")
print("__________Download Mode__________")
print("\n 1. Download to Current Directory")
print("\n 2. Download to Target Directory")
print("\n")

mode = input("Select Download Mode : ")

url = input("Paste Your Video URL : ")

if mode == "2":
  outputdir = input("Enter Output Directory : ")

print("Processing...")
video = pafy.new(url)

streams = video.streams

for i in streams:
  print(i)

best = video.getbest()
print(best.resolution , best.extension)

cmand = input("Are you sure that you wanna download this video? y / n>")

if cmand == "y":
  best.download()
  currentfile = best.generate_filename()

  if mode == "2":
    sh.move(currentfile , outputdir)

  print("Video Downloaded successfully!!!")

if cmand == "n":
  print("Download cancelled")