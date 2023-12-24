import pytest
from main import handle_user_message, extract_game_name

def test_intent_recognition():
    message = "Can you create a manual for Monopoly?"
    intent = extract_game_name(message)
    assert intent == "create_manual"

def test_agent_calls():
    # ... Mock agent functions and test calls within handle_user_message (omitted for brevity)
    pass