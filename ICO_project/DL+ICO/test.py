import _pickle as pickle
path = '/users/barry/desktop/vectors_48h.pkl'
f = open(path,'rb')
info = pickle.load(f)

print(info)
ft = open('/users/barry/desktop/test.txt', 'w')
ft.write(str(info))