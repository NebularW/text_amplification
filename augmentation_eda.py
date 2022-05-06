# coding = utf8
import codecs
from nlpcda import Similarword
from nlpcda import EquivalentChar
from nlpcda import RandomDeleteChar


def fetch_data(input_file):
    """ Store each reference and candidate sentences as a list """
    input_string = ''
    reference_file = codecs.open(input_file, 'r', 'utf-8')
    for line in reference_file.readlines():
        input_string += line

    return input_string


def similar_word(input_str):
    smw = Similarword(create_num=3, change_rate=0.3)
    replace_str = smw.replace(input_str)
    return replace_str


def equivalent_char(input_str):
    s = EquivalentChar(create_num=3, change_rate=0.3)
    replace_str = s.replace(input_str)
    return replace_str


def random_delete_char(input_str):
    s = RandomDeleteChar(create_num=3, change_rate=0.3)
    replace_str = s.replace(input_str)
    return replace_str


if __name__ == '__main__':
    ini_file = 'D:\\Code\\PyCharm\\DataScience\\text\\input.txt'
    in_str = fetch_data(ini_file)

    print('原文件：\n')
    print(in_str)
    i = 1
    for output_str in similar_word(in_str):
        out = open('.\\output\\similar_word' + str(i) + '.txt', 'w', encoding='utf-8')
        out.write(output_str)
        out.close()
        i += 1
    i = 1
    for output_str in equivalent_char(in_str):
        out = open('.\\output\\equivalent_char' + str(i) + '.txt', 'w', encoding='utf-8')
        out.write(output_str)
        out.close()
        i += 1
    i = 1
    for output_str in random_delete_char(in_str):
        out = open('.\\output\\random_delete_char' + str(i) + '.txt', 'w', encoding='utf-8')
        out.write(output_str)
        out.close()
        i += 1
