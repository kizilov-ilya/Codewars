def rot13(message):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    alphabet = {alpha[i]: i + 1 for i in range(len(alpha))}
    inv_alphabet = {value: key for key, value in alphabet.items()}
    answer = ''
    for i in range(len(message)):
        if message[i].lower() in alphabet.keys() and message[i].isupper():
            answer += str(inv_alphabet.get(alphabet.get(message[i].lower()) + 13)).upper() if alphabet.get(
                message[i].lower()) <= 13 else str(inv_alphabet.get(alphabet.get(message[i].lower()) - 13)).upper()
        elif message[i].lower() in alphabet.keys():
            answer += str(inv_alphabet.get(alphabet.get(message[i].lower()) + 13)) if alphabet.get(
                message[i].lower()) <= 13 else str(inv_alphabet.get(alphabet.get(message[i].lower()) - 13))
        else:
            answer += str(message[i])
    return answer


print(rot13("tEst"))
