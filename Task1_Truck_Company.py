import pandas as pd
import numpy as np
from itertools import permutations

# Read CSV files :
routes = pd.read_csv('C://Users//User//Documents//Challenge_remote//routes.csv')
logs = pd.read_csv('C://Users//User//Documents//Challenge_remote//logs.csv')
sample_trip = pd.read_csv('C://Users//User//Documents//Challenge_remote//sample_trip.csv')

# print data frame details :
print("Routes DataFrame:")
print(routes)
print("\nLogs DataFrame:")
print(logs.head())
print("\nSample Trip DataFrame:")
print(sample_trip)

# calculate trip distance with trips and routes :
def trip_distance(trip, routes):
    total_distance = 0
    for route in trip:
        if route in routes['route_1'].values:
            total_distance += routes[routes['route_1'] == route].iloc[0, 1]
    return total_distance


# Received mileage differences for a truck by function :
def get_truck_mileage_diffs(truck_logs):
    mileage_cols = [col for col in truck_logs.columns if col.startswith('Log #')]
    mileages = truck_logs[mileage_cols].values.flatten()
    mileages = mileages[~np.isnan(mileages)]
    return np.diff(mileages)


# greedy approach Function used for valid trip :
def find_valid_trip_greedy(truck_mileage_diffs, routes, num_destinations=8):
    all_routes = routes['route_1'].tolist()
    trip = []
    remaining_diff = truck_mileage_diffs[0]

    for _ in range(num_destinations):
        best_route = min(all_routes, key=lambda r: abs(trip_distance([r], routes) - remaining_diff))
        trip.append(best_route)
        all_routes.remove(best_route)
        route_distance = trip_distance([best_route], routes)
        remaining_diff -= route_distance

        if len(truck_mileage_diffs) > 1:
            truck_mileage_diffs = truck_mileage_diffs[1:]
            remaining_diff = truck_mileage_diffs[0]

    return trip


# Calculated Individual truck trips reconstruction and storage(list)
reconstructed_trp = []

for truck in logs['Truck'].unique():
    truck_logs = logs[logs['Truck'] == truck]
    mileage_diffs = get_truck_mileage_diffs(truck_logs) # mileage_diffs calculated
    valid_trip = find_valid_trip_greedy(mileage_diffs, routes) # valid trip by greedy approach function

    reconstructed_trp.append({
        'Truck': truck,
        'Reconstructed Trip': ' -> '.join(valid_trip),
        'Total Distance': trip_distance(valid_trip, routes)
    })

# generated new DataFrame with the reconstructed trips
reconstructed_df = pd.DataFrame(reconstructed_trp)
# Print reconstructed trips
print("\nReconstructed Trips DataFrame:")
print(reconstructed_df)

# Converted reconstructed trips into a CSV file
reconstructed_df.to_csv('C://Users//User//Documents//remote_challenge//reconstructed.csv', index=False)
print("\nReconstructed trips have been saved to 'C://Users//User//Documents//remote_challenge//reconstructed.csv'")

# Step to identify the truck corresponding to the sample trip
print("\nSample Trip DataFrame:")
print(sample_trip)
print(f"sample trip Shape: {sample_trip.shape}")
print(f"sample trip Columns: {sample_trip.columns}")

if sample_trip.empty:
    print("The sample_trip DataFrame is empty.")
else:
    # Assuming here the routes are the columns of the sample_trip DataFrame
    trip_routes = sample_trip.columns.tolist()
    trip_distance = trip_distance(trip_routes, routes)

    match_truck = None
    match_score = float('inf')

    for _, row in reconstructed_df.iterrows():
        reconstructed_trip = row['Reconstructed Trip']
        reconstructed_distance = row['Total Distance']

        # score here based on route similarity and different distance
        route_similarity = len(set(trip_routes) & set(reconstructed_trip)) / len(trip_routes)
        distance_difference = abs(trip_distance - reconstructed_distance)

        score = (1 - route_similarity) + (distance_difference / trip_distance)

        if score < match_score:
            match_score = score
            match_truck = row['Truck']

    print(f"\n truck of the sample trip is: {match_truck}")
    print(f"Trip distance: {trip_distance:.2f}")