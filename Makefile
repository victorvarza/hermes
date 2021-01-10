IMAGE = qedzone/hermes
ARCH = $(shell uname -m)
TAG = 1.0

build:
	docker build -t $(IMAGE):$(ARCH)-$(TAG) .

push: build
	docker push $(IMAGE)

dev.setup:
	[[ ! -d ./venv ]] && python3 -m venv venv
#	source ./venv/bin/activate
#	pip install -r requirements.txt	

dev.run: 
	docker run -d --name hermes \
		-v $(shell pwd)/monitor:/monitor \
		-v $(shell pwd)/app/conf:/app/conf \
		$(IMAGE):$(ARCH)-$(TAG)

dev.cleanup:
	docker rm -f hermes 