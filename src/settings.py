from dataclasses import dataclass


@dataclass
class Settings:
    bridge_ip: str
    username: str | None
    action: str
    light_name: str | None
    group_name: str | None
    brightness: int | None
