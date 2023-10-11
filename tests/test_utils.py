from pathlib import Path
from unittest.mock import MagicMock, patch

from anime_girl_chatbot.utils import load_config


@patch("anime_girl_chatbot.utils.ProjectConfig")
def test_load_config_file(mock_config, create_toml_file):
    """Config file exists and from_toml_file is called."""
    # create the file
    file_path = create_toml_file(
        {
            "openai_api_key": "test",
            "openai_model": "gpt-4",
            "username": "test",
            "password": "test",
        }
    )

    # create the mock
    mock_config.from_toml_file.return_value = MagicMock()

    # call the function
    load_config(file_path)

    mock_config.from_toml_file.assert_called_once_with(file_path)


@patch("anime_girl_chatbot.utils.ProjectConfig")
def test_load_config_env(mock_config):
    """Config file does not exist and from_env is called."""
    # set a non-existing file path
    file_path = Path("non-existing-file-path.toml")

    # create the mock
    mock_config.from_env.return_value = MagicMock()

    # call the function
    load_config(file_path)

    mock_config.from_env.assert_called_once()
