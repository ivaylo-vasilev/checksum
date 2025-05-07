#!/usr/bin/env python3

import hashlib
import argparse
import sys
import os

parser = argparse.ArgumentParser(prog="mksum", description="Generate checksum hash values", epilog="(c) Ivaylo Vasilev")
parser.add_argument("file", nargs="?", help="specify file")
parser.add_argument("--hash", metavar="hash", default="md5", help="specify hash type")
parser.add_argument("--list", action="store_true", help="show supported hash types")
parser.add_argument("--version", action="version", version="%(prog)s 1.0.2", help="show program version")
args = parser.parse_args()


def main():
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    elif args.list:
        print("mksum: --hash md5 | sha1 | sha224 | sha256 | sha384 | sha512 | all")
        sys.exit(0)

    if not os.path.isfile(args.file):
        sys.exit("error: %s is not a file" % args.file)

    file_name = os.path.basename(args.file)
    file_size = os.path.getsize(args.file)
    file_size = float(file_size / 1024 / 1024)

    print("Generating checksum hash value(s)")
    print("=================================")
    print("File name: %s" % file_name)
    print("File size: %.2f MB" % file_size)
    print("")

    with open(args.file, "rb") as f:
        file = f.read()
    
    if args.hash == "md5":
        print(*md5_hash(file))
        print("")
    elif args.hash == "sha1":
        print(*sha1_hash(file))
        print("")
    elif args.hash == "sha224":
        print(*sha224_hash(file))
        print("")
    elif args.hash == "sha256":
        print(*sha256_hash(file))
        print("")
    elif args.hash == "sha384":
        print(*sha384_hash(file))
        print("")
    elif args.hash == "sha512":
        print(*sha512_hash(file))
        print("")
    elif args.hash == "all":
        print(*md5_hash(file))
        print("")
        print(*sha1_hash(file))
        print("")
        print(*sha224_hash(file))
        print("")
        print(*sha256_hash(file))
        print("")
        print(*sha384_hash(file))
        print("")
        print(*sha512_hash(file))
        print("")
    else:
        sys.exit("error: unknown or unsupported hash type '%s'" % args.hash)


def md5_hash(file):
    hashobject0 = hashlib.md5()
    hashobject0.update(file)

    return "MD5    :", hashobject0.hexdigest()


def sha1_hash(file):
    hashobject1 = hashlib.sha1()
    hashobject1.update(file)

    return "SHA-1  :", hashobject1.hexdigest()


def sha224_hash(file):
    hashobject2 = hashlib.sha224()
    hashobject2.update(file)

    return "SHA-224:", hashobject2.hexdigest()


def sha256_hash(file):
    hashobject3 = hashlib.sha256()
    hashobject3.update(file)

    return "SHA-256:", hashobject3.hexdigest()


def sha384_hash(file):
    hashobject4 = hashlib.sha384()
    hashobject4.update(file)

    return "SHA-384:", hashobject4.hexdigest()


def sha512_hash(file):
    hashobject5 = hashlib.sha512()
    hashobject5.update(file)

    return "SHA-512:", hashobject5.hexdigest()


if __name__ == "__main__":
    main()
