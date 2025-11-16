#Function

# def describe_dataset():
#   print("This function summarizes key statistics of a dataset")

# describe_dataset()

# Creating a Real Dataset

#import pandas as pd

#Create a sample data
# data = pd.DataFrame({
#   "region": ["North", "South", "North", "West", None],
#   "sales": [1200, 1500, None, 1100, 900]
# })


# print("Original Data")
# print()
# print(data)



#cleaning missing values
# let's make a function that removes rows with missing values

import pandas as pd

#Create a sample data
# data = pd.DataFrame({
#   "region": ["North", "South", "North", "West", None],
#   "sales": [1200, 1500, None, 1100, 900]
# })

# def clean_missing_value(df):
#   """Remove rows with missing values and reports how many were removed"""

#   before = len(df)   #number of rows before cleaning
#   df = df.dropna()   # drops rows with any missing values

#   after = len(df)  # number of rows after cleaning

#   print(f"Removed {before - after} rows with missing data.")

#   return df

# clean_data = clean_missing_value(data)
# print("\nCleaned Data.")
# print(clean_data)


#Try...Except

# try:
#   numbers = [10, 20, 0, 30]
#   average = sum(numbers) / len(numbers)
#   print("Average:", average)

# except:
#   print("Something went wrong while calculating the average")

# try:
#   numbers = ["John", false]
#   average = sum(numbers) / len(numbers)
#   print("Average:", average)
# except ZeroDivisionError:
#   print("Cannot divide by zero - your data list is empty")
# except TypeError:
#   print("Make sure all data points are numeric.")
# except NameError:
#    print("Make sure all data points are of valid data type name")

#else:
# try:
#   scores = [85, 90, 78, 92]
#   avg = sum(scores) / len(scores)

# except:
#   print("Error while processing scores")

# else:
#   print(f"Average score: {avg}")

#finally


try:
  data = [0, "Dan"]
  result = sum(data) /len(data)
  print("Average:", result)

except:
  print("Something went wrong during analysis")

finally:
  print("Analysis step completed")

# If your data does not meet expectations, you can manually raise an error
# Raise an Exception
missing_values = 12

if missing_values > 0:
  raise Exception("Dataset contains missing values. Clean data before analysis")

data = "234", "456", "789" # Should be a list, not a string

if not isinstance(data, list):
  raise TypeError("Data must be in a list format, not a string")

# File handling