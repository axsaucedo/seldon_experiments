
install:
	kubectl config use-context docker-for-desktop
	kubectl config set-context docker-for-desktop --namespace default
	helm install seldon-core-operator --repo https://storage.googleapis.com/seldon-charts --name seldon-core
	helm install stable/ambassador --name ambassador --set crds.keep=fals
	kubectl patch svc ambassador --type='json' -p '[{"op":"replace","path":"/spec/type","value":"NodePort"}]'

deploy:
	kubectl config use-context docker-for-desktop
	kubectl config set-context docker-for-desktop --namespace default
	kubectl apply -f seldon_deployment.json

reload:
	make build_images
	kubectl delete pod -l seldon-app=text-example-text-dep-text-pred

remove:
	kubectl delete -f seldon_deployment.json

build_images:
	cd step_one && ./build_image.sh
	cd step_two && ./build_image.sh
	cd step_three && ./build_image.sh

send_request: 
	curl -X POST -H 'Content-Type: application/json' \
		-d "{'data': {'names': ['get'], 'ndarray': ['data']}}" \
		http://localhost:32085/seldon/default/text-example/api/v0.1/predictions

