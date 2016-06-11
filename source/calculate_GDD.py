def checkGDD(values):
    GDD = []
    item = 0
    for i in values:
        if i >= 0:
            item += i
        GDD.append(item)
    return GDD
	
def calculate_GDD(Data, baseTemp):	
    Data['GDD'] = ((Data['Max Temp (°C)'] + Data['Min Temp (°C)'])/2)- baseTemp
    Data['GDD'] = checkGDD(Data['GDD']) 
    return Data