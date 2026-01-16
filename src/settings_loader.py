from src.app_error import AppError
from src.settings import Settings


class SettingsLoader:
    def __init__(self, env):
        self.env = env

    def load(self):
        bridge_ip = self._required("HUE_BRIDGE_IP")
        username = self._optional("HUE_USERNAME")
        action = (self.env.get("HUE_ACTION") or "toggle").strip().lower()

        light_name = self._optional("HUE_LIGHT_NAME")
        group_name = self._optional("HUE_GROUP_NAME")
        brightness = self._brightness(self._optional("HUE_BRI"))

        if action != "register" and not (light_name or group_name):
            raise AppError("Set HUE_LIGHT_NAME or HUE_GROUP_NAME.")

        if light_name and group_name:
            raise AppError("Set only one: HUE_LIGHT_NAME or HUE_GROUP_NAME.")

        return Settings(bridge_ip, username, action, light_name, group_name, brightness)

    def _required(self, key):
        val = self._optional(key)
        if not val:
            raise AppError(f"Missing required env var: {key}")
        return val

    def _optional(self, key):
        val = self.env.get(key)
        if not val:
            return None
        val = val.strip()
        return val or None

    def _brightness(self, raw):
        if raw is None:
            return None
        try:
            value = int(raw)
        except ValueError:
            raise AppError("HUE_BRI must be an integer 1..254.")
        if not 1 <= value <= 254:
            raise AppError("HUE_BRI must be in range 1..254.")
        return value
