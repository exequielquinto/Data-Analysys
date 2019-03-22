import pandas as pd
from matplotlib import pyplot as plt
print ('done')
#x=[1,2,4]
#y=[2,3,4]
#z=[4,2,1]
#plt.plot(x,y)
#plt.plot(x,z)
#plt.title('test plot')
#plt.xlabel('x')
#plt.ylabel('y')
#plt.legend(['y','z'])
#plt.show()
sample_data=pd.read_csv('48V_DC_Input.csv')
#sample_data=pd.read_csv('48V_DC_Input.csv', header=None, delimiter=r"\s+")
print type(sample_data)
print('loaded')
print sample_data
#print sample_data.Vrms_StdResults
#print sample_data.Vrms_StdResults.iloc[1]
print sample_data.Vrms_StdResults.iloc[0:5]

