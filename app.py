import streamlit as st
import os
from dotenv import load_dotenv
import yaml
import textwrap
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, WebsiteSearchTool
from pydantic import BaseModel, Field
from typing import List
import warnings
warnings.filterwarnings('ignore')

# Load environment variables from .env file
load_dotenv()

# Set API keys from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")
serper_api_key = os.getenv("SERPER_API_KEY")

# Use the API keys in the necessary places (e.g., for CrewAI or other imports)
os.environ["OPENAI_API_KEY"] = openai_api_key
os.environ["SERPER_API_KEY"] = serper_api_key

# Custom CSS for styling
st.markdown("""
    <style>
        .main-title { font-size: 32px; color: #4e8cd9; font-weight: bold; }
        .subheader { font-size: 20px; font-weight: bold; color: #31333f; }
        .post-card { background-color: #f9f9f9; padding: 15px; border-radius: 8px; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); }
        .post-content { font-size: 16px; line-height: 1.5; }
        .sidebar { background-color: #f0f2f6; padding: 20px; border-radius: 8px; }
    </style>
""", unsafe_allow_html=True)

# Define Structured Output
class SocialMediaPost(BaseModel):
    platform: str = Field(..., description="Social media platform for the post")
    content: str = Field(..., description="Content of the social media post")

class ContentOutput(BaseModel):
    article: str = Field(..., description="Article content formatted in markdown")
    social_media_posts: List[SocialMediaPost] = Field(..., description="List of social media posts related to the article")

# Load Task and Agent configurations
files = {
    'agents': 'config/agents.yaml',
    'tasks': 'config/tasks.yaml'
}

configs = {}
for config_type, file_path in files.items():
    with open(file_path, 'r') as file:
        configs[config_type] = yaml.safe_load(file)

agents_config = configs['agents']
tasks_config = configs['tasks']

# Set up agents
global_research_analyst_agent = Agent(
    config=agents_config['global_research_analyst_agent'],
    tools=[SerperDevTool(), ScrapeWebsiteTool()]
)
data_insights_agent = Agent(
    config=agents_config['data_insights_agent'],
    tools=[SerperDevTool(), WebsiteSearchTool()]
)
content_director_agent = Agent(
    config=agents_config['content_director_agent'],
    tools=[SerperDevTool(), WebsiteSearchTool()]
)
content_quality_agent = Agent(
    config=agents_config['content_quality_agent']
)

# Set up tasks
monitor_global_news_task = Task(
    config=tasks_config['monitor_global_news'],
    agent=global_research_analyst_agent
)
analyze_global_data_task = Task(
    config=tasks_config['analyze_global_data'],
    agent=data_insights_agent
)
create_engaging_content_task = Task(
    config=tasks_config['create_engaging_content'],
    agent=content_director_agent,
    context=[monitor_global_news_task, analyze_global_data_task]
)
content_quality_review_task = Task(
    config=tasks_config['content_quality_review'],
    agent=content_quality_agent,
    output_pydantic=ContentOutput
)

# Create the crew
content_creation_crew = Crew(
    agents=[global_research_analyst_agent, data_insights_agent, content_director_agent, content_quality_agent],
    tasks=[monitor_global_news_task, analyze_global_data_task, create_engaging_content_task, content_quality_review_task],
    verbose=True
)

# Streamlit interface with sidebar and custom styling
st.sidebar.markdown("<div class='sidebar'><h3>Generate Content</h3>", unsafe_allow_html=True)
topic = st.sidebar.text_input("💡 Enter a topic for content generation")
generate_button = st.sidebar.button("🚀 Generate Content")

st.markdown("<div class='main-title'>AI-Powered Content Generator 🌟</div>", unsafe_allow_html=True)
st.write("Welcome! Generate engaging social media posts and articles by simply entering a topic in the sidebar.")

if generate_button and topic:
    with st.spinner("Generating content... please wait ⏳"):
        # Run the content creation pipeline
        result = content_creation_crew.kickoff(inputs={'subject': topic})
        
        # Display social media posts
        st.markdown("<div class='subheader'>Generated Social Media Posts 📱</div>", unsafe_allow_html=True)
        posts = result.pydantic.dict().get('social_media_posts', [])
        for post in posts:
            platform = post['platform']
            content = post['content']
            st.markdown(f"<div class='post-card'><b>Platform:</b> {platform}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='post-content'>{textwrap.fill(content, width=70)}</div>", unsafe_allow_html=True)
            st.write("-" * 50)
        
        # Display the article
        st.markdown("<div class='subheader'>Generated Article 📰</div>", unsafe_allow_html=True)
        article_content = result.pydantic.dict().get('article', "No article content available.")
        st.markdown(article_content)
else:
    if not topic:
        st.sidebar.warning("Please enter a topic to generate content.")
