# main.py

import os
import sys
from dotenv import load_dotenv
from crewai_tools import SerperDevTool
from agents import get_topic_analyzer_agent, get_idea_generator_agent
from tasks import get_analyze_topic_task, get_generate_ideas_task
from crew_setup import get_blog_post_ideas_crew

# Load environment variables from .env file
load_dotenv()

# Define Agents
topic_analyzer_agent = get_topic_analyzer_agent()
idea_generator_agent = get_idea_generator_agent()

# Define Tasks
analyze_topic_task = get_analyze_topic_task(topic_analyzer_agent)
generate_ideas_task = get_generate_ideas_task(idea_generator_agent, analyze_topic_task)

# Instantiate the Crew
blog_post_ideas_crew = get_blog_post_ideas_crew(
    topic_analyzer_agent,
    idea_generator_agent,
    analyze_topic_task,
    generate_ideas_task
)

# Get topic from user input
if len(sys.argv) > 1:
    topic_for_analysis = " ".join(sys.argv[1:])
else:
    topic_for_analysis = input("Enter the topic to analyze: ")

# Kick off the crew process
print("## Starting the Blog Post Idea Generation Process")
result = blog_post_ideas_crew.kickoff(inputs={'topic': topic_for_analysis})

# Print the final result
print("## Generated Blog Post Ideas:")
print(result)