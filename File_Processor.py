import pandas as pd

filename='60V_Selkirk_Eff'


sample_data=pd.read_csv(filename+'.csv')
data = pd.DataFrame()
data_ave = pd.DataFrame()

#print sample_data.shape[0]
max_col = sample_data.shape[0]-1
#print max_col

cntr=0

while cntr<max_col:
    if (sample_data.D_Watts_AC.iloc[cntr]-sample_data.D_Watts_AC.iloc[cntr+1])<150:
        #print (sample_data.Watts_AC.iloc[cntr+1]-sample_data.Watts_AC.iloc[cntr])
        cntr=cntr+1
        #print sample_data.Watts_AC.iloc[cntr]
        #print ('run')
        #print cntr
    else:
        #print (cntr+2)
        #print sample_data.Watts_AC.iloc[cntr]
        #print (sample_data.Watts_AC.iloc[cntr]-sample_data.Watts_AC.iloc[cntr+1])
        cntr=cntr+1
        temp=sample_data[["A_Taken","B_Vrms","C_Arms","D_Watts_AC","E_PF","F_Freq","G_Athd","H_Watts_DC","I_Vdc","J_Adc","K_Eff"]].iloc[(cntr-11):(cntr-1)]
        #print temp.mean(axis=0)
        data=data.append(temp, ignore_index=True)
        data_ave=data_ave.append(temp.mean(axis=0), ignore_index=True)
        
temp=sample_data[["A_Taken","B_Vrms","C_Arms","D_Watts_AC","E_PF","F_Freq","G_Athd","H_Watts_DC","I_Vdc","J_Adc","K_Eff"]].iloc[(max_col-10):(max_col)]
data=data.append(temp, ignore_index=True)
data_ave=data_ave.append(temp.mean(axis=0), ignore_index=True)
data.to_csv(filename+'_Processed'+'.csv')
data_ave.to_csv(filename+'_Processed_Averaged'+'.csv')
print ('done')