Это шифровальщик текста, основанный на цезарь шифре (сдвиге). Программа предоставляет возможность зашифровать и расшифровать текст с помощью заданных кодов сдвига.

Для начала, пользователю предлагается выбрать действие: 1 - зашифровать текст, 2 - расшифровать текст, 0 - выйти из программы. 

Если пользователь выбирает 1, программа просит ввести текст для шифровки. Например, "привет, это супер важный текст, который не должен быть расшифрован". Затем пользователю предлагается ввести коды сдвига через запятую. Например, "19,16,4,5,3,6,13,16,17,19,3,4,25,19,12,9,3,4,5,6,7,8". 

Текст сдвигается поочередно на каждый из введенных кодов сдвига. Сначала текст сдвигается на 19, затем на 16, после чего на 4, и так далее. 

В итоге получается зашифрованный текст: "ииаыюк, хкж йлзюи ыщяеуб кювйк, вжкжиуб ею эжгяюе ъукф ищйрамижыще".

Если пользователь выбирает 2, программа просит ввести текст для расшифровки. Например, "ииаыюк, хкж йлзюи ыщяеуб кювйк, вжкжиуб ею эжгяюе ъукф ищйрамижыще". Затем пользователю предлагается ввести коды сдвига через запятую, аналогично "19,16,4,5,3,6,13,16,17,19,3,4,25,19,12,9,3,4,5,6,7,8". 

Шифротекст расшифровывается таким же образом, как он был зашифрован. Применяются коды сдвига в обратном порядке. 

В итоге получается расшифрованный текст: "привет, это супер важный текст, который не должен быть расшифрован".

Для запуска программы необходимо запустить пайтон скрипт - main.py"

или запустить "shifr.exe".




EN:

This is a text encryptor based on the Caesar cipher (shift). The program allows users to encrypt and decrypt text using specified shift codes.

To begin, the user is prompted to choose an action: 1 - encrypt text, 2 - decrypt text, 0 - exit the program.

If the user selects 1, the program asks for the text to be encrypted. For example, "Hello, this is an important text that should not be decrypted." Then the user is asked to enter shift codes separated by commas. For example, "19,16,4,5,3,6,13,16,17,19,3,4,25,19,12,9,3,4,5,6,7,8".

The text is shifted sequentially by each of the entered shift codes. First, the text is shifted by 19, then by 16, followed by 4, and so on.

The result is the encrypted text: "Uryyb, guvf vf na vachfgevny grkg gung fubhyq abg or qnfurbsnavrq."

If the user selects 2, the program asks for the text to be decrypted. For example, "Uryyb, guvf vf na vachfgevny grkg gung fubhyq abg or qnfurbsnavrq." Then the user is asked to enter shift codes separated by commas, similar to "19,16,4,5,3,6,13,16,17,19,3,4,25,19,12,9,3,4,5,6,7,8".

The encrypted text is decrypted in the same way it was encrypted. The shift codes are applied in reverse order.

The result is the decrypted text: "Hello, this is an important text that should not be decrypted."

To run the program, you need to execute the Python script - main.py, or run "shifr.exe".
