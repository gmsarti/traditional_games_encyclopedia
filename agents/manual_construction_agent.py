from jinja2 import Template  # For template-based formatting

def construct_manual(wikipedia_info, duckduckgo_info):
    template_file = "resources/templates/manual_template.md"
    with open(template_file, "r") as f:
        template = Template(f.read())
    manual_text = template.render(
        introduction=wikipedia_info["introduction"],
        setup=wikipedia_info["setup"],
        rules=combine_rules(wikipedia_info["rules"], duckduckgo_info)
    )
    return manual_text

def combine_rules(wikipedia_rules, duckduckgo_rules):
    # Combine rule information, prioritizing clarity and conciseness
    # Consider using NLP techniques for merging and summarization
    return f"{wikipedia_rules}\n\n{duckduckgo_rules}"
