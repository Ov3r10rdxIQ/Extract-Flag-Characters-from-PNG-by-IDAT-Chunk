### by Ov3r10rdxIQ, in 05/06/2024
###

def extract_flag_from_png(png_file):
    flag = ""
    with open(png_file, "rb") as file:
        data = file.read()
        i = 0
        while i < len(data):
            # Check if the current position starts an IDAT chunk
            if data[i:i+4] == b'\x49\x44\x41\x54':
                # Extract the character before the IDAT chunk
                flag += chr(data[i-1])
            i += 1
    return flag

# Usage
png_file = "hey.png"  # Replace with the path to your PNG file
flag = extract_flag_from_png(png_file)
print("Flag:", flag)

