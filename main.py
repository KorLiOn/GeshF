import hashlib

def short_sha_n(input_bytes, n):
    # Крок 1: Обчислити SHA-512 геш від масиву байтів x
    sha512_hash = hashlib.sha512(input_bytes).digest()

    # Крок 2: Взяти найменші n бітів від вектору T
    byte_index = n // 8  # Кількість байтів, яку нам потрібно
    bit_offset = n % 8   # Кількість бітів в останньому байті
    if bit_offset == 0:
        result_bytes = sha512_hash[:byte_index]
    else:
        last_byte = sha512_hash[byte_index]
        mask = 0xFF >> (8 - bit_offset)  # Маска для отримання останніх bit_offset бітів
        result_bytes = sha512_hash[:byte_index] + bytes([last_byte & mask])

    # Крок 3: Повернути H
    return result_bytes

# Приклад використання
input_data = b"Hello, World!"  # Вхідний масив байтів
n = 64  # Довжина вихідного вектора в бітах
hashed_result = short_sha_n(input_data, n)
print(hashed_result.hex())  # Вивести результат у вигляді шістнадцяткового рядка
//https://drive.google.com/file/d/1_IxZuXhKTpWWzVhM7ez7HpnAzJSmynVb/edit