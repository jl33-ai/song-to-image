"""
Rough Project Stucture Plan
Project/
|-- gui/
|   |-- main_window.py
|-- api/
|   |-- genius_api.py
|   |-- generative_ai_api.py
|-- utils/
|   |-- lyrics_parser.py
|   |-- image_text_overlay.py
|-- main.py
|-- requirements.txt
"""

from ... import ...

if __name__ == "__main__":
    # Initialize your GUI and APIs
    window = MainWindow()
    genius_api = GeniusAPI(api_key="...")
    generative_ai_api = GenerativeAIAPI(api_key="...")
    
    # Start your GUI event loop
    window.run()