import rasa
from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter
from agents.wikipedia_agent import wikipedia_search
from agents.duckduckgo_agent import duckduckgo_search
from agents.manual_construction_agent import construct_manual
from rasa.nlu.extractors.crf_entity_extractor import CRFEntityExtractor


# Load trained Rasa models
interpreter = RasaNLUInterpreter("models/nlu")
agent = Agent.load("models/dialogue")

def handle_user_message(message):
    user_intent = interpreter.parse(message)["intent"]["name"]
    if user_intent == "create_manual":
        game_name = extract_game_name(message)  # Implement game name extraction
        wikipedia_rules = wikipedia_search(game_name)
        duckduckgo_rules = duckduckgo_search(game_name)
        manual = construct_manual(wikipedia_rules, duckduckgo_rules)
        agent.handle_text(manual)  # Present manual to user or store
    else:
        agent.handle_text(message)  # Use Rasa for other conversational flows


def extract_game_name(message):
    entity_extractor = CRFEntityExtractor.load("models/nlu")  # Load trained model
    entities = entity_extractor.extract_entities(message)
    for entity in entities:
        if entity["entity"] == "game_name":
            return entity["value"]
    return None  # No game name found


# Start the Rasa interactive loop
if __name__ == "__main__":
    rasa.run(agent, handle_user_message)
