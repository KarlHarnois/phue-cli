SERVICE = phue
DC = docker compose

.PHONY: build register run on off toggle shell console

build:
	$(DC) build

register:
	$(DC) run --rm -e HUE_ACTION=register $(SERVICE)

on:
	$(DC) run --rm -e HUE_ACTION=on $(SERVICE)

off:
	$(DC) run --rm -e HUE_ACTION=off $(SERVICE)

toggle:
	$(DC) run --rm -e HUE_ACTION=toggle $(SERVICE)

shell:
	$(DC) run --rm -it --entrypoint sh $(SERVICE)

console:
	$(DC) run --rm -it --entrypoint python $(SERVICE) -i -c \
	"from phue import Bridge; import os; b = Bridge(os.environ['HUE_BRIDGE_IP'], username=os.environ['HUE_USERNAME'])"
