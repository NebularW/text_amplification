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


def eda(filepath, filename):
    in_str = fetch_data(filepath)
    output_file = []
    i = 0
    for output_str in similar_word(in_str):
        if i != 0:
            output_path = '.\\output\\' + filename + '_similar_word' + str(i) + '.txt'
            output_file.append(output_path)
            out = open(output_path, 'w', encoding='utf-8')
            out.write(output_str)
            out.close()
        i += 1

    i = 0
    for output_str in equivalent_char(in_str):
        if i != 0:
            output_path = '.\\output\\' + filename + '_equivalent_char' + str(i) + '.txt'
            output_file.append(output_path)
            out = open(output_path, 'w', encoding='utf-8')
            out.write(output_str)
            out.close()
        i += 1
    i = 0
    for output_str in random_delete_char(in_str):
        if i != 0:
            output_path = '.\\output\\' + filename + '_random_delete_char' + str(i) + '.txt'
            output_file.append(output_path)
            out = open(output_path, 'w', encoding='utf-8')
            out.write(output_str)
            out.close()
        i += 1

    return output_file


if __name__ == '__main__':
    eda('.\\text\\content1.txt', 'content1.txt')
