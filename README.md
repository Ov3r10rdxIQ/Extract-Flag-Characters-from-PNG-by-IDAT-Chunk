# Extract-Flag-Characters-from-PNG-by-IDAT-Chunk

## Description

This code snippet is designed to extract flag characters from a PNG file by analyzing the IDAT chunks. It iterates through the bytes of the PNG file and identifies the start of each IDAT chunk. For each IDAT chunk found, it extracts the byte preceding it and interprets it as a character, appending it to the flag string. The resulting flag is then returned.

## Summary

This code performs a basic extraction of flag characters from a PNG file based on their position relative to IDAT chunks. It can be useful for simple steganography challenges where the flag is concealed within the structure of the PNG file.
I Used it in the RingZer0 ctf, The Sloth Challenge.
Star if you like it.
