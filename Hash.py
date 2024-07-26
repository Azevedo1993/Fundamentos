import hashlib

def generate_hash_code(password):
    hash_object = hashlib.sha256()
    byte_input = password.encode()
    hash_object.update(byte_input)
    hash_code = hash_object.hexdigest()
    print(hash_code)

generate_hash_code("a")
