.PHONY: default build run dry-run

IMAGE ?= qedzone/hermes

default: build_arm64


build_arm64:
	docker build -t $(IMAGE):"arm64" .

push_arm64: build_arm64
	docker push $(IMAGE):"arm64"

run_arm64:
	docker run -d 
	-v /mnt/monitor:/monitor 
	--name hermes $(IMAGE):"arm64"

build:
	docker build -t $(IMAGE) .

push: build
	docker push $(IMAGE)

run:
	docker run -d 
	-v /mnt/monitor:/monitor 
	--name hermes $(IMAGE)