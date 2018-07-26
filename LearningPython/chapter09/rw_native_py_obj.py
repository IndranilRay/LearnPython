import pickle
# Initialize a dictionary
D = {'a': 1, 'b': 2}
F = open('datafile.pkl', 'wb')
pickle.dump(D, F)
F.close()

# read a pickle file
F = open('datafile.pkl', 'rb')
E = pickle.load(F)
F.close()
print(E)