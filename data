import pandas
from google.colab import drive
drive.mount('/content/gdrive', force_remount=True)

root_path = 'gdrive/MyDrive/SoftwareEngineering/'
data_path =  root_path + 'Data/'
# Input
data_file =  data_path + 'animeReviewsOrderByTime.csv'

# Delimiter
data_file_delimiter = ','

# The max column count a line in the file could have
largest_column_count = 0

# Loop the data lines
with open(data_file, 'r') as temp_f:
    # Read the lines
    lines = temp_f.readlines()

    for l in lines:
        # Count the column count for the current line
        column_count = len(l.split(data_file_delimiter)) + 1
        
        # Set the new most column count
        largest_column_count = column_count if largest_column_count < column_count else largest_column_count

# Generate column names (will be 0, 1, 2, ..., largest_column_count - 1)
column_names = [i for i in range(0, largest_column_count)]

# Read csv
df = pandas.read_csv(data_file, header=None, delimiter=data_file_delimiter, names=column_names)

# Set first row as Headers
new_header = df.iloc[0] #grab the first row for the header
df = df[1:] #take the data less the header row
df.columns = new_header #set the header row as the df header

# Create temp_df of all the columns to be concactenated and concactenate them
temp_df = df.iloc[:, 14:]
concat = pandas.Series(temp_df.fillna('').values.tolist()).str.join('')
concat.index=concat.index+1
concat = pandas.concat([pandas.Series([0]),concat])

#Add concactenated column to clean Dataset
df = df.iloc[:,:14]
df['Review']= concat

# Save cleaned dataset to Data folder in Google Drive
df.to_csv('cleaned_anime_data.csv')
!cp cleaned_anime_data.csv "gdrive/MyDrive/SoftwareEngineering/Data"
