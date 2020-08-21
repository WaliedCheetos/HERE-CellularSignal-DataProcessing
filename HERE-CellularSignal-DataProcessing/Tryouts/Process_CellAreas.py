import  math, traceback, sys, os, time, random, md5, datetime, json


##jsonFile = 'C:/Users/ahmadmoh/O_o/HERE/Data/Cellular Signals/HERE Cellular Signals GeoJSON MEA S191_G1 RevA/CELLULAR_191G1_MEA_DCEL2/CELLULAR_191G1_MEA_DCEL2-ARE/json1.json'
#jsonFile = 'C:/Users/ahmadmoh/O_o/HERE/Data/Cellular Signals/HERE Cellular Signals GeoJSON MEA S191_G1 RevA/CELLULAR_191G1_MEA_DCEL2/CELLULAR_191G1_MEA_DCEL2-ARE/FeatureCollection_are_cellularArea_1433 - Copy.json'
jsonFile = 'C:\\Users\\ahmadmoh\\O_o\\HERE\\Data\\Cellular Signals\\CELL_GEOJSON_201E0_ARE\\sample_FeatureCollection_are_cellularArea_1433.json'

##The magic starts here.
##

def remove_uni(s):
    """remove the leading unicode designator from a string"""
    if s.startswith("u'"):
        s2 = s.replace("u'", "'", 1)
    elif s.startswith('u"'):
        s2 = s.replace('u"', '"', 1)
    return s2

try:


    
    print("WaliedCheetos: Hollla ...!!!")

    with open(jsonFile) as json_file:
        data = json.load(json_file)
        for feature in data['cellularAreas']:
            ##print((str(feature['features'])[1:-1]).encode()
            print(json.dumps(feature['features'][0]))+','
            #print('geometry: ' + feature['geometry'])
            #print('properties: ' + p['properties'])
            #print('From: ' + p['type'])
            #print('==========================================================')


    
except Exception as e:
    #log exception
    #
    print("A Python error occured", "ERROR")
    msgs = traceback.format_exception(*sys.exc_info())
    for msg in msgs:
        print(msg.strip(), "ERROR")
    
finally:
    print("WaliedCheetos: Done ...!!!")
