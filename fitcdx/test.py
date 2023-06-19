import csv
import pandas as pd



act_list = ["Outdoor Running_27th May","Outdoor Cycling_27th May","Steps Count_27th May","Outdoor Running_28th May","Outdoor Cycling_28th May","Steps Count_28th May","Steps Count_29th May","Steps Count_30th May","Steps Count_31st May","Steps Count_1st June","Steps Count_2nd June","Steps Count_3rd June","Outdoor Running_3rd June","Outdoor Cycling_3rd June","Steps Count_4th June","Outdoor Cycling_4th June","Outdoor Running_4th June"]

fitcdx = pd.read_csv("fitcdx.csv",index_col=0)
teams = fitcdx['teamName'].unique().tolist

def get_data_fun_params(url,activity,team):

    """ This function will fecth the data from api url and return the data"""

    import requests
    from requests.packages.urllib3.exceptions import InsecureRequestWarning

    # Disable SSL certificate verification warning
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    params ={
        'activity':activity,
        'teamName':team
    }

    # Make a GET request to the API endpoint
    response = requests.get(url,verify=False,params=params)

    # Check the response status code
    if response.status_code == 200:
        # Request was successful
        data = response.json()
        # Process the data as needed
        return data
    else:
        # Request failed
        print('Error:', response.status_code)




for team in teams():
    for activity in act_list:
        data = get_data_fun_params("https://vlgspfitcdx.devsys.net.sap:4430/point",activity,team)
        
        for dict_item in data:
            activity_dict = []
            new_dict = dict_item
            new_dict['activity'] = activity
            new_dict['team'] = team
            activity_dict.append(new_dict)
            
            filename = "data.csv"
            # Write the dictionary to the CSV file
            # Extract field names from the first dictionary
            fieldnames = data[0].keys()

            with open(filename, "a", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
    