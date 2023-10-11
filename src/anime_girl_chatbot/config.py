"""Project configuration."""

from enum import Enum
from os import environ
from pathlib import Path
from typing import Optional

from pydantic import BaseModel, Field
from tomlkit import load


class OpenAIModel(str, Enum):
    """OpenAI chatbot models for fine-tuning."""

    GPT4 = "gpt-4"
    GPT35T = "gpt-3.5-turbo"
    DAVINCI = "davinci-002"
    BABBAGE = "babbage-002"


class ProjectConfig(BaseModel):
    """Project configuration."""

    openai_api_key: str = Field(..., description="OpenAI API key.")
    openai_model: OpenAIModel = Field(
        OpenAIModel.GPT35T, description="OpenAI model to use."
    )
    username: Optional[str] = Field(None, description="Username for the chatbot.")
    password: Optional[str] = Field(None, description="Password for the chatbot.")
    share: Optional[bool] = Field(
        False,
        description="Share the chatbot UI with outside, can be used for three days.",
    )

    @classmethod
    def from_env(cls):
        """Load config from environment variables."""
        return cls(
            openai_api_key=environ.get("OPENAI_API_KEY", None),
            openai_model=environ.get("OPENAI_MODEL", None),
            username=environ.get("USERNAME", None),
            password=environ.get("PASSWORD", None),
            share=environ.get("SHARE", None),
        )

    @classmethod
    def from_toml_file(cls, path: Path = Path("../../.config.toml")):
        """Load config from a TOML file, under project header."""
        with open(path) as f:
            config = load(f)
        return cls(**config["project"])
