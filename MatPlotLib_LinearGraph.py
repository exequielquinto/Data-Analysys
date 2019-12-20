import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
#import glob


sample_data=pd.read_csv('IEEE1547_Data_Dist_Without_Outliers.csv')

#sample_data=pd.read_csv('THD_ATE.csv')
plt.rcParams["figure.figsize"] = (15,8)

#print list(sample_data)
#print list(sample_data)[0]
#print sample_data['Ithd']

#print np.arange(1,100,1)
numbers=np.arange(1,160,4)
print numbers

#num=0   #0 for ITHD
ctr=1

for num in numbers:
    print num

    #x=np.arange(1,100,1)
    x_data=list(sample_data)[0]
    x=sample_data[x_data]
    
    y_data1=list(sample_data)[num]
    y1=sample_data[y_data1]
    
    y_data2=list(sample_data)[num+1]
    y2=sample_data[y_data2]
    
    y_data3=list(sample_data)[num+2]
    y3=sample_data[y_data3]
    
    y_data4=list(sample_data)[num+3]
    y4=sample_data[y_data4]

    plt.plot(x,y1)
    plt.plot(x,y2)
    plt.plot(x,y3)
    plt.plot(x,y4)
    


    title=str(list(sample_data)[num])+' Data Distribution'
    plt.title(title)
    plt.xlabel("Sample Number")
    plt.ylabel("Reading")
    y1_legend=str(list(sample_data)[num])
    plt.legend([y1_legend,"LSL","USL","Average"])
    
    
    
    #fig = matplotlib.pyplot.gcf()
    #fig.set_size_inches(18.5, 10.5)
    
    #fig.savefig('test2png.png', dpi=100)
    filename='Data_Dist_IHD'+str(ctr)
    plt.savefig(filename+'.png', dpi=200)
    ctr=ctr+1

    plt.show()