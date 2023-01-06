import torch
import torch.nn as nn
import torchvision
import torchvision.models as models
import torch.optim as optim
import os
import sys
import argparse


#import logging


#logger = logging.getLogger(__name__)
#logger.setLevel(logging.DEBUG)
#logger.addHandler(logging.StreamHandler(sys.stdout))



def net():
    '''
    TODO: Complete this function that initializes your model
          Remember to use a pretrained model
    '''
    model = models.resnet18(pretrained=True)

    for param in model.parameters():
        param.requires_grad = False   

    num_features=model.fc.in_features
    model.fc = nn.Sequential(
                   nn.Linear(num_features, 10))
    return model

    
def model_fn(model_dir):
    '''
    TODO: Complete this to load your trained model.
    '''
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    #logger.info(f"DEVICE: {device}")
    
    #logger.info("LOADING MODEL WEIGHTS")
    model = net().to(device)
    
    with open(os.path.join(model_dir, 'model.pth'), 'rb') as f:
        model.load_state_dict(torch.load(f))
    return model