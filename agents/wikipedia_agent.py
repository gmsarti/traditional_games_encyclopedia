import wikipedia
import spacy  # For NLP tasks

nlp = spacy.load("en_core_web_sm")  # Load a suitable NLP model

def wikipedia_search(game_name):
    try:
        game_info = wikipedia.summary(game_name, sentences=10)
        rules_section = extract_rules(game_info)
        return rules_section
    except wikipedia.exceptions.PageError:
        return "Game not found on Wikipedia."

def extract_rules(text):
    # Use NLP techniques to identify relevant rule sections
    doc = nlp(text)
    rules_sections = []
    for section in doc.sections:
        if any(word.lower() in section.text.lower() for word in ["rules", "gameplay", "how to play"]):
            rules_sections.append(section.text)
    return "\n".join(rules_sections)
