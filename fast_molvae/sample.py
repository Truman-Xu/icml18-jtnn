import torch
import torch.nn as nn

import math, random, sys
import argparse
from jtvae import *
from jtvae.nnutils import check_device
import rdkit

lg = rdkit.RDLogger.logger() 
lg.setLevel(rdkit.RDLogger.CRITICAL)

parser = argparse.ArgumentParser()
parser.add_argument('--nsample', type=int, required=True)
parser.add_argument('--vocab', required=True)
parser.add_argument('--model', required=True)

parser.add_argument('--hidden_size', type=int, default=450)
parser.add_argument('--latent_size', type=int, default=56)
parser.add_argument('--depthT', type=int, default=20)
parser.add_argument('--depthG', type=int, default=3)

args = parser.parse_args()
   
model_vocab = [x.strip("\r\n ") for x in open(args.vocab)] 
model_vocab = Vocab(model_vocab)

device = check_device()
model = JTNNVAE(
    model_vocab, args.hidden_size, args.latent_size, args.depthT, args.depthG,
)
model.load_state_dict(torch.load(args.model))
model = model.to(device)

torch.manual_seed(0)
for i in range(args.nsample):
    print(model.sample_prior())
