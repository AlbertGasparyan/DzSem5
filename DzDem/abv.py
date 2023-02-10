my_text  ='Напишите абв напиабв програбвмму программу, удаляющую из \
 этого абв текста все вабвс слова, содерабващие содержащие "абв"'

def del_abv(text):
    text=list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)
my_text=del_abv(my_text)
print(my_text)