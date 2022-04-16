import socket
import sys
from random import randint

HEADER_LENGTH = 10
a = 250
b = 479

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(), 1234))

lower_case = {chr(i+71):i for i in range(26,52)}
upper_case = {chr(i+65):i for i in range(0,26)}
letters = upper_case | lower_case
letters_list = list(letters.keys())


def generate_non_zero_k():
    k_prime = 0

    while k_prime == 0:
        k = randint(1, 1000000)  # generate random number
        k_prime = (a - k + b) % 52
        print(k_prime)

    return k

def shift_cipher(plaintext, k_prime):
    ciphertext = ''
    #Loop through the plain text
    for i in range(len(plaintext)):
        x = plaintext[i]

        if x in letters_list:
            x_index = letters[x]
            y = (x_index + k_prime) % 52
            ciphertext += letters_list[y]

        else:
            ciphertext += x

    return ciphertext


k = generate_non_zero_k()
send_k = str(k).encode('utf-8')
send_k_header = f"{len(send_k):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(send_k_header + send_k)

while True:
    message = input()

    if message:

        k_prime = (a - k + b) % 52
        print(k_prime)
        ciphertext = shift_cipher(message, k_prime)
        print(message, ciphertext)
        send_ciphertext = ciphertext.encode('utf-8')
        ciphertext_header = f"{len(ciphertext):<{HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(ciphertext_header + send_ciphertext)

    # receive message
    acknowledgement_header = client_socket.recv(HEADER_LENGTH)
    if not len(acknowledgement_header):
        print("connection closed by the server")
        sys.exit()

    acknowledgement_length = int(acknowledgement_header.decode('utf-8').strip())
    acknowledgement = client_socket.recv(acknowledgement_length)
    print(acknowledgement.decode('utf-8'))

