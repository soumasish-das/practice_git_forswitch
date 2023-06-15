# import pandas library
import pandas as pd

# dictionary with list object in values
details = {
    'Name': ['Ankit', 'Aishwarya', 'Shaurya', 'Shivangi'],
    'Age': [23, 21, 22, 21],
    'University': ['BHU', 'JNU', 'DU', 'BHU'],
}

# creating a Dataframe object
df = pd.DataFrame(details, columns=['Name', 'Age', 'University'],
                  index=['a', 'b', 'c', 'd'])
print(df)
# Get the number of columns
print("Number of Columns:", len(df))





