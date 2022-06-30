# coding=utf8
import os
from crawler import Crawler
from amplification_eda import eda
from amplification_back_translate import back_translate
from evaluate_bleu import evaluate_bleu

if __name__ == '__main__':

    Crawler()

    input_text = ".\\text"
    output_dir = ".\\output"
    for root, dirs, files in os.walk(input_text):
        for file in files:
            filepath = os.path.join(root, file)
            filename = file.strip('.txt')
            for output in back_translate(filepath, filename):
                evaluate_bleu(output, filepath)
            for output in eda(filepath, filename):
                evaluate_bleu(output, filepath)




