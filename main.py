def shifrCezar(txt, kody):
    result = txt

    for kod in kody:
        result = _shifrCezar(result, kod)

    return result

def deshifrCezar(txt, kody):
    result = txt

    for kod in reversed(kody):  # Используем reversed, чтобы расшифровать в обратном порядке
        result = _shifrCezar(result, -kod)

    return result

def _shifrCezar(txt, kod):
    encrypted_text = ""

    for char in txt:
        if char.isalpha():
            start = ord('А') if char.isupper() else ord('а')
            shifted_char = chr((ord(char) - start + kod) % 33 + start)
            encrypted_text += shifted_char
        else:
            encrypted_text += char

    return encrypted_text

def main():
    while True:
        choice = input("Выберите действие (1 - Зашифровать, 2 - Расшифровать, 0 - Выйти): ")

        if choice == "0":
            print("Программа завершена.")
            break

        elif choice == "1":
            txt_to_encrypt = input("Введите текст для шифрования: ")
            shifts = [int(x.strip()) for x in input("Введите коды сдвига через запятую: ").split(',')]
            encrypted_text = shifrCezar(txt_to_encrypt, shifts)
            print("Зашифрованный текст:", encrypted_text)

        elif choice == "2":
            txt_to_decrypt = input("Введите текст для расшифровки: ")
            shifts = [int(x.strip()) for x in input("Введите коды сдвига через запятую: ").split(',')]
            decrypted_text = deshifrCezar(txt_to_decrypt, shifts)
            print("Расшифрованный текст:", decrypted_text)

        else:
            print("Некорректный выбор.")

if __name__ == "__main__":
    main()
