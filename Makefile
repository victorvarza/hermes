.PHONY: default build run dry-run

IMAGE ?= qedzone/hermes

default: build

build:
	docker build -t $(IMAGE) .

push: build
	docker push $(IMAGE)

run:
	docker run -d 
	-v /mnt/monitor:/monitor 
	--name hermes $(IMAGE)