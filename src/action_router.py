from src.app_error import AppError
from src.actions.on_off import OnOff
from src.actions.register import Register
from src.actions.toggle import Toggle


class ActionRouter:
    def resolve(self, action):
        if action == "register":
            return Register()

        if action == "toggle":
            return Toggle()

        if action == "on":
            return OnOff(True)

        if action == "off":
            return OnOff(False)

        raise AppError("HUE_ACTION must be on|off|toggle|register.")
