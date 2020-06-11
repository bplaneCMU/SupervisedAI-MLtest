import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

'''
Disregarding 1st Principal component
use 2nd and 3rd as points in a k-means
algorithm to find to which cluster each
point belongs

Though it appears obvious with the human eye
we should still try to be rigerous and find clusters
mathematically
'''
def __main(path):
    #Import PCA csv
    frame = pd.read_csv(path)
    frame.drop(labels='PC1', axis=1, inplace=True)

    kmeans = KMeans(n_clusters=6, max_iter=1000, random_state=1)

    labels = kmeans.fit_predict(frame)

    df = pd.read_csv('../tracks_17_cleaned.csv')

    df['label'] = labels.tolist()
    frame['label'] = labels.tolist()
    
    df.to_csv('pca_labelled.csv', index=False)

    #Create fig object
    fig = plt.figure(figsize = (8,8))
    #Format the axis to look nice
    ax = fig.add_subplot(1,1,1) 
    ax.set_xlabel('Principal Component 3', fontsize = 15)
    ax.set_ylabel('Principal Component 2', fontsize = 15)
    ax.set_title('2 Component PCA', fontsize = 20)

    #Graph data as scatter plot, enable grid
    colors = ['red', 'yellow', 'blue', 'orange', 'green', 'purple']
    for i in range(6):
        temp_df = frame.loc[frame['label'] == i]
        ax.scatter(temp_df['PC3'], temp_df['PC2'], s=25, c=colors[i])
    
    ax.grid()
    plt.show()
    return



if __name__ == '__main__':
    __main(sys.argv[1])
