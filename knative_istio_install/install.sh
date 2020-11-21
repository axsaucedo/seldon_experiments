curl -L https://istio.io/downloadIstio | ISTIO_VERSION=1.6.8 TARGET_ARCH=x86_64 sh -
istio-1.6.8/bin/istioctl install --set profile=demo
kubectl patch svc istio-ingressgateway -n istio-system --patch "$(cat ./istio-gateway-patch.yaml)"
