Usage:
py -m AffineCipher -key <a b> [-encrypt | -decrypt] -in <input_file> -out <output_file>
eg.
py -m AffineCipher -key 1 8 -encrypt -in plaintext.txt -out ciphertext.txt
py -m AffineCipher -key 1 8 -decrypt -in ciphertext.txt -out decrypted.txt
py -m AffineCipher -key 3 8 -encrypt -in hello.txt -out byebye.txt
py -m AffineCipher -key 3 8 -decrypt -in byebye.txt -out helloagain.txt

Used internal libraries:
argparse, sys

Used external libraries:
-

Written and interpreted in Python 3.7.4, Tested on Windows 10 Pro Version 2004 Build 19041.329

Python environment variable will have to be set in PATH in order for python command to work (or call python.exe with it's absolute path).
If not set, set the following in command prompt

SET PATH=PATH;<PATH_TO_PYTHON>
eg. SET PATH=PATH;%LOCALAPPDATA%\Programs\Python\Python37-32;

It is recommended to place your input files into the same directory as myProgram.py and output files are saved to the same directory unless an absolute path is entered.