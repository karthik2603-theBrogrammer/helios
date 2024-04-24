# helios
 CC Project 24

 

## To Build the Image
```
docker build .
```

```
minikube start // run the minikube kubernetes image using docker.
```

## To push to hub

```
docker tag helios:latest karthiknamboori/helios:1.0 -- whatever tag you want.
```

```
docker push karthiknamboori/helios:1.0 --- push the same tag.
```


## Cron Job

```
kubectl apply -f helios-cron.yaml
```

```
kubectl delete cronjob helios
```

```
kubectl get pods --watch
```

```
kubectl logs helios-28522547-lqrj9 // do not use same pod name, user specific.
```


