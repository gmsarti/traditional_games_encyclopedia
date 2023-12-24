import pytest
from agents.duckduckgo_agent import duckduckgo_search

def test_duckduckgo_search_success():
    rules = duckduckgo_search("Monopoly")
    assert "properties" in rules.lower()  # Assert basic content

def test_duckduckgo_search_no_results():
    rules = duckduckgo_search("Unknown Game")
    assert rules == "No relevant information found on DuckDuckGo."

def test_duckduckgo_search_api_error():
    with pytest.raises(requests.exceptions.RequestException):
        duckduckgo_search("Invalid Request")
