from crewai import Task

def get_analyze_topic_task(topic_analyzer_agent):
    return Task(
        description=(
            "Analyze the following topic: '{topic}'. "
            "Identify at least 3-5 key sub-themes or angles that could be explored. "
            "Also, consider the potential target audience and what aspects would appeal to them. "
            "Provide a concise summary of your analysis."
        ),
        expected_output="A summary of the topic analysis, including key themes, angles, and target audience considerations.",
        agent=topic_analyzer_agent
    )

def get_generate_ideas_task(idea_generator_agent, analyze_topic_task):
    return Task(
        description=(
            "Based on the topic analysis provided, generate a list of exactly 5 distinct, engaging, "
            "and relevant blog post titles or ideas. Each idea should be unique and directly related to the analysis. "
            "The output should be a Python list of 5 strings."
        ),
        expected_output="A Python list of 5 strings, each representing a unique blog post idea/title.",
        agent=idea_generator_agent,
        context=[analyze_topic_task] # This task depends on the output of the analyze_topic_task
    )
