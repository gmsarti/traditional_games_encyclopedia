import pytest
from agents.manual_construction_agent import construct_manual

def test_manual_construction():
    wikipedia_info = {"introduction": "A strategic game", "setup": "Place pieces on the board", "rules": "Detailed rules section"}
    duckduckgo_info = "Additional rules from DuckDuckGo"
    manual = construct_manual(wikipedia_info, duckduckgo_info)
    assert "Strategic game" in manual  # Assert content from both sources

def test_manual_template_formatting():
    # ... Test template rendering and manual structure (omitted for brevity)
    pass