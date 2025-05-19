# Blog Post Idea Generator

This project uses CrewAI to generate blog post ideas based on a given topic. It leverages autonomous agents to analyze a topic and brainstorm engaging blog post titles.

## Features
- Analyze any topic for key themes, angles, and target audience interests
- Generate 5 unique and relevant blog post ideas for each topic
- Modular code structure for easy maintenance and extension

## Usage
1. **Install dependencies**
   ```powershell
   pip install -r requirements.txt
   ```
   (Make sure to include `python-dotenv`, `crewai`, and `crewai-tools` in your requirements.)

2. **Set up API keys**
   - Create a `.env` file in the project directory with the following content:
     ```env
     SERPER_API_KEY=your_serper_api_key
     OPENAI_API_KEY=your_openai_api_key
     # ANTHROPIC_API_KEY=your_anthropic_api_key (optional)
     ```

3. **Run the script**
   - Provide the topic as a command-line argument:
     ```powershell
     python main.py "Your topic here"
     ```
   - Or run without arguments and enter the topic interactively.

## Project Structure
- `main.py` - Entry point; loads environment, gets topic, and runs the crew
- `agents.py` - Agent definitions
- `tasks.py` - Task definitions
- `crew_setup.py` - Crew setup and orchestration

## Requirements
- Python 3.8+
- `crewai`
- `crewai-tools`
- `python-dotenv`

## License
MIT
