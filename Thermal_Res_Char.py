import pandas as pd         
import visa, time    


#Connect to Instruments
rm = visa.ResourceManager()
daq = rm.open_resource('ASRL13::INSTR')


def measure():
    #Time
    temp['A_Time']=time.ctime()
    
    #Minutes
    temp['B_Mins']=round((time.time()-ref_time)/60)
       
    #Amb
    daq.write('MEAS:TEMP? %s,%s,(%s)' % ('TCouple', 'K', '@101'))
    time.sleep(0.5)
    temp['C_Amb'] = float(daq.read())
       
    #HTSK
    daq.write('MEAS:TEMP? %s,%s,(%s)' % ('TCouple', 'K', '@303'))
    time.sleep(0.5)
    temp['D_Htsk'] = float(daq.read())
    
    #PCB Bottom
    daq.write('MEAS:TEMP? %s,%s,(%s)' % ('TCouple', 'K', '@304'))
    time.sleep(0.5)
    temp['E_PCB_Bot'] = float(daq.read())
    
    #PCB Top/Tab of Q16_P4
    daq.write('MEAS:TEMP? %s,%s,(%s)' % ('TCouple', 'K', '@305'))
    time.sleep(0.5)
    temp['F_PCB_Top'] = float(daq.read())
    
    #PCB Top/Tab of Q10_P4
    daq.write('MEAS:TEMP? %s,%s,(%s)' % ('TCouple', 'K', '@306'))
    time.sleep(0.5)
    temp['G_Q10_P4'] = float(daq.read())
    
    #PCB Top/Tab of Q2_P3
    daq.write('MEAS:TEMP? %s,%s,(%s)' % ('TCouple', 'K', '@307'))
    time.sleep(0.5)
    temp['H_Q2_P3'] = float(daq.read())
    
    #Measure Iin
    daq.write('MEAS:VOLT:DC? AUTO,DEF,(@110)')
    time.sleep(0.5)                              
    Iin = (float(daq.read()))*3998.401
    temp['I_Iin'] = Iin
    
    #Measure Vd1
    daq.write('MEAS:VOLT:DC? AUTO,DEF,(@101)')
    time.sleep(0.5)
    temp['J_Vd1'] = float(daq.read())
    
    #Measure Pd1
    temp['K_Pd1'] = (temp['I_Iin']/32)*temp['J_Vd1']
    
    #Measure Vd2
    daq.write('MEAS:VOLT:DC? AUTO,DEF,(@101)')
    time.sleep(0.5)
    temp['L_Vd2'] = float(daq.read())
    
    #Measure Pd2
    temp['M_Pd2'] = (temp['I_Iin']/32)*temp['L_Vd2']
         
results = pd.DataFrame()
ref_time=time.time()
temp = {}
while 1:
    
    #measure()
    try:
        measure()       
    except:
        try:
            print('measure error1')
            time.sleep(1)
            measure()
        except:
            try:
                print('measure error2')
                time.sleep(1)
                measure()
            except:
                print('measure error3')
                time.sleep(1)
                measure()
    
    results = results.append(temp, ignore_index=True)    # 17
    print temp['A_Time'],' ',temp['C_Amb'],'C',' ', temp['D_Htsk'],'C',temp['E_PCB_Bot'],'C',' ',temp['F_PCB_Top'],'C',' ',temp['G_Q10_P4'],'C',' ',temp['H_Q2_P3'],'C',temp['I_Iin'],'A',temp['J_Vd1'],'V',' ', temp['K_Pd1'],'W',' ',temp['L_Vd2'],'V'
    results.to_csv('Thermal_Resistance_1.csv')
    time.sleep(60)   # Delay in seconds before capturing results               
print('finished')