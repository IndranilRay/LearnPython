"""
 Demonstrate pickle module for storing python objects in a file
"""
import pickle
D = dict(a=1, b=2)
F = open('test_pickle.txt', 'wb')
pickle.dump(D, F)
F.close()

# read file using pickle
F = open('test_pickle.txt', 'rb')
S = pickle.load(F)
# reading back data
print(S)



