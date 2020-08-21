import requests
import pandas as pd
import json

URL = "https://geocode.search.hereapi.com/v1/geocode"
api_key = 'AiDeDsNBuN_8cik-NqBz1EzftssyzBYBSHNvkc7uHZQ' # Acquire from developer.here.com
excel_input = r'C:\Users\ahmadmoh\O_o\HERE\OneDrive\OneDrive - HERE Global B.V-\HERE\Customers\InCube\SampleDataUAE.xlsx'

#read excel sheet content into a pandas data frame
df = pd.read_excel(excel_input, sheet_name='Sheet1')
responses = []
#loop excel sheet, and read each delivery address value
for i in df.index:
    
    #taking delivery address value
    #location = df['Address'][i] + ", " + df['Area'][i] + ", " + df['City'][i]
    if str(df['City'][i]) == 'nan':
        location = df['Address'][i]
    else:
        location = str(df['Address'][i]) + ", " + str(df['City'][i])
    #location = input("Enter the location here: ") #taking user input

    #construct your request body
    PARAMS = {'apikey':api_key,'q':location} 

    # sending get request and saving the response as response object 
    r = requests.get(url = URL, params = PARAMS)

    #read response
    data = r.json()

    if len(data['items']) > 0:
        latitude = data['items'][0]['position']['lat']
        longitude = data['items'][0]['position']['lng']
        title = data['items'][0]['title']
        resultType = data['items'][0]['resultType']
        responses.append([i, df['Address'][i], df['Area'][i], df['City'][i], latitude, longitude, title, resultType, r.text])

    else:
        responses.append([i, df['Address'][i], df['Area'][i], df['City'][i], '', '', '', '', r.text])

df_response = pd.DataFrame(responses, columns=["id", "address", "area", "city", "lat", "lng", "title", "result_type", "json_response"])

with pd.ExcelWriter(excel_input, engine='xlsxwriter') as writer:    
    df_response.to_excel(writer, 'responses')
    writer.save()
    writer.close()

#with pd.ExcelWriter(excel_input) as writer:
#    writer.book = openpyxl.load_workbook(excel_input)
#    df_response.to_excel(writer, sheet_name='responses')






