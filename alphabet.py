def alphabet_position(text):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    alphabet = {alpha[i]: i + 1 for i in range(len(alpha))}
    answer = ''
    for i in range(len(text)):
        if text[i].lower() in alphabet.keys():
            answer += str(alphabet.get(text[i].lower())) + ' '
    return answer[:-1]