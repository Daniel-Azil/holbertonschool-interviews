# UTF-8 Validation Method

## Introduction
This repository contains a Python method that determines if a given data set represents a valid UTF-8 encoding. The method `validUTF8(data)` takes a list of integers, where each integer represents one byte of data, and returns `True` if the data is a valid UTF-8 encoding, and `False` otherwise.

## UTF-8 Encoding Overview
UTF-8 is a variable-width character encoding used for electronic communication. It can encode characters in one to four bytes. The following rules apply to determine the validity of a UTF-8 encoding:

- For a 1-byte character, the first bit is a 0, followed by its Unicode code.
- For an n-byte character (n > 1), the first byte starts with n bits set to 1, followed by a 0 bit, and the next n-1 bytes start with 10.
