#!/usr/bin/env python
# coding: utf-8

# ## Inverse Cooking: Recipe Generation from Food Images

# import torch
import os
# from src.args import get_parser
import pickle
from src.model import get_model
# from torchvision import transforms
# from src.utils.output_utils import prepare_output
# from PIL import Image
import time
import sys

# import requests
from io import BytesIO

urls = []
ids = []

ids.append("hello")
urls.append(sys.argv[1])

print(urls)
sys.stdout.flush()
# print(ids)
# print(sys.argv[1])

# -----------------------------------------
'''
data_dir = './data'

# code will run in gpu if available and if the flag is set to True, else it will run on cpu
use_gpu = True
device = torch.device('cuda' if torch.cuda.is_available() and use_gpu else 'cpu')
map_loc = None if torch.cuda.is_available() and use_gpu else 'cpu'

print(device)
print(map_loc)

# code below was used to save vocab files so that they can be loaded without Vocabulary class
# ingrs_vocab = pickle.load(open(os.path.join(data_dir, 'final_recipe1m_vocab_ingrs.pkl'), 'rb'))
# ingrs_vocab = [min(w, key=len) if not isinstance(w, str) else w for w in ingrs_vocab.idx2word.values()]
# vocab = pickle.load(open(os.path.join(data_dir, 'final_recipe1m_vocab_toks.pkl'), 'rb')).idx2word
# pickle.dump(ingrs_vocab, open('../demo/ingr_vocab.pkl', 'wb'))
# pickle.dump(vocab, open('../demo/instr_vocab.pkl', 'wb'))

ingrs_vocab = pickle.load(open(os.path.join(data_dir, 'ingr_vocab.pkl'), 'rb'))
vocab = pickle.load(open(os.path.join(data_dir, 'instr_vocab.pkl'), 'rb'))

ingr_vocab_size = len(ingrs_vocab)
instrs_vocab_size = len(vocab)
output_dim = instrs_vocab_size

t = time.time()

sys.argv = ['']
del sys
args = get_parser()
args.maxseqlen = 15
args.ingrs_only = False
model = get_model(args, ingr_vocab_size, instrs_vocab_size)
# Load the trained model parameters
model_path = os.path.join(data_dir, 'modelbest.ckpt')
model.load_state_dict(torch.load(model_path, map_location=map_loc))
model.to(device)
model.eval()
model.ingrs_only = False
model.recipe_only = False
# print('loaded model')
# print("Elapsed time:", time.time() - t)

transf_list_batch = [transforms.ToTensor(), transforms.Normalize((0.485, 0.456, 0.406),
                                                                 (0.229, 0.224, 0.225))]
to_input_transf = transforms.Compose(transf_list_batch)

greedy = [True, False, False, False]
beam = [-1, -1, -1, -1]
temperature = 1.0
numgens = 1

# Set ```use_urls = True``` to get recipes for images in ```demo_urls```.
#
# You can also set ```use_urls = False``` and get recipes for images in the path in ```data_dir/test_imgs```.

use_urls = True  # set to true to load images from demo_urls instead of those in test_imgs folder
show_anyways = False  # if True, it will show the recipe even if it's not valid

final_output = {}

response = requests.get(urls[0])
image = Image.open(BytesIO(response.content))

transf_list = [transforms.Resize(256), transforms.CenterCrop(224)]
transform = transforms.Compose(transf_list)

image_transf = transform(image)
image_tensor = to_input_transf(image_transf).unsqueeze(0).to(device)

#plt.imshow(image_transf)
#plt.axis('off')
#plt.show()
#plt.close()

num_valid = 1

for i in range(numgens):
    with torch.no_grad():
        outputs = model.sample(image_tensor, greedy=greedy[i],
                                temperature=temperature, beam=beam[i], true_ingrs=None)

    ingr_ids = outputs['ingr_ids'].cpu().numpy()
    recipe_ids = outputs['recipe_ids'].cpu().numpy()

    outs, valid = prepare_output(recipe_ids[0], ingr_ids[0], ingrs_vocab, vocab)

    print(outs['ingrs'])
    #print(final_output)

    final_output[ids[0]] = outs['ingrs']

# sys.stdout.flush()
'''
'''
if valid['is_valid'] or show_anyways:

    print('RECIPE', num_valid)
    num_valid += 1
    # print ("greedy:", greedy[i], "beam:", beam[i])

    BOLD = '\033[1m'
    END = '\033[0m'
    print(BOLD + '\nTitle:' + END, outs['title'])

    print(BOLD + '\nIngredients:' + END)
    print(', '.join(outs['ingrs']))

    print(BOLD + '\nInstructions:' + END)
    print('-' + '\n-'.join(outs['recipe']))

    print('=' * 20)

else:
    pass
    print("Not a valid recipe!")
    print("Reason: ", valid['reason'])
    
'''
