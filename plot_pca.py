import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

'''
Runs the formatted csv file through two rounds
of principle component analysis

Plots resulting data using matplotlib's pyplot
'''
def __main(path):
    frame = pd.read_csv(path)
    
    pca = PCA(n_components = 2)
    pca_frame = pd.DataFrame(data = pca.fit_transform(frame),
                            columns = ['PC1', 'PC2'])

    #Create fig object
    fig = plt.figure(figsize = (8,8))
    #Format the axis to look nice
    ax = fig.add_subplot(1,1,1) 
    ax.set_xlabel('Principal Component 1', fontsize = 15)
    ax.set_ylabel('Principal Component 2', fontsize = 15)
    ax.set_title('2 Component PCA', fontsize = 20)

    #Graph data as scatter plot, enable grid
    ax.scatter(pca_frame['PC1'], pca_frame['PC2'], s=25)
    ax.grid()

    #Save PCA csv
    pca_frame.to_csv('pca.csv', index=False)

    #Display char
    plt.show()



if __name__ == '__main__':
    path = sys.argv[1]
    __main(path)
