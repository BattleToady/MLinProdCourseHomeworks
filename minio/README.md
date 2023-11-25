# How deploy minio?

1. Install krew: https://krew.sigs.k8s.io/docs/user-guide/setup/install/

2. Check if it was installed correctly by running:
   
```kubectl krew```

4. Install minio into your Kubernetes:

```kubectl krew install minio```

5. Init minio and create tenant:
```kubectl minio init
kubectl minio tenant create tenant1 --namespace default --servers 1 --volumes 4 --capacity 1Ti```
