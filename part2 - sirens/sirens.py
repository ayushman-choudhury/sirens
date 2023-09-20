import numpy as np
import pandas as pd
from scipy.io.wavfile import write
from scipy import signal

# ----------------------------------------------------------------------------------
# Define constants
samplingRate = 44100 # The sampling rate of modern audio is 44,100 samples per second
secPerNote = 0.25 # Each data point will correspond to 1/4 of a second
noteLength = int(samplingRate * secPerNote) # Expressed in samples per second 
dfCOVID = pd.read_csv("covidData.csv") # COVID data from the WHO: https://covid19.who.int/WHO-COVID-19-global-data.csv

# These could be customized by the user
# codeList = ["AFRO", "AMRO", "EMRO", "EURO", "SEARO", "WPRO"]
code = "AMRO"
freqMin = 58.3 # 98Hz corresponds to G2, 58.3Hz corresponds to Bb1
freqMax = 3000 # 1568Hz corresponds to G6, 1864.7Hz corresponds toBb6 
# ----------------------------------------------------------------------------------





# ----------------------------------------------------------------------------------
# Function getData: (regionCode) --> list of data
def getData(regionCode):
    """
    Queries the csv file for the data by region
    :param regionCode: one of "AFRO", "AMRO", "EMRO", "EURO", "SEARO", "WPRO"
    :return: a smoothed list of new COVID cases each day for that region
    """
    # Access and sum data for this region
    loc = dfCOVID[ dfCOVID["WHO_region"] == regionCode]
    locPivot = loc.pivot_table(index = "Date_reported", columns = "Country_code", values = "New_cases")
    locPivot['Sum'] = locPivot.sum(axis = 1)
    list = locPivot['Sum'].to_numpy()

    #Compute 14-day averages to smoothen out the data
    newList = np.copy(list)
    for i in range(7, len(list) - 7):
        newList[i] = sum(list[(i - 7):(i + 6)]) / 14

    return newList
# ----------------------------------------------------------------------------------





# ----------------------------------------------------------------------------------
# Function makeWav: (start, end) --> glissando between the two pitches
def makeWav(start, end):
    """
    Takes two pitch values, and returns the array of values corresponding to a 
    glissando between the two, via a Sawtooth wave
    :param start: the first pitch (Hz)
    :param end: the second pitch (Hz)
    :return: a "noteLength"-size array of pitch values
    """
    # First, correct for phase shifting:
    if end != start:
        end = (start + end)/2

    # Frequencies - a smooth progression
    freq = np.linspace(start, end, noteLength)

    # Volume - lowest note has volume 1, highest note has volume 5
    vol = ((freq - freqMin) / (freqMax - freqMin)) * 4 + 1

    # List of indices - allows us to apply a wave to the frequencies
    x = np.linspace(0, secPerNote, noteLength)
    
    # Wave = Volume * shape(2pi * Frequency * Index)
    # Sine: 
    # return vol * np.sin(2 * np.pi * freq * x/samplingRate)
    # Sawtooth:
    return 0.01 * vol * signal.sawtooth(2 * np.pi * freq * x)
# ----------------------------------------------------------------------------------





# ----------------------------------------------------------------------------------
def stagger(base):
    """
    Takes a base set of frequencies, and adds together alternates,
    staggered by a quarter noteLength, so that the blips between glissandos are hidden.
    :param base: the base array of frequencies
    :return: a new array, with the staggers
    """

    staggerUnit = int(noteLength / 4)
    # alt1 - - - -
    alt1 = np.append(base, np.zeros(staggerUnit * 4))

    # - alt2 - - -
    alt2 = np.concatenate((np.zeros(staggerUnit),
                     base,
                     np.zeros(staggerUnit * 3)))
    
    # - - alt3 - -
    alt3 = np.concatenate((np.zeros(staggerUnit * 2),
                     base,
                     np.zeros(staggerUnit * 2)))
    
    # - - - alt4 -
    alt4 = np.concatenate((np.zeros(staggerUnit * 3),
                     base,
                     np.zeros(staggerUnit)))
    
    return alt1 + alt2 + alt3 + alt4
    #return alt1 + alt3
# ----------------------------------------------------------------------------------





# ----------------------------------------------------------------------------------
def main():
        
    # Step 1: Extract the raw data
    
    print("Extracting raw data for", code, "...")
    data = getData(code)
    print("... extracted!")



    # Step 2: normalize the data to the defined frequency range
    print("Normalizing data...")
    scaledData = (data - data.min()) / (data.max() - data.min())
    freqPoints = scaledData * (freqMax - freqMin) + freqMin
    print("... normalized!")



    # Step 3: make the glissandos between freqPoints, and append them together
    print("Appending glissandos...")
    frequencies = np.zeros(1)
    for i in range(len(freqPoints) - 1):
        frequencies = np.append(frequencies, 
                makeWav(freqPoints[i], freqPoints[i + 1]))
        if (i % 100 == 0):
            print("... on glissando", i, "...")
    print("... done!")



    # Step 4: create alternate waves to hide the clips between glissandos
    print("Forming alternate waves... ")
    finalFreqs = stagger(frequencies)
    print("... formed!")



    # Step 5: layer all of these files into a single wave file, and write to WAV
    print("Writing final file...")
    write(f'waves/{code}/{code}-{freqMin}-{freqMax}.wav', samplingRate, finalFreqs)
    print("... done!")
# ----------------------------------------------------------------------------------





print("\n \n --------------------------------- ")
print("   Sirens - data query interface   ")
print(" --------------------------------- \n \n")
print("1. Select a region, as defined by the WHO.")
print("Possible regions: AFRO | AMRO | EMRO | EURO | SEARO | WPRO")
code = input("Enter code here: ")

print("\n2. Select a minimum frequency.")
print("Ex. 98Hz corresponds to G2, 58.3Hz corresponds to Bb1")
freqMin = float(input("Enter min frequency here: "))

print("\n3. Select a maximum frequency.")
print("Ex. 1568Hz corresponds to G6, 1864.7Hz corresponds to Bb6")
freqMax = float(input("Enter max frequency here: "))

print("\nEnd of interface.")
print(" ---------------------------------------- \n \n")
main()
