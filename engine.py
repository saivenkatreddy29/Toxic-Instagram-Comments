import pandas as pd
import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader
from transformers import AutoTokenizer
# from model_defination import lstm_model
import warnings
from torch import nn
from run import get_comments
warnings.filterwarnings('ignore')
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased",return_type = 'pt')
class lstm_model(nn.Module):
    def __init__(self,
                vocab_size = 30522,
                output = 6):
        super().__init__()
        self.Embedding_layer = nn.Embedding(num_embeddings =vocab_size ,
                                          embedding_dim = 32)
        self.linear_layer =   nn.Linear(32,64)
        self.relu = nn.ReLU()
        self.lstm1 = nn.LSTM(64,128,
                   bidirectional = True, batch_first = True)
        self.lstm2 = nn.LSTM(128*2,64,
                   bidirectional = True,batch_first = True)
        
        self.output = nn.Linear(64*2,output)

    def forward(self,x):
        x = x.squeeze(1)
        # print(f'going inside: {x.shape}')
        x = self.Embedding_layer(x)
        # print(f'coming outside:{x.shape}')
        
        x = self.linear_layer(x)
        x = self.relu(x)
        # print(f'x before:{x.shape}')
        x,_ = self.lstm1(x)
        x,_ = self.lstm2(x)
        # print(f'after {x.shape}')
        x = self.output(x)
        x = x.mean(dim=1)
        return x
        
    
device = 'cuda' if torch.cuda.is_available() else 'cpu'

model = lstm_model() 
model.load_state_dict(torch.load('lstm_model_weights.pth', map_location=torch.device('cpu')))
# model = torch.load(r"lstm_model.pth",weights_only = False, map_location=torch.device('cpu'))

def test_cust(input_txt,model = model):
    in_tokenized = tokenizer(input_txt, truncation = True, padding = 'max_length', max_length = 150,return_tensors = 'pt')
    ids = in_tokenized['input_ids']
    # print(ids.shape)
    ids = ids.unsqueeze(0)
    # print(ids.shape)
    print('reached for loding model')
    output_t = model(ids.to(device)).squeeze(0)
    print('loaded the model')
    pre = output_t>0
    final = [1 if item else 0 for item in pre]
    return final
haris_comment = "https://www.instagram.com/p/DB9OgtyCP7h/"
def get_toxic_users(haris_comment = haris_comment):

    data = get_comments(haris_comment,limit = 10)
    # df = pd.read_csv(r"comments.csv")
    # data = df[['ownerUsername','text']]
    verified = []
    total = []
    for text in data['text']:
        preds = test_cust(text)
        verified.append(preds)
        total.append(sum(preds))
    # print(f'verified:{verified}')
    # print(total)
    data['predicted'] = verified
    data['total'] = total
    sorted_data = data.sort_values(by= 'total')
    toxic_guys = list(sorted_data[-5:]['ownerUsername'])
    comment_made = list(sorted_data[-5:]['text'])
    print(toxic_guys)
    return toxic_guys,comment_made

if __name__ == '__main__':
    get_toxic_users()
    
    