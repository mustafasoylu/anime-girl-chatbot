# anime-girl-chatbot

In this repo, we will create an anime girl imitator chatbot using ChatGPT and Python.


## インストール

First, create an OpenAI API key from the [OpenAI website](https://openai.com/blog/openai-api). If you haven't installed poetry yet, please install it.

```bash
pip install poetry
```

After cloning this repository, install the packages with poetry.

```bash
poetry install --with dev
```

## Project Configuration
The following information is required for project configuration:

- OpenAI API key (Required): Can be obtained from the [OpenAI website](https://openai.com/blog/openai-api).
- OpenAI model name (Optional): Please select from [the listed models](https://github.com/mustafasoylu/anime-girl-chatbot/blob/2982f0bb984452d3549d0aab3bd7e8c753a47265/src/anime_girl_chatbot/config.py#L12). The default is gpt-3.5-turbo.
- Username (Optional): Chatbot's username (Enter along with the password)
- Password (Optional): Chatbot's password (Enter along with the username)
- Share key (Optional): Set to true if you want to make it public. The default is false.

If you want external people to access the chatbot, you can set the share key to true. However, the link created by gradio can only be used for 3 days. Please refer to the [gradio documentation](https://www.gradio.app/guides/sharing-your-app) for details.

### Running on a Local Computer

When running on a local computer, create a .config.yaml file in the project root directory and fill it out as follows:

```toml
[project]
openai_api_key = "OpenAI API key"
openai_model = "Model name"
username = "Username"
password = "Password"
share = false
```

### When Deploying
When deploying, you can use the environment variables set in [config.py](https://github.com/mustafasoylu/anime-girl-chatbot/blob/2982f0bb984452d3549d0aab3bd7e8c753a47265/src/anime_girl_chatbot/config.py#L36).

## Using Locally

To use locally, run the following command:

```bash
poetry run chatbot
```

## Testing

To run tests, execute the following command:

```bash
poetry run pytest
```

