

kind_create_cluster:
	kind create cluster --config kind_config.yaml


install-istio:
	./install-istio.sh
	kubectl patch svc istio-ingressgateway -n istio-system --patch "$$(cat ./istio-gateway-patch.yaml)"


install-knative-serving:
	kubectl apply --filename https://github.com/knative/serving/releases/download/v0.18.0/serving-crds.yaml
	kubectl apply --filename https://github.com/knative/serving/releases/download/v0.18.0/serving-core.yaml
	kubectl apply --filename https://github.com/knative/net-istio/releases/download/v0.18.0/release.yaml

install-knative-serving-xip:
	kubectl apply --filename https://github.com/knative/serving/releases/download/v0.18.0/serving-default-domain.yaml

install-knative-eventing:
	kubectl apply --filename https://github.com/knative/eventing/releases/download/v0.18.0/eventing-crds.yaml
	kubectl apply --filename https://github.com/knative/eventing/releases/download/v0.18.0/eventing-core.yaml
	kubectl apply --filename https://github.com/knative/eventing/releases/download/v0.18.0/in-memory-channel.yaml
	kubectl apply --filename https://github.com/knative/eventing/releases/download/v0.18.0/mt-channel-broker.yaml


install-cert-manager:
	kubectl apply --validate=false -f https://github.com/jetstack/cert-manager/releases/download/v1.0.4/cert-manager.yaml


install-seldon:
	kubectl create ns seldon-system
	helm install seldon-core seldon-core-operator --repo https://storage.googleapis.com/seldon-charts --namespace seldon-system --set istio.enabled=true

