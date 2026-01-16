IMAGE = phue
RUN = docker run --rm --net=host --env-file .env

.PHONY: build register run on off toggle shell repl

build:
	docker build -t $(IMAGE) .

register:
	$(RUN) -e HUE_ACTION=register $(IMAGE)

run:
	$(RUN) $(IMAGE)

on:
	$(RUN) -e HUE_ACTION=on $(IMAGE)

off:
	$(RUN) -e HUE_ACTION=off $(IMAGE)

toggle:
	$(RUN) -e HUE_ACTION=toggle $(IMAGE)

shell:
	$(RUN) -it --entrypoint sh $(IMAGE)

console:
	$(RUN) -it --entrypoint python $(IMAGE) -i -c \
	"from phue import Bridge; import os; b = Bridge(os.environ['HUE_BRIDGE_IP'], username=os.environ['HUE_USERNAME'])"
