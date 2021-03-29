# Datavant K8s Dev Demo

## Installation

Install `kubectl`, `minikube`, and `skaffold`:

```
brew install kubectl minikube skaffold
```

Enable `nginx-ingress`:

```
minikube addons enable ingress
```

If this doesn't work, you may need to [change your vm driver](https://github.com/kubernetes/minikube/issues/7332#issuecomment-730565633):

```
minikube config set vm-driver hyperkit
minikube delete
minikube start
minikube addons enable ingress
```

## Developing

First, make sure you're in your local context:

```
kubectl config use-context minikube
```

Then from the root directory of this repo build the docker images:

```
make build
```

and then start the demo app:

```
make start
```

Navigate to the IP address printed by this command:

```
minikube ip
```

and you will see the app. All changes you make to both the app (located at `/`) and the api (located at `/api`) will be hot reloaded.
