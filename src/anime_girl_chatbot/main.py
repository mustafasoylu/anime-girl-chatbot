"""Main module for the chatbot service."""

from anime_girl_chatbot.service import ChatbotService


def main():
    """Run the chatbot service."""
    chatbot_service = ChatbotService()
    chatbot_service.run()


if __name__ == "__main__":
    """Run the chatbot service."""
    main()
