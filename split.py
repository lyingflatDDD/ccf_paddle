"""
split the train data 

"""

import numpy as np
import os 
#from sklearn import datasets
from sklearn.model_selection import train_test_split

def main():
    root_path = "/public/home/cxiao/Study/data/skiing"
    orgin = os.path.join(root_path,"train_data.npy") 
    label = os.path.join(root_path,"train_label.npy")
    
    # read data 
    orgin_np = np.load(orgin)
    label_np = np.load(label)

    print(orgin_np.shape,label_np.shape)
    X_train,X_test,y_train,y_test = train_test_split(orgin_np, label_np, test_size=0.2,stratify=label_np, shuffle=True, random_state=1)
    print(X_train.shape,y_train.shape)
    np.save(os.path.join(root_path,"val_data.npy"),X_test)
    np.save(os.path.join(root_path,"val_label.npy"),y_test)
    np.save(os.path.join(root_path,"train_data_split.npy"),X_train)
    np.save(os.path.join(root_path,"train_label_split.npy"),y_train)



def analize():
    root_path = "/public/home/cxiao/Study/data/skiing"
    orgin = os.path.join(root_path,"train_data.npy") 
    label = os.path.join(root_path,"val_label.npy")

    label_np = np.load(label)

    index = [0 for _ in range(10)]
    for i in range(len(label_np)):
	   # print(label_np[i])
	    index[int(label_np[i])]+=1
    print(index)
if __name__ == "__main__":
    #main()
    analize()
