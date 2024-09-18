# Projects
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 1. Truck Company Trip Reconstruction
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


This project focuses on reconstructing the travel routes of trucks based on log data, calculating mileage, and matching sample trips to trucks based on distance and route similarity.

### Modules Used:

Pandas: for CSV data manipulation
NumPy: for mathematical operations and missing data handling
itertools.permutations: for possible trip combinations

### Key Functions:

trip_distance: Calculates the total trip distance based on routes.
get_truck_mileage_diffs: Extracts mileage differences from truck logs.
find_valid_trip_greedy: Greedy algorithm to reconstruct valid trips for trucks.
Reconstructed Trip Matching: Matches reconstructed trips to sample trips based on distance similarity.

### Input Files:

routes.csv: Contains route information.
logs.csv: Contains log data with truck mileage.
sample_trip.csv: Sample trip data for truck identification.

### Outputs:

reconstructed.csv: CSV containing reconstructed trips.
Log message output identifying which truck is responsible for a given sample trip.

## 2. Mass Spectrometer Control & Time Drift Analysis
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This project is designed for real-time mass spectrometry control, detecting important peptides and calculating time drift between expected and measured times.

### Modules Used:
Pandas: for CSV data manipulation
NumPy: for numerical operations
SciPy: for distance metrics
Seaborn & Matplotlib: for visualization
CDIST: for computing distance between sample and library peptides

### Key Functions:
is_important: Identifies whether a peptide measurement is deemed important based on mass and charge.
instrument_gen: A generator that yields each peptide measurement from the sample.
Time Drift Calculation: Computes the time drift by comparing measured vs expected peptide retention times.

### Input Files:
library.csv: Contains important peptide information (mass, charge, time).
measurement.csv: Real-time peptide measurements from the mass spectrometer.

### Outputs:

observed_drift.jpg: Visualization showing the time drift between expected and observed peptide retention times.
Mean and standard deviation of time drift values printed in the console.
Experience Demonstrated
With over five years of experience in data science, the code in this repository showcases expertise in:

1. Data Wrangling: Effective use of Pandas and NumPy to manipulate large datasets.
2. Algorithm Development: Creation of a greedy algorithm to solve route reconstruction problems.
3. Real-Time Data Processing: Implementation of a generator for real-time data handling in the mass spectrometry control system.
4. Statistical Analysis & Visualization: Advanced statistical analysis with SciPy and visualizations using Seaborn/Matplotlib, including regression modeling and drift distributions.
5. Installation and Usage

### Requirements:

Python 3.8 or higher
Required Libraries:

code
pip install pandas numpy scipy seaborn matplotlib

### Running the Projects:
Truck Company Trip Reconstruction:

Place the routes.csv, logs.csv, and sample_trip.csv files in the appropriate directory.
Run the Truck_Company.py script to output the reconstructed trips and identify the truck associated with the sample trip.
Mass Spectrometer Control & Time Drift Analysis:

Place the library.csv and measurement.csv files in the appropriate directory.
Run the Mass_spectrometer_control.py script to generate visualizations and drift statistics.

### Outputs:

For the Truck Reconstruction project, the result will be a CSV file with reconstructed trips and log messages identifying trucks.
For the Mass Spectrometer Control project, the result will be a drift plot saved as observed_drift.jpg and printed drift statistics.
Future Enhancements:
Route Optimization: Extend the truck reconstruction algorithm to use optimization techniques such as dynamic programming for more accurate trip reconstruction.
Machine Learning Integration: Use ML models to predict important peptide detections based on historical data.
Parallel Processing: Enhance performance for large datasets by incorporating multiprocessing techniques.

### License:

This project is licensed under the MIT License - see the LICENSE file for details.
