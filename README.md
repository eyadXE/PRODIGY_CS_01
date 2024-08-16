# Caesar Cipher Python Program

## Overview

This Python program implements the Caesar Cipher, a simple encryption technique where each letter in a text is shifted by a fixed number of positions in the alphabet. This program allows users to both encrypt and decrypt messages using the Caesar Cipher algorithm.

## How It Works

The Caesar Cipher works by shifting each letter in the plaintext by a specified number of positions down the alphabet. For example, with a shift of 3:

- 'A' becomes 'D'
- 'B' becomes 'E'
- ...
- 'Z' wraps around to 'C'

### Encryption

The encryption process shifts each letter in the input text forward by the specified shift key. Non-alphabetic characters (such as spaces, punctuation, and numbers) remain unchanged.

### Decryption

The decryption process shifts each letter in the input text backward by the specified shift key to recover the original message.

## Features

- **Encrypt Messages**: Input a message and a shift key to encrypt the text.
- **Decrypt Messages**: Input an encrypted message and the same shift key to decrypt and recover the original text.
- **Handles Upper and Lower Case**: The program distinguishes between upper and lower case letters, preserving the case of each letter.
- **Preserves Non-Alphabetic Characters**: Non-alphabetic characters like spaces, punctuation, and numbers are not altered during encryption or decryption.

## Usage
