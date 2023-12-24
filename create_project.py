import os

def create_project_structure():
    os.makedirs("agents", exist_ok=True)
    os.makedirs("dialogue_management", exist_ok=True)
    os.makedirs("resources", exist_ok=True)
    os.makedirs("resources/data", exist_ok=True)
    os.makedirs("resources/templates", exist_ok=True)
    os.makedirs("tests", exist_ok=True)

    with open("requirements.txt", "w") as f:
        f.write("rasa\n")
        f.write("wikipedia\n")
        f.write("requests\n")
        # Add other required libraries

if __name__ == "__main__":
    create_project_structure()
