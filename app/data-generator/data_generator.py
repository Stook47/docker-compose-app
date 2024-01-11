import time
import random
import matplotlib.pyplot as plt
from redis import StrictRedis

redis_client = StrictRedis(host='data-store', port=6379, db=0)

#Number of data points to generate
num_points = 50

while True:
    #Generate random time series data
    timestamps = [time.time() - i for i in range(num_points)]
    values = [random.randint(1, 100) for _ in range(num_points)]
    
    data = {
        'timestamp': timestamps,
        'values': values
    }
    
    #Store data in Redis
    redis_client.set('time_series_data', str(data))
    
    #Plot the Data
    plt.plot(timestamps, values, marker='o')
    plt.xlabel('Timestamp')
    plt.ylabel('Value')
    plt.title('Randomly Generated Time Plot')
    plt.grid(True)
    plt.savefig('/app/static/plot.png') #Save as image so it can be referenced in HTML code
    plt.close()
    
    time.sleep(3)