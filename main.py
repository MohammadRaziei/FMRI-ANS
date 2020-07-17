import os

def getDatadbPath():
    import os
    folder_path = os.path.join(os.getcwd(),'datadb', 'haxby2001')
    if(not os.path.exists(folder_path)):
        print('download dataset to ' + folder_path)
        f = []
        f0 = wget.download('http://data.pymvpa.org/datasets/haxby2001/stimuli-2010.01.14.tar.gz')
        for i in range(1, 7):
          f.append(wget.download('http://data.pymvpa.org/datasets/haxby2001/subj' + str(i) + '-2010.01.14.tar.gz'))
        
        import tarfile #, zipfile
        import wget
        
        def extract_file(fname, path):
            tar = tarfile.open(fname, "r:gz")
            tar.extractall(path)
            tar.close()
        
        extract_file(f0, folder_path)
    
        cnt = 0
        for fname in f:
            cnt += 1
            extract_file(fname, folder_path)
    return folder_path

#%%
datadb_folder = getDatadbPath()
 
#%%
import os, logging
logging.getLogger("imported_module").setLevel(logging.ERROR)
from mvpa2.suite import *
# subjpath = os.path.join(pymvpa_datadbroot, 'haxby2001', 'subj1')
print("==============================")
subjpath = os.path.join(os.getcwd(),'datadb', 'haxby2001', 'subj1')
attrs = SampleAttributes(os.path.join(subjpath, 'labels.txt'),
                         header=True)
ds = fmri_dataset(samples=os.path.join(subjpath, 'bold.nii.gz'),
                  targets=attrs.labels, chunks=attrs.chunks,
                  mask=os.path.join(subjpath, 'mask8b_face_vt.nii.gz'))

#%%

from matplotlib import pyplot as plt 
plt.imshow(ds.O[1,25 ,:,:])
plt.show()
#%%
from mvpa2.measures.corrcoef import pearson_correlation


def normalize(x):
    x = (x - np.min(x))/np.std(x)
    # x -= np.min(x)
    # x = x / np.max(x)
    # x = 2*x-1
    return x


# def spont(x, axis=0):
#     y = np.mean(x, axis=axis)
#     return y
#%%
labels = []; cats = {}
with open(os.path.join(subjpath,'labels.txt'), 'r') as f:
    f.readline()
    for i in range(1452):
        s = f.readline().split(' ')
        labels.append((s[0],int(s[1])))
        try:
            cats[s[0]].append(i)
        except:
            cats[s[0]] = [i]
#%%   

for i in range(200,400,10):
    z = np.mean(ds.O, axis=0).reshape(-1, 1)
    X = ds.O[309,:,:,:].reshape(-1, 1) - z
    Y = ds.O[i,:,:,:].reshape(-1, 1) - z

    z = np.where(z < np.max(z)*0.9)[0]
    X = X[z]
    Y = Y[z]
    
    z = np.union1d( np.where(X > 0)[0], np.where(Y > 0)[0])
    X = normalize(X[z])
    Y = normalize(Y[z])

    corr = pearson_correlation(X, Y)
    print(corr, labels[i])






