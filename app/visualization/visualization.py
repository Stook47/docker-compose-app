from flask import Flask, render_template
from redis import StrictRedis
import matplotlib.pyplot as plt
from mpld3 import fig_to_html

app = Flask(__name__)
redis_client = StrictRedis(host='data-store', port=6379, db =0)

@app.route('/')
def index():
    #Retrieve time series data from Redis
    data_str = redis_client.get('time_series_data')
    
    if data_str is not None:
        #Decode the bytes and evalueate the string
        data = eval(data_str.decode())
    else:
        #If 'time_series_data" key doesn't exist, must provide data
        data = {'timestamps': [], 'values': []}
    
    #Generate dynamic plot
    plt.plot(data['timestamps'], data['values'], marker='o')
    plt.xlabel('Timestamp')
    plt.ylabel('Value')
    plt.title('Randomly Generated Time Series Data')
    plt.grid(True)
    
    plot_html = fig_to_html(plt.gcf())
    
    return render_template('index.html', plot_html=plot_html)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)