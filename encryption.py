# Read q, p, s, and the plaintext message from a file
with open("input.txt", "r") as file:
    q = int(file.readline().strip())  # Read q (first line)
    p = int(file.readline().strip())  # Read p (second line)
    s = int(file.readline().strip())  # Read s (third line)
    flag = file.readline().strip()  # Read the flag (fourth line)

# Compute n = p * q 
n = p * q

# Generate the key using BBS 
x = s
key = f"{int(''.join(str((x := (x * x) % n) & 1) for _ in range(336)), 2):032x}"  

# Encrypt the message using XOR
flag_hex = flag.encode('utf-8').hex()
encrypted_flag = ''.join(f"{int(flag_hex[i], 16) ^ int(key[i], 16):01x}" for i in range(len(flag_hex)))

# Write the encrypted flag to a new file
with open("encrypted_flag.txt", "w") as file:
    file.write(encrypted_flag)