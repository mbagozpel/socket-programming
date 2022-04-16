import socket

HEADER_LENGTH = 10
a = 250
b = 479

lower_case = {chr(i+71):i for i in range(26,52)}
upper_case = {chr(i+65):i for i in range(0,26)}
letters = upper_case | lower_case
letters_list = list(letters.keys())

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # for reconnection purposes

server_socket.bind((socket.gethostname(), 1234))
server_socket.listen(1)



def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)

        if not len(message_header):
            return False

        message_length = int(message_header.decode('utf-8').strip())
        return {"header": message_header, "data": client_socket.recv(message_length)}

    except Exception as e:
        return False

def decrypt_cipher(ciphertext, k_prime):
    decryption = ''

    for i in range(len(ciphertext)):
        y = ciphertext[i]

        if y in letters_list:
            y_index = letters[y]
            x = (y_index - k_prime) % 52
            decryption += letters_list[x]

        else:
            decryption += y

    return decryption



clt, adrs = server_socket.accept()
received_k = receive_message(clt)
k = f"{received_k['data'].decode('utf-8')}"
k_prime = (a - int(k) + b) % 52
print(k_prime)

while True:
    message = receive_message(clt)
    message_received = f"{message['data'].decode('utf-8')}"
    message_decrypted = decrypt_cipher(message_received, k_prime)
    print(message_received, message_decrypted)

    msg = "Message received".encode('utf-8')
    msg_header = f"{len(msg):<{HEADER_LENGTH}}".encode('utf-8')
    clt.send(msg_header + msg)




