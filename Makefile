SERVICE = phue
RUN = docker compose run --rm -e

.PHONY: build register run on off toggle shell console

build:
	docker compose build

register:
	$(RUN) HUE_ACTION=register $(SERVICE)

on:
	$(RUN) HUE_ACTION=on $(SERVICE)

off:
	$(RUN) HUE_ACTION=off $(SERVICE)

toggle:
	$(RUN) HUE_ACTION=toggle $(SERVICE)

shell:
	$(RUN) -it --entrypoint sh $(SERVICE)

console:
	$(RUN) -it --entrypoint python $(SERVICE) -i -c \
	"from phue import Bridge; import os; b = Bridge(os.environ['HUE_BRIDGE_IP'], username=os.environ['HUE_USERNAME'])"
