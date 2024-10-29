# AI-Powered Content Generator

This project is an AI-driven content creation tool designed to streamline the generation of social media posts and articles. By entering a topic, users can generate high-quality content in seconds, making it especially valuable for companies and content teams looking to automate and enhance their content production processes. This demo serves as a foundational base that can be extended for full-scale content creation across various industries.

## Features

- **Topic-Based Content Generation**: Enter a topic, and the tool generates relevant social media posts and a full-length article, suitable for immediate use.
- **Multi-Agent Workflow**: Uses CrewAI agents to research, analyze, and curate content by scraping and reviewing web data.
- **High-Quality Outputs**: Automatically optimized content for platforms like LinkedIn, Twitter, and more, helping brands maintain consistency across channels.
- **Customizable**: Easily expandable with new tasks and agents, making it adaptable to specific brand needs.

## Use Cases

This project can benefit:
- **Companies** looking for a reliable, scalable solution to generate timely and engaging content.
- **Social Media Managers** who need quick, relevant content ideas.
- **Marketing Teams** aiming to maintain a high content output without additional resources.

By leveraging AI, this project acts as a quick-start demo for companies to build on, ensuring rapid content generation without compromising on quality or brand voice.

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
   Create a `.env` file in the root of the project and add your API keys:
   ```plaintext
   OPENAI_API_KEY=your_openai_api_key
   SERPER_API_KEY=your_serper_api_key
   ```

4. **Run the application**:
   ```bash
   streamlit run app.py
   ```

## Technologies Used

- **Streamlit**: For building an interactive, user-friendly interface.
- **CrewAI**: Manages agents and tasks that simulate content production workflows.
- **OpenAI**: Powers the text generation and research analysis.
- **SerperDevTool and ScrapeWebsiteTool**: Used by agents to gather and process web data for content creation.

## How It Works

The app relies on a multi-agent setup using CrewAI to implement distinct roles:

1. **Research Analyst Agent**: 
   - Gathers relevant information by scraping the web based on the input topic. 
   - Utilizes tools like `SerperDevTool` to ensure the latest information is retrieved from various online sources.

2. **Data Insights Agent**: 
   - Analyzes the data collected to extract key insights and trends relevant to the topic. 
   - Provides context and data-driven support for content creation.

3. **Content Director Agent**: 
   - Creates engaging, topic-centered content from the insights gathered. 
   - Ensures that the generated content aligns with the target audience's needs and expectations.

4. **Quality Review Agent**: 
   - Refines the output to ensure high quality and relevance.
   - Conducts checks to maintain brand voice and optimize the content for various platforms.

Each agent operates collaboratively, leveraging their specific strengths to produce well-rounded content in a matter of seconds. The integration of web scraping allows for real-time data gathering, ensuring that the content generated is not only timely but also relevant.

## Usage

Enter your topic in the app’s sidebar, and it will automatically generate a series of social media posts and an article. The generated content is structured for readability and engagement, suitable for direct publishing or as a draft for further customization.

## Future Enhancements

This project is a foundation for automated content generation. Potential improvements could include:
- Additional agents for handling niche content topics.
- Enhanced quality checks for SEO optimization.
- Real-time feedback for refining the generated content.
