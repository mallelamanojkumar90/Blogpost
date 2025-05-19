from crewai import Crew, Process

def get_blog_post_ideas_crew(topic_analyzer_agent, idea_generator_agent, analyze_topic_task, generate_ideas_task):
    return Crew(
        agents=[topic_analyzer_agent, idea_generator_agent],
        tasks=[analyze_topic_task, generate_ideas_task],
        process=Process.sequential, # The tasks will be executed in the order defined
        verbose=True
    )
