from __future__ import print_function
import sys
import pandas as pd

# Set variables
basepath= '/user/baibhav/'
file_in = basepath +'test.csv'
file_out = basepath + 'duplicate.csv'
# key field value
field_name ="Incident_Number"
# read in CSV
df = pd.read_csv(file_in)
key_field = set(df[field_name].values)
header = True
print(len(df))

try:

    ids = df[field_name]
    data = pd.concat(g for _, g in df.groupby(field_name) if len(g) > 1) 
    print(len(data))
    if len(data) > 1:
        data.to_csv(file_out, mode='w', header=header, index=False)
        #header = False

    else:
        pass

    print("End time: " + str(datetime.now()))

except:
    # print error if there's a problem
    print("Unexpected error:", sys.exc_info()[0])
    raise