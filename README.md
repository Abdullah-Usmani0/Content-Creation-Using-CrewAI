# AI-Powered Content Generator

This project is an AI-driven content generation app built using Streamlit. It leverages **CrewAI** to automate the creation of social media posts and articles based on a given topic. The application organizes tasks across specialized agents, each responsible for a distinct part of the content generation pipeline, including web scraping and data analysis.

## Features

- **Topic-Based Content Generation**: Input a topic and generate social media posts and an article related to the topic.
- **Multi-Agent System**: Uses CrewAI to manage agents, each performing different tasks such as web scraping, data analysis, and content creation.
- **Interactive Web App**: Built with Streamlit for easy user interaction and display of generated content.

## Technologies Used

- **Streamlit**: Provides an interactive web interface for input and output.
- **CrewAI**: Manages agents and tasks, creating a coordinated workflow for content generation.
- **Agents and Tasks in CrewAI**: 
  - **Global Research Analyst Agent**: Collects relevant information by scraping the web for up-to-date content.
  - **Data Insights Agent**: Analyzes the collected data to identify key insights.
  - **Content Director Agent**: Uses insights to draft engaging social media posts and articles.
  - **Content Quality Agent**: Reviews and refines the output for coherence and quality.

## Project Structure

- **Agents Configuration**: Each agent has its configuration file, which specifies the tools they use, such as web scraping or data search APIs.
- **Task Management**: Tasks define the work that each agent will carry out. Tasks are executed sequentially or concurrently depending on the dependencies.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/AI-Powered-Content-Generator.git
   cd AI-Powered-Content-Generator
   ```

2. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:

   To keep API keys and sensitive information secure, use environment variables instead of directly embedding them in code. Store your keys in a `.env` file or set them directly in the operating system’s environment.

   Example `.env` file:
   ```
   OPENAI_API_KEY=your_openai_api_key
   SERPER_API_KEY=your_serper_api_key
   ```

   Then load the environment variables in your script using:
   ```python
   from dotenv import load_dotenv
   load_dotenv()
   ```

4. **Run the application**:
   ```bash
   streamlit run app.py
   ```

## Usage

1. **Enter a Topic**: Enter a topic in the sidebar input field.
2. **Generate Content**: Click the "Generate Content" button to initiate the multi-agent pipeline.
3. **View Output**: The app displays generated social media posts and an article based on the provided topic.
