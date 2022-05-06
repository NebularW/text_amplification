from nltk.translate.bleu_score import sentence_bleu, corpus_bleu
from nltk.translate.bleu_score import SmoothingFunction
reference = [['我', '是', '谁']]
candidate = ['我', '是', '谁']
smooth = SmoothingFunction()  # 定义平滑函数对象
score = sentence_bleu(reference, candidate,  smoothing_function=smooth.method1)
corpus_score = corpus_bleu([reference], [candidate], smoothing_function=smooth.method1)
print(corpus_score)