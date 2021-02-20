import pandas as pd 
import numpy as np

def split_data_into_two_samples(data):
    
    train_data, test_data = train_test_split(data, test_size=0.3, random_state=42)
    
    return train_data, test_data


def prepare_data(data):
    #select_data = data.select_dtypes(exclude=[object])
    data = data.drop(columns=["Id"])
    y = data["SalePrice"]
    data = data.drop(columns=["SalePrice"])
    select_data = data.select_dtypes([np.number])
    return select_data.dropna(axis=1), y
