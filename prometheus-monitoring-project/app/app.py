from flask import Flask, Response
import prometheus_client
from prometheus_client import Counter, Gauge, generate_latest, CONTENT_TYPE_LATEST
import random
import time
import threading

app = Flask(__name__)

# Define Prometheus metrics
REQUESTS = Counter('app_requests_total', 'Total number of requests')
EXCEPTIONS = Counter('app_exceptions_total', 'Total number of exceptions')
TEMPERATURE = Gauge('app_temperature_celsius', 'Current temperature')
HUMIDITY = Gauge('app_humidity_percent', 'Current humidity')

@app.route('/')
def home():
    REQUESTS.inc()
    return "Welcome to the Monitoring Demo App!"

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

def simulate_sensor_data():
    while True:
        try:
            # Simulate temperature and humidity readings
            temp = random.uniform(20.0, 30.0)
            humidity = random.uniform(40.0, 60.0)
            
            TEMPERATURE.set(temp)
            HUMIDITY.set(humidity)
            
            # Simulate occasional exceptions
            if random.random() < 0.05:  # 5% chance of exception
                raise Exception("Random simulated error")
            
            time.sleep(5)
        except Exception as e:
            EXCEPTIONS.inc()
            print(f"Simulated error: {e}")

if __name__ == '__main__':
    # Start sensor data simulation in a background thread
    sensor_thread = threading.Thread(target=simulate_sensor_data)
    sensor_thread.daemon = True
    sensor_thread.start()
    
    app.run(host='0.0.0.0', port=5000)
