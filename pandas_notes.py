#Pandas notes:

'''
access data by index in series rather than dictionary key
use .iloc[] with the number of the index in the square brackets,
	to select row in a df, or item in a series
use .loc['indexName'] to select a row by index
use df['columnName'] to get a column

.loc & .iloc return a row series, iloc uses #'s for position, loc names
df['column'] returns a column series

example:
countries.loc['America' : 'Canada', 'Population'] -returns rows America through Canada (inclusive), with only Population info

~ = not
| = or
& = and

df.plot() #will plot the data frame using matplotlib

##Checking for empty values:
pd.isnull()
pd.isna()
or
pd.notnull()
pd.notna()


seriesName.dropna() -> returns series without null values 

seriesName.fillna(0) #fills na with value 0
seriesName.fillna('nothing here bro') ...

#fill null dataframe
df.fillna(method='ffill', axis=0) #forward fills null data vertically (in columns)
df.fillna(method='ffill', axis=1) #forward fills null data along the row


##Replace invalid values
df['Sex'].replace({'D': 'F', 'N': 'M'}) #changes D values to F, and N to M

#find duplicates
seriesName.duplicated() #returns true for any value that is duplicated (2nd+ occurance will be true)
seriesName.duplicated(keep='last') #returns true for 1st occurance if it is repeated later is series
seriesName.drop_duplicates() #drops any repeated value


'''