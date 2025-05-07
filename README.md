# checksum
Verify file integrity and generate checksum hash values.
---

For a long time I wanted to have a simple and at the same time effective tool to verify file's integrity using the given checksum values. That is why I developed my own CLI program, written in *Python*, that does exactly this: verifies the integrity of a file using a generated checksum hash value. **chksum** takes the *file* as a command line argument and the hash value specified with the argument `-v, --value`. The program determines the type of the hash value by itself and does the ingrity check. The supported hash types are: **md5**, **sha1**, **sha224**, **sha256**, **sha384**, and **sha512**.

*usage example:*
`$ chksum FILE -v HASH_VALUE`

The output of `--help` optional argument:
```
chksum - verify file integrity

positional arguments:
  FILE                  specify file

options:
  -h, --help            show this help message and exit
  -v HASH_VALUE, --value HASH_VALUE
                        enter hashed value
  --version             show program version
```

---

I have also made another CLI program to generate checksum hash value(s), **mksum**. It also supports **md5**, **sha1**, **sha224**, **sha256**, **sha384**, and **sha512**. **mksum** can generate a hash of a single type, for instance *sha256* or can use *all* the supported types at once.

*usage example:*
`$ mksum FILE --hash HASH_TYPE | all`

The output of `--help` optional argument:
```
Generate checksum hash values

positional arguments:
  file         specify file

options:
  -h, --help   show this help message and exit
  --hash hash  specify hash type
  --list       show supported hash types
  --version    show program version
```
