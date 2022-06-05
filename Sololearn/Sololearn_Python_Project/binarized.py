import numpy as np
from sklearn.preprocessing import Binarizer 
input_data = np.array(
[[2.1,-1.9,5.5,],[-1.5,2.4,3.5],[0.5,-7.9,5.6],[5.9,2.3,-5.8]]
)
data_binarized=Binarizer(threshold=0.5)
print("\nBinarized data:\n",data_binarized)