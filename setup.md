# Architecture

commit to repo -> cloud build -> container registry -> GKE Deployment -> GKE HPA -> GKE Service -> GKE Ingress

## commit to repo automatically triggers a build

- explain google cloud build
- explain creation of trigger. important things to explain here are
	- linking of github repo
	- trigger point (for us it was commit to master branch, but explain other options)
	- file it will use for build `cloudbuild.yaml`
	- service account that it would use
	- a bucket created to save cloud build logs

## google container registry

explain here the container registry you created and the URL for it

## cloudbuild.yaml file

- explain gcp cloud builders we use example docker, gke-deploy
- explain usage of $SHORT_SHA
- explain 3 steps we use
	1. docker build
	2. docker push
	3. gke deploy

## GKE

- explain the cluster you had setup of 3 machines

## GKE Deployment

- explain our depl.yaml file

## GKE HPA (Horizontal Pod Autoscaler)

- this is main part for your project
- explain how autoscaler works and what is horizontal autoscaling
- explain our hpa file, mainly
	- min replicas
	- max replicas
	- target cpu utilization

## GKE service

- explain what a NodePort service does
- our serv.yaml file mainly 
	- how its telling which pods it is enabling communication for
	- port and targetPort


## ingress

- explain need for ingress and our ingress file

### extra

1. create firestore secret: `kubectl create secret generic firestore-keys --from-file=firestorecredential.json=./adminsa.json`