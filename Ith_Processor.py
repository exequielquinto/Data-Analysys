import pandas as pd
import numpy as np

def capture_data():
    temp['101_Product']=list(sample_data)[1]
    temp['102_UNIT#']=sample_data[list(sample_data)[1]].iloc[0]   #Unit #
    temp['103.1_Test_Date']=sample_data[list(sample_data)[1]].iloc[4]
    temp['103_Ithd']=sample_data[list(sample_data)[3]].iloc[878]   #Ithd
    temp['104_IHD2']=sample_data[list(sample_data)[3]].iloc[881]   #Ihd2
    temp['105_IHD3']=sample_data[list(sample_data)[3]].iloc[882]   #Ihd3
    temp['106_IHD4']=sample_data[list(sample_data)[3]].iloc[883]   #Ihd4
    temp['107_IHD5']=sample_data[list(sample_data)[3]].iloc[884]   #Ihd5
    temp['108_IHD6']=sample_data[list(sample_data)[3]].iloc[885]   #Ihd6
    temp['109_IHD7']=sample_data[list(sample_data)[3]].iloc[886]   #Ihd7
    temp['110_IHD8']=sample_data[list(sample_data)[3]].iloc[887]   #Ihd8
    temp['111_IHD9']=sample_data[list(sample_data)[3]].iloc[888]   #Ihd9
    temp['112_IHD10']=sample_data[list(sample_data)[3]].iloc[889]   #Ihd10
    temp['113_IHD11']=sample_data[list(sample_data)[3]].iloc[890]   #Ihd11
    temp['114_IHD12']=sample_data[list(sample_data)[3]].iloc[891]   #Ihd12
    temp['115_IHD13']=sample_data[list(sample_data)[3]].iloc[892]   #Ihd13
    temp['116_IHD14']=sample_data[list(sample_data)[3]].iloc[893]   #Ihd14
    temp['117_IHD15']=sample_data[list(sample_data)[3]].iloc[894]   #Ihd15
    temp['118_IHD16']=sample_data[list(sample_data)[3]].iloc[895]   #Ihd16
    temp['119_IHD17']=sample_data[list(sample_data)[3]].iloc[896]   #Ihd17
    temp['120_IHD18']=sample_data[list(sample_data)[3]].iloc[897]   #Ihd18
    temp['121_IHD19']=sample_data[list(sample_data)[3]].iloc[898]   #Ihd19
    temp['122_IHD20']=sample_data[list(sample_data)[3]].iloc[899]   #Ihd20
    temp['123_IHD21']=sample_data[list(sample_data)[3]].iloc[900]   #Ihd21
    temp['124_IHD22']=sample_data[list(sample_data)[3]].iloc[901]   #Ihd22
    temp['125_IHD23']=sample_data[list(sample_data)[3]].iloc[902]   #Ihd23
    temp['126_IHD24']=sample_data[list(sample_data)[3]].iloc[903]   #Ihd24
    temp['127_IHD25']=sample_data[list(sample_data)[3]].iloc[904]   #Ihd25
    temp['128_IHD26']=sample_data[list(sample_data)[3]].iloc[905]   #Ihd26
    temp['129_IHD27']=sample_data[list(sample_data)[3]].iloc[906]   #Ihd27
    temp['130_IHD28']=sample_data[list(sample_data)[3]].iloc[907]   #Ihd28
    temp['131_IHD29']=sample_data[list(sample_data)[3]].iloc[908]   #Ihd29
    temp['132_IHD30']=sample_data[list(sample_data)[3]].iloc[909]   #Ihd30
    temp['133_IHD31']=sample_data[list(sample_data)[3]].iloc[910]   #Ihd31
    temp['134_IHD32']=sample_data[list(sample_data)[3]].iloc[911]   #Ihd32
    temp['135_IHD33']=sample_data[list(sample_data)[3]].iloc[912]   #Ihd33
    temp['136_IHD34']=sample_data[list(sample_data)[3]].iloc[913]   #Ihd34
    temp['137_IHD35']=sample_data[list(sample_data)[3]].iloc[914]   #Ihd35
    temp['138_IHD36']=sample_data[list(sample_data)[3]].iloc[915]   #Ihd36
    temp['139_IHD37']=sample_data[list(sample_data)[3]].iloc[916]   #Ihd37
    temp['140_IHD38']=sample_data[list(sample_data)[3]].iloc[917]   #Ihd38
    temp['141_IHD39']=sample_data[list(sample_data)[3]].iloc[918]   #Ihd39
    temp['142_IHD40']=sample_data[list(sample_data)[3]].iloc[919]   #Ihd40
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
    data.to_csv('Ithd_Data.csv')
