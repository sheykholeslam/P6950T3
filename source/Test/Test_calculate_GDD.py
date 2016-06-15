import pandas as pd
import numpy as np
from nose.tools import assert_equal

# Checking GDD values. If the value < 0 than value = 0. 
def checkGDD(values):
    GDD = []
    item = 0
    for i in values:
        if i >= 0:
            item += i
        GDD.append(item)
    return GDD

# Taking the complete DataFrame and calculating GDD. Than add the GDD values as a new column. 
def calculate_GDD(Data, baseTemp):	
    Data['GDD'] = ((Data['Max'] + Data['Min'])/2)- baseTemp
    Data['GDD'] = checkGDD(Data['GDD']) 
    return Data
	
def Main():
    baseTemp = 10
    # Observed Min, Max values for test purpose. 
    obs = {'Max' : pd.Series([13.1, 4.9, 13.4, 20.7, 27.9, 18.4, 15.8, 17.9, 11.8, 15.1, 21.5, 19.8, 10.6, 15.7, 14.9]),
           'Min' : pd.Series([0.7, -1.6, -5.6, -0.6, 3.1, 3.4, -1.2, 2.4, 0.5, -1.4, 0.1, 3, 0.6, -3.2, 1])}
    obs_df = pd.DataFrame(obs)
    
    test_obs = calculate_GDD(obs_df, baseTemp)
    
    obs_GDD = np.array(test_obs['GDD'])
    obs_GDD = list(obs_GDD)
    obs_GDD = [ round(elem, 2) for elem in obs_GDD ]
    
    # Sample expected values including manually calculated GDD values to compare with Observed values. 
    exp = {'Max' : pd.Series([13.1, 4.9, 13.4, 20.7, 27.9, 18.4, 15.8, 17.9, 11.8, 15.1, 21.5, 19.8, 10.6, 15.7, 14.9]),
           'Min' : pd.Series([0.7, -1.6, -5.6, -0.6, 3.1, 3.4, -1.2, 2.4, 0.5, -1.4, 0.1, 3, 0.6, -3.2, 1]), 
           'GDD' : pd.Series([0, 0, 0, 0.05, 5.55, 6.45, 6.45, 6.60, 6.60, 6.60, 7.40, 8.80, 8.80, 8.80, 8.80])}
    exp_df = pd.DataFrame(exp)
    
    exp_GDD = np.array(exp_df['GDD'])
    exp_GDD = list(exp_GDD)
    exp_GDD =  [ round(elem, 2) for elem in exp_GDD ]
    
    assert_equal(exp_GDD, obs_GDD)

		
if __name__ == '__main__':
    Main()
