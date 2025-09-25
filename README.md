# Kubernetes HPA & Grafana Demo

This project demonstrates how to deploy a simple CPU-bound application on Azure Kubernetes Service (AKS), monitor it with Prometheus + Grafana, and watch the Horizontal Pod Autoscaler (HPA) scale replicas up and down under load.

---

## Demo

The Horizontal Pod Autoscaler scales from 2 → 5 pods under CPU load, then back down as load subsides.
![HPA scaling demo](docs/img/demo-1.gif)

---

## 🚀 Features

- **Horizontal Pod Autoscaler (HPA)** — scales pods automatically based on CPU usage (% of requested resources).
- **Prometheus Metrics** — scrapes container CPU usage and HPA target metrics.
- **Grafana Dashboard** — includes:
  - Current Replica Count
  - Replica Count Over Time
  - Cluster CPU Usage (all nodes)
  - CPU Utilization vs HPA Target & Measured
  - Pod Restarts / Health

---

## ⚙️ Prerequisites

- An AKS cluster (or any Kubernetes cluster)
- `kubectl` configured
- Helm installed
- Prometheus & Grafana installed (via [kube-prometheus-stack](https://artifacthub.io/packages/helm/prometheus-community/kube-prometheus-stack) or another method)

---

## 🛠 Deploy the Demo App & HPA

```bash
kubectl apply -f manifests/deployment.yaml
kubectl apply -f manifests/hpa.yaml
```

### Confirm resources:

```bash
kubectl get pods -n app
kubectl get hpa -n app
```

---

## 📊 Install Prometheus & Grafana

### Using Helm (example):

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

helm install monitoring prometheus-community/kube-prometheus-stack \
  --namespace monitoring --create-namespace
```

### Port-forward Grafana (if not exposed via ingress):

```bash
kubectl port-forward svc/monitoring-grafana -n monitoring 3000:80
```

### Login with default credentials:

- **username:** admin
- **password:** prom-operator

---

## 📈 Load Test to Trigger Scaling

### Run a CPU load against the app to see the HPA react:

```bash
URL="http://<your-service-ip-or-dns>/cpu?seconds=2"
while true; do curl -s "$URL" > /dev/null; done
```

- This loop will keep sending CPU-intensive requests, causing the HPA to add replicas.

### Watch scaling in real time:

```bash
kubectl -n app get hpa -w
kubectl -n app get pods -o wide
```

---

## 🔥 Watch the Dashboard

- **Current Replicas** — shows how many pods are running now

- **Replica Count Over Time** — see the autoscaler history

- **Cluster CPU Usage (all nodes)** — total CPU usage across the cluster

- **CPU Utilization vs HPA Target & Measured** — shows how the HPA adjusts to maintain target CPU

- **Pod Restarts / Health** — quick check for pod stability

---

## 🧹 Tear Down

```bash
kubectl delete -f manifests/hpa.yaml
kubectl delete -f manifests/deployment.yaml
```
