import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
from scipy import stats
import seaborn as sns


# Load data into df from csv
library = pd.read_csv('C://Users//User//Documents//Challenge_remote//library.csv')
sample = pd.read_csv('C://Users//User//Documents//Challenge_remote//measurement.csv')

# Print of column names to check available values
print("Columns in library:", library.columns)
print("Columns in sample:", sample.columns)

# Use here 'important'
imp_peptides = library[library['Important'] == True]

# Print peptides.
print("First few rows of imp_peptides:")
print(imp_peptides.head())

def instrument_gen(): # generator designed to iterate over dataframe sample, one raw at time
    for i in range(len(sample)):
        yield sample.iloc[i]
# instrument generator added
instrument = instrument_gen()

# Prints message when peptide is observed:
def do():
     print("Important peptide detected! Adjusting instrument settings.")
# Check function : given measurement considered "important" by comparing different peptides :
def is_important(measurement, imp_peptides, tolerance=0.01):
        measurement_array = np.array([[measurement['Mass'], measurement['Charge']]])
        library_array = imp_peptides[['Mass', 'Charge']].values
        distances = cdist(measurement_array, library_array)
        return np.any(distances < tolerance)

# This is main loop: initialise two empty lists
expected_t = []
measured_t = []

# Recover next measurement from instrument generator
while True:
        try:
            measurement = next(instrument)
            if is_important(measurement, imp_peptides): # checks is_important function
                do()
            library_match = library[(library['Mass'].round(2) == round(measurement['Mass'], 2)) &
                                    (library['Charge'] == measurement['Charge'])] # makes effort to find match for measurement (mass , charge) of library df
            if not library_match.empty: # if match found appends expected time
                expected_t.append(library_match.iloc[0]['Time'])
                measured_t.append(measurement['Time'])
        except StopIteration: # StopIteration raised for no more measurements
            break

# Visualized time drift here:
# time drift calculated :
expected_t = np.array(expected_t)
measured_t = np.array(measured_t)
time_drift = measured_t - expected_t

# plot generated :
plt.figure(figsize=(12, 8))
sns.set_style("whitegrid")
sns.set_palette("deep")

#  Scatter plot (alpha blending)
sns.scatterplot(x=expected_t, y=measured_t)

# correlation included :

# Regression included with confidence interval :
sns.regplot(x=expected_t, y=measured_t, scatter=False, color='g', label='Regression Line')

# plot labels and size :
plt.title('Time Drift Analysis(Peptide Measurements)', fontweight='bold')

# histogram plot of time drift :
axins = plt.axes([0.65, 0.15, 0.25, 0.25])
sns.histplot(time_drift, kde=True, ax=axins)
axins.set_title('Time Drift Distribution', fontsize=10)
axins.set_xlabel('Time Drift (min)', fontsize=8)
axins.tick_params(axis='both', which='major', labelsize=8)
plt.legend(fontsize=12)
plt.tight_layout()
plt.savefig('C:/Users/User/Documents/remote_challenge/observed_drift.jpg', dpi=300)
plt.show()
# Calculated drift statistics here
time_diff = np.array(measured_t) - np.array(expected_t)

print(f"Mean_tim(drift): {np.mean(time_diff):.2f} ")
print(f"SD_time(drift): {np.std(time_diff):.2f} ")