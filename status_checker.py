# Put your url list in urls
urls = []

# a list where all the data is displayed, for the dataframe which will be exported as a sheet
status_list = []
for url in urls:

  # initialize the url status to default
    url_status = ''
    
    # status_d gives the status, up(site is good), yellow (site has errors , 403, 404), down (site cannot be reached)
    status_d = ''
    print(url)
    try:
        r = requests.get(url)
        status = r.status_code
        if status == 200:
            status_d = "up"
        else:
            status_d = "yellow"
    except Exception as e:
        status_d = "down"
        status = 0
    print(status_d)
    print(status) 
    
    url_status = [url,status_d, status]
    status_list.append(url_status)
    
print(status_list)

# export the data to a excel csv

import pandas as pd

df = pd.DataFrame(status_list)
df.to_csv('status_check.csv', index=False)
