IMAGE = qedzone/hermes
TAG = 1.0

build:
	docker build -t $(IMAGE):$(TAG) .

push: build
	docker push $(IMAGE)

run:
	docker run -d 
	-v ./monitor:/monitor 
	--name hermes $(IMAGE)

dev.setup:
	[[ ! -d ./venv ]] && python3 -m venv venv
#	source ./venv/bin/activate
#	pip install -r requirements.txt	