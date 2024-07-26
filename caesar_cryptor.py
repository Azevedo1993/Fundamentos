
def encrypt(text, number_of_switches):
   encrypted_text = ""
   for character in text:
       encrypted_text = encrypted_text + chr((ord(character) - ord('a') + number_of_switches) % 26 + ord('a'))
   print(encrypted_text)

def decrypt(text):
    decrypted_text = ""
    for character in text:
        decrypted_text = decrypted_text + chr((ord(character) - ord('a') - 3) % 26 + ord('a'))
    print(decrypt)

def get_user_input():
    input_text = input("Hide: ")
    input_switches = int(input("Number of switches: "))
    encrypt(input_text, input_switches)

get_user_input()
