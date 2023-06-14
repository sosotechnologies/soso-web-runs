```
docker build -t sosotech/sosotech:6.13.1 .
docker run -itd -p  5000:5000 sosotech/sosotech:6.13.1
```

***encode the DB password***
***Add the encoded password to your secret***

```
echo -n 'Depay50#' | base64
```

***login to pod***

```
kubectl exec -it mysql-deployment-78bb878564-7n2x5 -- mysql -uroot -p
```

***database commands***

```
show databases;
CREATE DATABASE sosotechreal;
use sosotechreal;
show tables;
select * from register;
```

***get the mysql pod IP and pass to the SQLACHRMY connection string***

```
kubectl get pod <pod> -o jsonpath='{.status.podIP}'

kubectl get pod mysql-deployment-78bb878564-7n2x5 -o jsonpath='{.status.podIP}'
```

***Tell OpenAI***
create the following:  
- flask login app with mysql backend
- dockerfile for the app
- flask app kubernetes deployment
- flask app kubernetes service
- kubernetes configmap
- kubernetes secret
- mysql deployment
- mysql service
- pv and pvc