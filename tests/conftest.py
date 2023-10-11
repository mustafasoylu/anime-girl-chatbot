import pytest
from tomlkit import dumps


@pytest.fixture
def create_toml_file(tmp_path):
    """Create a toml file with given data and return path to it."""

    def create_toml_file_helper(data):
        """Helper function to create a toml file with given data."""
        # temporary path to save the file
        file_path = tmp_path / "config.toml"

        # our config is a dict with a single key "project"
        toml_dict = {"project": data}

        # convert toml_dict to a string and save it to file_path
        toml_str = dumps(toml_dict)
        with open(file_path, "w") as f:
            f.write(toml_str)

        # return the path to the file
        return file_path

    yield create_toml_file_helper
