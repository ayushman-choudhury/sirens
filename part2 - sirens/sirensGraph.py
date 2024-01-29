import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dfCOVID = pd.read_csv("covidData.csv") # COVID data from the WHO: https://covid19.who.int/WHO-COVID-19-global-data.csv

# ----------------------------------------------------------------------------------
# Function getData: (regionCode) --> list of data
def getData(regionCode):
    """
    Queries the csv file for the data by region
    :param regionCode: one of "AFRO", "AMRO", "EMRO", "EURO", "SEARO", "WPRO"
    :return: a smoothed list of new COVID cases each day for that region, as a percentage of the maximum case count
    """
    # Access and sum data for this region
    loc = dfCOVID[ dfCOVID["WHO_region"] == regionCode]
    locPivot = loc.pivot_table(index = "Date_reported", columns = "Country_code", values = "New_cases")
    locPivot['Sum'] = locPivot.sum(axis = 1)
    list = locPivot['Sum'].to_numpy()

    # Compute 14-day averages to smoothen out the data
    newList = np.copy(list)
    for i in range(7, len(list) - 7):
        newList[i] = sum(list[(i - 7):(i + 6)]) / 14

    # Compute maximum, for scaling
    maxVal = newList.max()

    return (newList / maxVal) * 100
# ----------------------------------------------------------------------------------


print("\n \n --------------------------------- ")
print("   Sirens - creating graph   ")

# Call function to get data across all regions

afro = getData("AFRO")
amro = getData("AMRO")
emro = getData("EMRO")
euro = getData("EURO")
searo = getData("SEARO")
wpro = getData("WPRO")

dates = dfCOVID["Date_reported"][0:len(afro)]

# Create a plot of this data

plt.figure(figsize=(10, 7))
plt.plot(dates, afro, label='Africa')
plt.plot(dates, amro, label='Americas')
plt.plot(dates, emro, label='East Mediterranean')
plt.plot(dates, euro, label='Europe')
plt.plot(dates, searo, label='Southeast Asia')
plt.plot(dates, wpro, label='Western Pacific')

plt.xlabel('Date')
plt.ylabel('New COVID Cases (% of max by region)          ')
plt.legend(loc='center', bbox_to_anchor = (-0.25,0.2))
plt.xticks(dates[[0, 364, 729, 1094]])
plt.savefig('sirensPlot.jpg', dpi=300, bbox_inches='tight')

print("\nGraph saved!")