import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a simulated GPS dataset
data = {
    "timestamp": pd.date_range(start="2023-01-01", periods=100, freq="T"),
    "latitude": np.cumsum(np.random.normal(0, 0.0001, 100)) + 39.92077,
    "longitude": np.cumsum(np.random.normal(0, 0.0001, 100)) + 32.85411,
}

gps_data = pd.DataFrame(data)
gps_data.head()
