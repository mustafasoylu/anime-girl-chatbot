from unittest.mock import patch

import pytest

from anime_girl_chatbot.config import ProjectConfig


def test_from_toml_file(create_toml_file):
    """Test that from_toml_file accepts a path to a toml file."""

    # case 1: file does not exist
    with pytest.raises(FileNotFoundError):
        ProjectConfig.from_toml_file("does_not_exist.toml")

    # case 2: file exists with proper data
    case2 = {
        "openai_api_key": "test",
        "openai_model": "gpt-4",
        "username": "test",
        "password": "test",
    }
    test_file = create_toml_file(case2)
    ProjectConfig.from_toml_file(test_file)

    # case 3: file exists with improper data, no api key
    case3 = {"openai_model": "gpt-4", "username": "test", "password": "test"}
    test_file = create_toml_file(case3)
    with pytest.raises(ValueError):
        ProjectConfig.from_toml_file(test_file)

    # case 4: file exists with improper data, wrong model name
    case4 = {
        "openai_api_key": "test",
        "openai_model": "gpt-5",
    }
    test_file = create_toml_file(case4)
    with pytest.raises(ValueError):
        ProjectConfig.from_toml_file(test_file)


@patch("anime_girl_chatbot.config.environ", {})
def test_from_env_case1():
    # case 1: empty environment variables
    with pytest.raises(ValueError):
        ProjectConfig.from_env()


@patch(
    "anime_girl_chatbot.config.environ",
    {
        "OPENAI_API_KEY": "test",
        "OPENAI_MODEL": "gpt-4",
        "USERNAME": "test",
        "PASSWORD": "test",
    },
)
def test_from_env_case2():
    # case 2: file exists with proper data
    ProjectConfig.from_env()


@patch(
    "anime_girl_chatbot.config.environ",
    {
        "OPENAI_MODEL": "gpt-4",
        "USERNAME": "test",
        "PASSWORD": "test",
    },
)
def test_from_env_case3():
    # case 3: file exists with improper data, no api key
    with pytest.raises(ValueError):
        ProjectConfig.from_env()


@patch(
    "anime_girl_chatbot.config.environ",
    {
        "OPENAI_API_KEY": "test",
        "OPENAI_MODEL": "gpt-5",
    },
)
def test_from_env_case4():
    # case 4: file exists with improper data, wrong model name
    with pytest.raises(ValueError):
        ProjectConfig.from_env()
