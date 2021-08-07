SHELL := /bin/bash
.DEFAULT_GOAL := help

#######################
# HELPER TARGETS
#######################

.PHONY: help
help:  ## help target to show available commands with information
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) |  awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

#######################
# INSTALLATION
#######################

.PHONY: build
build: 
	docker-compose build

.PHONY: run
run: 
	docker-compose up
	
