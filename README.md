# K8S-Exercise
Deploy a Simple Web Application to Kubernetes

## Create AKS cluster using Terraform

```bash
az login
az account list
az account set --subscription <id>
cd terraform
terraform init
terraform plan
terraform apply
az aks get-credentials --resource-group devTest --name devDemo
```

## Deploy the flask app to AKS

```bash
kubectl get svc -n ingress
kubectl apply -f k8s/
kubectl get pods
kubectl get ing
curl --resolve "flask.dev.local:80:<External ingress ip>" http://flask.dev.local/
```

## Implement rolling updates or rollbacks for the deployment.

```bash
--
Update the flask image container with v2
--
cd k8s
kubectl apply -f flask-app-deployment.yaml --record
kubectl rollout status deployment flask-app
kubectl rollout history deployment flask-app
kubectl get pods
kubectl get ing
curl --resolve "flask.dev.local:80:<External ingress ip>" http://flask.dev.local/

--
Roll back to a specific revision
--

kubectl rollout undo deployment flask-app --to-revision=<revision_number>
kubectl rollout status deployment flask-app
kubectl get pods
kubectl get ing
curl --resolve "flask.dev.local:80:<External ingress ip>" http://flask.dev.local/
```
