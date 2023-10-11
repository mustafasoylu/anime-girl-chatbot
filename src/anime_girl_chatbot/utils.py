"""Utility functions for the project."""

from pathlib import Path

from anime_girl_chatbot.config import ProjectConfig


def load_config(config_path: Path = Path(".config.toml")) -> ProjectConfig:
    """Load the project configuration from a toml file or from environment variables."""
    if config_path.exists():
        return ProjectConfig.from_toml_file(config_path)
    else:
        return ProjectConfig.from_env()
