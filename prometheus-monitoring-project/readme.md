# Prometheus Monitoring Project

## Prerequisites
- Docker
- Docker network

## Setup and Running

1. Create a Docker network:
```bash
docker network create monitoring-network
```

2. Build and run the Python Application:
```bash
# Navigate to app directory
docker build -t python-app .
docker run -d --name python-app --network monitoring-network -p 5000:5000 python-app
```

3. Build and run Prometheus:
```bash
# Navigate to prometheus directory
docker build -t custom-prometheus .
docker run -d --name prometheus --network monitoring-network -p 9090:9090 custom-prometheus
```

4. Build and run Alertmanager:
```bash
# Navigate to alertmanager directory
docker build -t custom-alertmanager .
docker run -d --name alertmanager --network monitoring-network -p 9093:9093 custom-alertmanager
```

5. Build and run Grafana:
```bash
# Navigate to grafana directory
docker build -t custom-grafana .
docker run -d --name grafana --network monitoring-network -p 3000:3000 custom-grafana
```

## Accessing Services
- Python App Metrics: http://localhost:5000/metrics
- Prometheus: http://localhost:9090
- Alertmanager: http://localhost:9093
- Grafana: http://localhost:3000 (default credentials: admin/admin)

## Grafana Dashboard Configuration
1. Add Prometheus as a data source
2. Import a dashboard for Python application metrics
3. Create custom panels for:
   - Total Requests
   - Exceptions
   - Temperature
   - Humidity
