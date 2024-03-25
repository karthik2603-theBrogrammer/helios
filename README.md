# helios
 CC Project 24


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
kubectl logs helios-28522547-lqrj9
```


## TO push to hub

```
docker tag helios:latest karthiknamboori/helios:1.0 -- whatever tag you want.
```

```
docker push karthiknamboori/helios:2.0 --- push the same tag.
```