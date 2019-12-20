import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from docutils.nodes import title

sample_data=pd.read_csv('IEEE1547_Freq_Dist_Without_Outliers.csv')

#print list(sample_data)
#print list(sample_data)[0]
#print sample_data

numbers=[0,3,6,9,12,15,18,21,24,27,30]
numbers=np.arange(0,80,2)
print numbers

#num=0   #0 for ITHD

ctr=1
for num in numbers:
    print num

    x_axis=list(sample_data)[num]
    y_axis=list(sample_data)[num+1]

    x=sample_data[x_axis]
    y=sample_data[y_axis]
    ind=np.arange(len(x))
    #ind2=np.arange(5)
    #print ind

    #plt.plot(x,y)
    plt.rcParams["figure.figsize"] = (15,8)   #15,8

    plt.bar(ind,y)
    plt.xticks(ind,x)

    #title=str(list(sample_data)[num])+' Frequency Distribution'+','+'Ppk(Upper)'+'='+str(sample_data[list(sample_data)[num+2]].iloc[0])
    title=str(list(sample_data)[num])+' Frequency Distribution'
    plt.title(title)
    plt.xlabel("Reading")
    plt.ylabel("Number of Occurence")
    
    
    
    #fig = matplotlib.pyplot.gcf()
    #fig.set_size_inches(18.5, 10.5)
    
    #fig.savefig('test2png.png', dpi=100)
    
    filename='Freq_Dist_IHD'+str(ctr)
    plt.savefig(filename+'.png', dpi=200)
    ctr=ctr+1    

    plt.show()