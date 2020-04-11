from django.conf import settings

import os

def importKaggleDataset():
    import requests
    
    
    #first we set the environment variables and authenticate 
    os.environ['KAGGLE_USERNAME'] = settings.KAGGLE_USERNAME
    os.environ['KAGGLE_KEY'] = settings.KAGGLE_API_KEY
    
    from kaggle.api.kaggle_api_extended import KaggleApi
    api = KaggleApi()
    api.authenticate()
    # The direct link to the Kaggle data set
    api.dataset_download_file(settings.KAGGLE_DATASET_PATH,settings.KAGGLE_DATASET_FILENAME, path=settings.DATASET_DIR, force=True)
    # The local path where the data set is saved.  

def parseKaggleDataset(): 
    from .parser import KaggleCSVParser 
    parser = KaggleCSVParser() 
    parser.parse(settings.KAGGLE_LOCAL_FILENAME)

def refreshKaggleDataset(): 
    importKaggleDataset() 
    parseKaggleDataset()
