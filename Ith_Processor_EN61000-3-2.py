import pandas as pd
import numpy as np

def capture_data():
    Iac= float(sample_data[list(sample_data)[3]].iloc[863])
    temp['101_Product']=list(sample_data)[1]
    temp['102_UNIT#']=sample_data[list(sample_data)[1]].iloc[0]   #Unit #
    temp['103.1_Test_Date']=sample_data[list(sample_data)[1]].iloc[4]
    temp['103_Ithd']=float(sample_data[list(sample_data)[3]].iloc[878])   #Ithd
    temp['104.1_IHD1']=Iac
    temp['104_IHD2']=float(sample_data[list(sample_data)[3]].iloc[881])*Iac/100   #Ihd2
    temp['105_IHD3']=float(sample_data[list(sample_data)[3]].iloc[882])*Iac/100   #Ihd3
    temp['106_IHD4']=float(sample_data[list(sample_data)[3]].iloc[883])*Iac/100   #Ihd4
    temp['107_IHD5']=float(sample_data[list(sample_data)[3]].iloc[884])*Iac/100   #Ihd5
    temp['108_IHD6']=float(sample_data[list(sample_data)[3]].iloc[885])*Iac/100   #Ihd6
    temp['109_IHD7']=float(sample_data[list(sample_data)[3]].iloc[886])*Iac/100   #Ihd7
    temp['110_IHD8']=float(sample_data[list(sample_data)[3]].iloc[887])*Iac/100   #Ihd8
    temp['111_IHD9']=float(sample_data[list(sample_data)[3]].iloc[888])*Iac/100   #Ihd9
    temp['112_IHD10']=float(sample_data[list(sample_data)[3]].iloc[889])*Iac/100   #Ihd10
    temp['113_IHD11']=float(sample_data[list(sample_data)[3]].iloc[890])*Iac/100   #Ihd11
    temp['114_IHD12']=float(sample_data[list(sample_data)[3]].iloc[891])*Iac/100   #Ihd12
    temp['115_IHD13']=float(sample_data[list(sample_data)[3]].iloc[892])*Iac/100   #Ihd13
    temp['116_IHD14']=float(sample_data[list(sample_data)[3]].iloc[893])*Iac/100   #Ihd14
    temp['117_IHD15']=float(sample_data[list(sample_data)[3]].iloc[894])*Iac/100   #Ihd15
    temp['118_IHD16']=float(sample_data[list(sample_data)[3]].iloc[895])*Iac/100   #Ihd16
    temp['119_IHD17']=float(sample_data[list(sample_data)[3]].iloc[896])*Iac/100   #Ihd17
    temp['120_IHD18']=float(sample_data[list(sample_data)[3]].iloc[897])*Iac/100   #Ihd18
    temp['121_IHD19']=float(sample_data[list(sample_data)[3]].iloc[898])*Iac/100   #Ihd19
    temp['122_IHD20']=float(sample_data[list(sample_data)[3]].iloc[899])*Iac/100   #Ihd20
    temp['123_IHD21']=float(sample_data[list(sample_data)[3]].iloc[900])*Iac/100   #Ihd21
    temp['124_IHD22']=float(sample_data[list(sample_data)[3]].iloc[901])*Iac/100   #Ihd22
    temp['125_IHD23']=float(sample_data[list(sample_data)[3]].iloc[902])*Iac/100   #Ihd23
    temp['126_IHD24']=float(sample_data[list(sample_data)[3]].iloc[903])*Iac/100   #Ihd24
    temp['127_IHD25']=float(sample_data[list(sample_data)[3]].iloc[904])*Iac/100   #Ihd25
    temp['128_IHD26']=float(sample_data[list(sample_data)[3]].iloc[905])*Iac/100   #Ihd26
    temp['129_IHD27']=float(sample_data[list(sample_data)[3]].iloc[906])*Iac/100   #Ihd27
    temp['130_IHD28']=float(sample_data[list(sample_data)[3]].iloc[907])*Iac/100   #Ihd28
    temp['131_IHD29']=float(sample_data[list(sample_data)[3]].iloc[908])*Iac/100   #Ihd29
    temp['132_IHD30']=float(sample_data[list(sample_data)[3]].iloc[909])*Iac/100   #Ihd30
    temp['133_IHD31']=float(sample_data[list(sample_data)[3]].iloc[910])*Iac/100   #Ihd31
    temp['134_IHD32']=float(sample_data[list(sample_data)[3]].iloc[911])*Iac/100   #Ihd32
    temp['135_IHD33']=float(sample_data[list(sample_data)[3]].iloc[912])*Iac/100   #Ihd33
    temp['136_IHD34']=float(sample_data[list(sample_data)[3]].iloc[913])*Iac/100   #Ihd34
    temp['137_IHD35']=float(sample_data[list(sample_data)[3]].iloc[914])*Iac/100   #Ihd35
    temp['138_IHD36']=float(sample_data[list(sample_data)[3]].iloc[915])*Iac/100   #Ihd36
    temp['139_IHD37']=float(sample_data[list(sample_data)[3]].iloc[916])*Iac/100   #Ihd37
    temp['140_IHD38']=float(sample_data[list(sample_data)[3]].iloc[917])*Iac/100   #Ihd38
    temp['141_IHD39']=float(sample_data[list(sample_data)[3]].iloc[918])*Iac/100   #Ihd39
    temp['142_IHD40']=float(sample_data[list(sample_data)[3]].iloc[919])*Iac/100   #Ihd40
data = pd.DataFrame()
temp={}

steps=np.arange(1,101)
print steps

for step in steps:
    #print step
    #sample_data=pd.read_csv(filename+'.csv')
    sample_data=pd.read_csv(str(step)+'.csv')
    #print list(sample_data)
    #print list(sample_data)[3]
    capture_data()
    data = data.append(temp, ignore_index=True)
    data.to_csv('Ithd_Data_Rms_w_Fund.csv')
