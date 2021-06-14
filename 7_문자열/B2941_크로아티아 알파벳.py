alpha_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
alphabet = input()
for i in alpha_list:
    alphabet = alphabet.replace(i, 'a')
print(len(alphabet))