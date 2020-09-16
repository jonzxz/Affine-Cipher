# Affine Cipher for CSCI361 S3 2020
# Developed and tested in Python 3.7.2, Windows 10 Pro Version 2004
# Written by Jon K, 2020

import argparse
import sys


def main():
    cli_args = parse_cli_args()
    # Converts key to int
    key = [int(i) for i in cli_args[0]]
    cipher_func = cli_args[1]
    input_file = cli_args[2]
    output_file = cli_args[3]
    output_text = []
    alphabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    try:
        with open(input_file, 'r') as input_file:
            input_data = input_file.read()

        if cipher_func == "encrypt":
            for c in input_data:
                if c.isalpha():
                    new_idx = affine_encrypt(key, char_alpha_to_idx(c))
                    output_text.append(alphabets[new_idx])
                else:
                    output_text.append(c)

        if cipher_func == "decrypt":
            for c in input_data:
                if c.isalpha():
                    new_idx = affine_decrypt(key, char_alpha_to_idx(c))
                    output_text.append(alphabets[new_idx])
                else:
                    output_text.append(c)

        with open(output_file, 'w') as output_file:
            output_file.write(''.join(output_text))
            print("{0} complete and written into designated output file".format(cipher_func))
    except FileNotFoundError:
        print("Input file does not exist or not in the current directory, please enter a valid input file!\n")


# Function to parse command line arguments
def parse_cli_args():
    parser = argparse.ArgumentParser("affine_cipher")
    parser.add_argument("-key", nargs='+', help="key pair separated by space, eg. 3 8", required=True, dest='key')
    parser.add_argument("-encrypt", action='store_true', default=False, dest='encrypt')
    parser.add_argument("-decrypt", action='store_true', default=False, dest='decrypt')
    parser.add_argument("-in", required=True, help="input file name", dest='input_file')
    parser.add_argument("-out", required=True, help="output file name", dest='output_file')
    args = parser.parse_args()

    cipher_func = None

    if not len(args.key) == 2:
        print("Invalid key size, only enter 2 values!")
        sys.exit(0)

    # If alpha of key is not relatively prime to 26
    if (int(args.key[0])) not in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
        print("Invalid key, please use only numbers relatively prime to 26 for alpha (a, b)")
        sys.exit(0)

    # If both or neither functions are entered
    if args.encrypt and args.decrypt or (not args.encrypt and not args.decrypt):
        print("Invalid encryption or decryption option, please enter either -encrypt or -decrypt only!")
        sys.exit(0)

    # Sets cipher_func to determine program type, to encrypt or decrypt
    if args.encrypt and not args.decrypt:
        cipher_func = "encrypt"
    elif args.decrypt and not args.encrypt:
        cipher_func = "decrypt"

    # Returns command line arguments as a list
    cli_args = [args.key, cipher_func, args.input_file, args.output_file]
    return cli_args


# Function to determine the value of a^-1 where a^-1 is the multiplicative inverse of a mod 26. Using ta(mod26) = 1,
# the value t is incremented from 1 to 26 (n alphabets) as a way of brute forcing to get a value t which is = to a^-1
def find_inverse(alpha):
    for t in range(1, 26):
        if ((t * alpha) % 26) == 1:
            return t


# Encryption function for affine cipher where the provided formula is
# C = (aM + b) mod 26, where a is key[0] and  b is key[1]
# The if condition here is used to see if the given char (in it's index form from the list) is an upper-case. If it is,
# It is then returned as an upper-case which will be initially removed due to %26 in the provided formula.
def affine_encrypt(key, char_idx):
    # c = aM + b mod 26
    cipher = ((key[0] * char_idx) + key[1]) % 26
    if char_idx >= 26:
        cipher = cipher + 26
    return cipher


# Decryption function for affine cipher where the general formula is
# M = a^-1 (C - b) mod 26.
# The if condition here is used to see if the given char (in it's index form from the list) is an upper-case. If it is,
# It is then returned as an upper-case which will be initially removed due to %26 in the general formula.
def affine_decrypt(key, char_idx):
    # M = t (C - b) mod 26 where t = a^-1 as calculated in find_inverse
    plain = (find_inverse(key[0]) * (char_idx - key[1])) % 26
    if char_idx >= 26:
        plain = plain + 26
    return plain


# Function to convert a character to an index which corresponds to a list of alphabetical characters a-zA-Z
def char_alpha_to_idx(chr):
    # Upper-cased characters - the rational for -39 is to obtain the index for my alphabets list
    # Since a-z is 0 - 25, A-Z is 26 - 51. For example, if the character is 'A' (65), a -39 is used to obtain index 26
    # of the list which is A. 'B' (66), -39 to get 27 which is B in the list, so on..
    if 65 <= ord(chr) <= 90:
        return (ord(chr) - 39)
    # Lower-cased characters - the rational for -39 is to obtain the index for my alphabets list
    # where the int returned correspond to the 0-25th character of the list
    if 97 <= ord(chr) <= 122:
        return (ord(chr) - 97)


main()
