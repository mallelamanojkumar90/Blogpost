from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
from agents import get_topic_analyzer_agent, get_idea_generator_agent
from tasks import get_analyze_topic_task, get_generate_ideas_task
from crew_setup import get_blog_post_ideas_crew

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

topic_analyzer_agent = get_topic_analyzer_agent()
idea_generator_agent = get_idea_generator_agent()
analyze_topic_task = get_analyze_topic_task(topic_analyzer_agent)
generate_ideas_task = get_generate_ideas_task(idea_generator_agent, analyze_topic_task)
blog_post_ideas_crew = get_blog_post_ideas_crew(
    topic_analyzer_agent,
    idea_generator_agent,
    analyze_topic_task,
    generate_ideas_task
)

@app.route('/', methods=['GET', 'POST'])
def index():
    ideas = None
    topic = ''
    if request.method == 'POST':
        topic = request.form.get('topic', '')
        if topic:
            result = blog_post_ideas_crew.kickoff(inputs={'topic': topic})
            # Try to extract points from result
            try:
                # If result is a string representation of a list, eval to list
                if isinstance(result, str) and result.strip().startswith('['):
                    ideas = eval(result)
                # If result is a string with numbered points, split into points
                elif isinstance(result, str) and any(s in result for s in ['1.', '2.', '3.', '4.', '5.']):
                    import re
                    ideas = re.findall(r'\d+\.\s*(.*?)(?=\n\d+\.|$)', result, re.DOTALL)
                    ideas = [i.strip().replace('\n', ' ') for i in ideas if i.strip()]
                else:
                    ideas = result
            except Exception:
                ideas = result
    return render_template('index.html', ideas=ideas, topic=topic)

if __name__ == '__main__':
    app.run(debug=True)
