# ASCII Code (American Standard Code for Information Interchange)
# A-Z (65-90)
# a-z (97-122)
# 0-9 (48-57)

letter = ';'

if (letter=='a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or 
    letter=='A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U'):
    print('Vowel')
elif (letter >= 'a' and letter <= 'z') or (letter>='A' and letter<='Z'):
    print('Consonant')
else:
    print('Others')
