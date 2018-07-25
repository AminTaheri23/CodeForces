
word = list(input())
vowel = ['a', 'o', 'u', 'i', 'e']
flag = 0
for i in range(len(word)):
    if (word[i] not in vowel) and (word[i] != 'n'):
        try:
            if (word[len(word)-1] not in vowel) and (word[len(word)-1] != 'n'):
                flag = 1
            if word[i + 1] not in vowel:
                flag = 1
        except IndexError:
            break
if flag == 0:
    print("YES")
else:
    print("NO")
