# MultiLayerCipher
## Overview
This project is a modular text encryption and decryption system developed in Python.
It combines multiple ASCII-based encryption algorithms into a randomized multi-layer pipeline with fully reversible decryption.

The system is designed to evolve into a more structured and extensible cryptographic engine.

## Features
- Multi-layer encryption pipeline
- Randomized cipher selection per layer
- Deterministic and fully reversible decryption
- Full printable ASCII (32-126) support
- CLI-based interactive interface

## Implemented Algorithms
- Atbash (ASCII adapted)
- Affine Cipher (mod 95)
- Vigenère-style ASCII shifting
- Rail Fence Cipher
- Polybius Square (10x10 ASCII adaptation)
All algorithms operate on the full printable ASCII range.

## Randomized Layering Example
Input:
Hello World!

Encrypted (Run 1):
SPp>PC*E+?pEPCpC*3p>P<%>p?*Ep>+3^E%!pK+K%C

Encrypted (Run 2):
rFrs'l:.7'F>''YYM:.c%"o'Ks!YH.M:"]

Encrypted (Run 3):
^VC05H2'pCMf2XREooK:2r\f)du-\rSfWdB[SN\oxdB['?S:%suWRJfew%bf\_s'Vo

Decrypted (Run 1 / Run 2 / Run 3):
Hello World!

## How to Run
```bash
python cipher.py
