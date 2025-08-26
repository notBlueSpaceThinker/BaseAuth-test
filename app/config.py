from dataclasses import dataclass
from typing import Literal
from environs import Env


@dataclass
class Config:
    MODE: Literal["DEV", "PROD"]
    DOCS_USER: str
    DOCS_PASSWORD: str

def load_config(path: str = None) -> Config:
    env = Env()
    env.read_env(path)

    mode = env("MODE")
    if mode not in ("DEV", "PROD"):
        raise ValueError(f"Invalid MODE: {mode}")

    return Config(
        MODE=mode,
        DOCS_USER=env("DOCS_USER"),
        DOCS_PASSWORD=env("DOCS_PASSWORD")
    )