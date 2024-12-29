from pykalman import KalmanFilter

# Define Kalman Filter parameters
initial_state = [gps_data['latitude'][0], gps_data['longitude'][0], 0, 0]
transition_matrix = [[1, 0, 1, 0],
                     [0, 1, 0, 1],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]]
observation_matrix = [[1, 0, 0, 0],
                      [0, 1, 0, 0]]

kf = KalmanFilter(transition_matrices=transition_matrix,
                  observation_matrices=observation_matrix,
                  initial_state_mean=initial_state)

# Prepare the data for filtering
observations = gps_data[['latitude', 'longitude']].values
state_means, _ = kf.filter(observations)

# Add filtered data to the dataframe
gps_data['latitude_filtered'] = state_means[:, 0]
gps_data['longitude_filtered'] = state_means[:, 1]
