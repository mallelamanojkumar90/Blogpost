from crewai import Agent
from crewai_tools import SerperDevTool

# Agent for analyzing the topic

def get_topic_analyzer_agent():
    return Agent(
        role="Topic Analyzer",
        goal="Analyze a given topic to identify key themes, potential angles, and target audience interests.",
        backstory=(
            "You are an expert content strategist specialized in breaking down complex topics "
            "into manageable and interesting components suitable for blog posts. "
            "You excel at identifying the core essence of a topic and suggesting creative approaches."
        ),
        verbose=True,
        allow_delegation=False,
        tools=[SerperDevTool()]
    )

# Agent for generating blog ideas

def get_idea_generator_agent():
    return Agent(
        role="Idea Generator",
        goal="Based on the topic analysis, brainstorm 5 distinct and engaging blog post titles/ideas.",
        backstory=(
            "You are a creative marketing specialist with a knack for generating catchy and relevant "
            "blog post ideas from strategic input. Your ideas are always fresh and target the identified audience effectively."
        ),
        verbose=True,
        allow_delegation=False
    )