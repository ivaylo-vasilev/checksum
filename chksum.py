#!/usr/bin/env python3

import hashlib
import argparse
import sys
import os
from colorama import init, Fore

init(autoreset=True)
OK = str(Fore.GREEN + "[+]" + Fore.RESET)
NO = str(Fore.RED + "[-]" + Fore.RESET)
ERR = str(Fore.RED + "Error:" + Fore.RESET)

BANNER = """

            ##########################
                   chksum 1.0.6
                ------------------
                        *
              (c)2025 Ivaylo Vasilev
            ##########################
            
        """

# Parse the arguments from command line
parser = argparse.ArgumentParser(prog="chksum", description="chksum - verify file integrity", epilog="(c) Ivaylo Vasilev")
parser.add_argument("file", nargs="?", metavar="FILE", help="specify file")
parser.add_argument("-v", "--value", metavar="HASH_VALUE", help="enter hashed value")
parser.add_argument("--version", action="version", version="%(prog)s 1.0.6", help="show program version")
args = parser.parse_args()


def main():
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    
    # Perform error checking
    if not args.file:
        sys.exit(f"{ERR} Missing required argument: FILE")
    if not os.path.isfile(args.file):
        sys.exit(f"{ERR} {args.file} is not a file")
    if not args.value:
        sys.exit(f"{ERR} Missing required argument: HASH_VALUE")
    
    print(BANNER)
    
    # Getting name and size information for the file
    file_name = os.path.basename(args.file)
    file_size = os.path.getsize(args.file)

    print("File information:")
    print("=================")
    print(f"Name: {file_name}")
    print(f"Size: {float(file_size / 1024 / 1024):.2f} MB")
    print("")
    print("Checking file ...")
    print("")

    # Open the file and read as binary to create a proper format for hash value library; needs data as bytes
    with open(args.file, "rb") as f:
        file = f.read()
    hashvalue = args.value

    # Specify the hash algorithm
    if len(args.value) == 32:
        print("Hash: MD5")
        print("=========")
        check = md5sum(file, hashvalue)
        if check == True:
            print(f"{OK} File integrity confirmed")
        else:
            print(f"{NO} File integrity not confirmed")
    elif len(args.value) == 40:
        print("Hash: SHA-1")
        print("===========")
        check = sha1sum(file, hashvalue)
        if check == True:
            print(f"{OK} File integrity confirmed")
        else:
            print(f"{NO} File integrity not confirmed")
    elif len(args.value) == 56:
        print("Hash: SHA-224")
        print("=============")
        check = sha224sum(file, hashvalue)
        if check == True:
            print(f"{OK} File integrity confirmed")
        else:
            print(f"{NO} File integrity not confirmed")
    elif len(args.value) == 64:
        print("Hash: SHA-256")
        print("=============")
        check = sha256sum(file, hashvalue)
        if check == True:
            print(f"{OK} File integrity confirmed")
        else:
            print(f"{NO} File integrity not confirmed")
    elif len(args.value) == 128:
        print("Hash: SHA-512")
        print("=============")
        check = sha512sum(file, hashvalue)
        if check == True:
            print(f"{OK} File integrity confirmed")
        else:
            print(f"{NO} File integrity not confirmed")
    else:
        sys.exit(f"{ERR} Unknown hash type for value: {args.value}")


def md5sum(file, hashvalue):
    hashobject = hashlib.md5()
    hashobject.update(file)

    if hashobject.hexdigest() == hashvalue:
        return True
    else:
        return False


def sha1sum(file, hashvalue):
    hashobject = hashlib.sha1()
    hashobject.update(file)

    if hashobject.hexdigest() == hashvalue:
        return True
    else:
        return False


def sha224sum(file, hashvalue):
    hashobject = hashlib.sha224()
    hashobject.update(file)

    if hashobject.hexdigest() == hashvalue:
        return True
    else:
        return False


def sha256sum(file, hashvalue):
    hashobject = hashlib.sha256()
    hashobject.update(file)

    if hashobject.hexdigest() == hashvalue:
        return True
    else:
        return False


def sha512sum(file, hashvalue):
    hashobject = hashlib.sha512()
    hashobject.update(file)

    if hashobject.hexdigest() == hashvalue:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
