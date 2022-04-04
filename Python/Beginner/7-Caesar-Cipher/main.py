alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("Welcome to Josh's Caesar Cipher. This allows you to encrypt and decrypt messages by shigting character positions.")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number UNDER 25:\n"))

def caesar(usertext=text, usershift=shift, userdirection=direction):
    if direction == "encode":       
        encrypted_pool = []
        for letter_being_checked in usertext:
            if letter_being_checked in alphabet:
                letterposition = alphabet.index(letter_being_checked)
                if (letterposition + usershift) < len(alphabet):
                    encrypted_pool.append(alphabet[letterposition + usershift])
                elif (letterposition + usershift) >= len(alphabet):
                    excess_letterposition = ((letterposition + usershift) - (len(alphabet)))
                    encrypted_pool.append(alphabet[excess_letterposition])
            else: 
                encrypted_pool.append(letter_being_checked)
        encoded_message = "".join(encrypted_pool)
        print(f"The encoded message is {encoded_message}")    
        
    if direction == "decode":
        decrypted_pool = []
        for letter_being_checked in usertext:
            if letter_being_checked in alphabet:
                letterposition = alphabet.index(letter_being_checked)
                if (letterposition - usershift) >= 0:
                    decrypted_pool.append(alphabet[letterposition - usershift])
                elif (letterposition - usershift) < 0:
                    excess_letterposition = ((letterposition - usershift) + (len(alphabet)))
                    decrypted_pool.append(alphabet[excess_letterposition])
            else: 
                decrypted_pool.append(letter_being_checked)
        decoded_message = "".join(decrypted_pool)
        print(f"The decoded message is {decoded_message}")

caesar()
while input("Want to run it again? Yes / No ").lower() == "yes":
    caesar()