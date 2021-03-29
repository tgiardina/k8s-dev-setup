.PHONY: build
build:
	docker build -t k8_demo/app:v0.1 ./app
	docker build -t k8_demo/api:v0.1 ./api

.PHONY: start
start:
	minikube start
	skaffold dev
