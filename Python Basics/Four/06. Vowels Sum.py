text = input()

result = 0

for i in range(0, len(text)):
    temp_char = text[i]
    if temp_char == 'a':
        result +=1
    elif temp_char == 'e':
        result +=2
    elif temp_char == 'i':
        result +=3
    elif temp_char == 'o':
        result +=4
    elif temp_char == 'u':
        result +=5

print(result)