from src.app import App
from src.actions.action_router import ActionRouter
from src.env import Env
from src.hue_controller import HueController
from src.settings_loader import SettingsLoader
from src.target_factory import TargetFactory


def main():
    env = Env()
    loader = SettingsLoader(env)
    controller = HueController(TargetFactory(), ActionRouter())
    return App(loader, controller).run()


if __name__ == "__main__":
    raise SystemExit(main())
