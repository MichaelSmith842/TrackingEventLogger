import pandas as pd

# threshold to record event. 
THRESHOLD = 1.5  

# process the CSV
def process_csv(file_path):
    # load CSV
    df = pd.read_csv(file_path)

    # total acceleration magnitude
    df['total_acceleration'] = (
        (df['accelerometerAccelerationX(G)'] ** 2) +
        (df['accelerometerAccelerationY(G)'] ** 2) +
        (df['accelerometerAccelerationZ(G)'] ** 2)
    ) ** 0.5

    # only rows where acceleration exceeds the threshold
    events = df[df['total_acceleration'] > THRESHOLD]

    # relevant columns 
    detected_events = events[[
        'loggingTime(txt)', 
        'total_acceleration',  
        'accelerometerAccelerationX(G)',
        'accelerometerAccelerationY(G)',
        'accelerometerAccelerationZ(G)',
        'locationTrueHeading(°)',  # heading
        'locationLatitude(WGS84)',  # lat
        'locationLongitude(WGS84)',  # long
        'locationSpeed(m/s)'  # speed
    ]]

    # re naming the columns 
    detected_events.rename(columns={
        'loggingTime(txt)': 'Timestamp',
        'accelerometerAccelerationX(G)': 'Accel_X',
        'accelerometerAccelerationY(G)': 'Accel_Y',
        'accelerometerAccelerationZ(G)': 'Accel_Z',
        'locationTrueHeading(°)': 'Heading',
        'locationLatitude(WGS84)': 'Latitude',
        'locationLongitude(WGS84)': 'Longitude',
        'locationSpeed(m/s)': 'Speed'
    }, inplace=True)


    print("Detected Events:")
    print(detected_events)

    # Save the results to a new CSV file (optional)
    output_file = "data/detected_events.csv"
    detected_events.to_csv(output_file, index=False)
    print(f"Results saved to {output_file}")



if __name__ == "__main__":
    # change file path to the path of your csv file 
    file_path = "/Users/michael/Desktop/EventLogger/uploads/2024-11-19_10_42_56_my_IOS_device.csv"
    process_csv(file_path)
