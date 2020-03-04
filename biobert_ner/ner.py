from server import *
from run_ner import *


with open('input.txt', 'r') as f:
    text = f.read()
    text = text[:-2]

text_hash = hashlib.sha224(text.encode('utf-8')).hexdigest()
input_gnormplus = 'input{}.PubTator'.format(text_hash)
f = open(input_gnormplus, 'w', encoding='utf-8')
f.write(text_hash + '|t|')
f.write('\n')
f.write(text_hash + '|a|' + text + '\n\n')
f.close()


dict_list = pubtator2dict_list(input_gnormplus, is_raw_text=True)
stm_dict = dict()
stm_dict['biobert'] = BioBERT(FLAGS)

try:
    res = stm_dict['biobert'].recognize(dict_list,is_raw_text=True,thread_id=None)
except:
    pass
print(res)
