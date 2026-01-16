from src.app_error import AppError
from src.group_target import GroupTarget
from src.light_target import LightTarget


class TargetFactory:
    def create(self, settings):
        if settings.group_name:
            return GroupTarget(settings.group_name)
        if settings.light_name:
            return LightTarget(settings.light_name)
        raise AppError("No target configured.")
