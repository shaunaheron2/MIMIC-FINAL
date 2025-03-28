import os
import pickle

dict_folder = "./data/dict"
print(os.listdir(dict_folder)) 

# Load a specific dictionary (e.g., dataDic)
with open("./data/dict/metaDic", "rb") as f:
    data_dict = pickle.load(f)

# Check the keys inside the dictionary
print(data_dict.keys())  # This will show available patient stay IDs (or categories)

sample_stay = list(data_dict.keys())[0]
print(f"Data for {sample_stay}: {data_dict[sample_stay].keys()}")