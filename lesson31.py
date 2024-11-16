from pprint import pprint

def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    string_positions = {}
    str_num = 0
    str_start_byte = file.seek(0)   # байт начальной строчки
    for string_ in strings:
        file.write(string_+'\n')
        str_num += 1
        key = (str_num, str_start_byte)
        string_positions[key]= string_
        str_start_byte = file.tell()
    file.close()
    return string_positions

file_name = 'newfile.txt'
strings = ["О", "Холодное небо, и сердце в груди на куски,", "ты страху не верил,", "и правду искал вопреки",
           "Стирая до крови всю душу свою через боль", "Ты воин света, который остался живой.", '', "Шаман"]
result = custom_write(file_name, strings)
pprint(result)
