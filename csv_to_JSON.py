import pandas as pd
import os
import json

# Threshold to record events
THRESHOLD = 1.5

def csv_to_json(file_path, output_path):
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)

    # Calculate total acceleration magnitude
    df['total_acceleration'] = (
        (df['accelerometerAccelerationX(G)'] ** 2) +
        (df['accelerometerAccelerationY(G)'] ** 2) +
        (df['accelerometerAccelerationZ(G)'] ** 2)
    ) ** 0.5

    # Filter rows where total acceleration exceeds the threshold
    events = df[df['total_acceleration'] > THRESHOLD]

    # Select relevant columns
    detected_events = events[[
        'loggingTime(txt)', 
        'total_acceleration', 
        'accelerometerAccelerationX(G)', 
        'accelerometerAccelerationY(G)', 
        'accelerometerAccelerationZ(G)', 
        'locationTrueHeading(°)', 
        'locationLatitude(WGS84)', 
        'locationLongitude(WGS84)', 
        'locationSpeed(m/s)'
    ]]

    # Rename columns for better readability
    detected_events.rename(columns={
        'loggingTime(txt)': 'time',
        'total_acceleration': 'totalAcceleration',
        'accelerometerAccelerationX(G)': 'accelX',
        'accelerometerAccelerationY(G)': 'accelY',
        'accelerometerAccelerationZ(G)': 'accelZ',
        'locationTrueHeading(°)': 'heading',
        'locationLatitude(WGS84)': 'latitude',
        'locationLongitude(WGS84)': 'longitude',
        'locationSpeed(m/s)': 'speed'
    }, inplace=True)

    # convert to JSON
    json_data = detected_events.to_dict(orient="records")

    # write JSON to file
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

    print(f"JSON data saved to {output_path}")
    return json_data

if __name__ == "__main__":
    # example usage
    csv_file_path = "/Users/michael/Desktop/EventLogger/uploads/2024-11-19_10_42_56_my_IOS_device.csv"  # Path to your CSV file
    json_file_path = "/Users/michael/Desktop/EventLogger/converted_data/data.JSON"  # Output path for JSON
    csv_to_json(csv_file_path, json_file_path)
