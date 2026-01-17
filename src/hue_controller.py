from phue import Bridge


class HueController:
    def __init__(self, target_factory, action_router):
        self.target_factory = target_factory
        self.action_router = action_router

    def execute(self, settings):
        if settings.username:
            bridge = Bridge(settings.bridge_ip, username=settings.username)
        else:
            bridge = Bridge(settings.bridge_ip)

        action = self.action_router.resolve(settings.action)

        target = None

        if settings.action != "register":
            target = self.target_factory.create(settings)

        return action.run(bridge, target, settings.brightness)
