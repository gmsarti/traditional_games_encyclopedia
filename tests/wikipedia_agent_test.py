import pytest
from agents.wikipedia_agent import wikipedia_search, extract_rules

def test_wikipedia_search_existing_game():
    rules = wikipedia_search("Chess")
    assert "board game" in rules.lower()  # Assert basic content

def test_wikipedia_search_nonexistent_game():
    with pytest.raises(wikipedia.exceptions.PageError):
        wikipedia_search("Fake Game")

def test_extract_rules():
    text = "This game has simple rules. Players take turns rolling dice."
    rules = extract_rules(text)
    assert "simple rules" in rules  # Assert relevant section extracted
