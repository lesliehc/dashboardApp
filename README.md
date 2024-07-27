# Dynamic Interactive Python Dashboard using ChatGPT

This project demonstrates how to create a dynamic, interactive dashboard using Python and ChatGPT. The dashboard allows users to generate multiple charts and visualizations based on natural language queries, providing an intuitive interface for data exploration and analysis.

## Summary

The Dynamic Interactive Python Dashboard is a versatile tool designed to simplify data visualization and analysis. By leveraging the power of ChatGPT and Streamlit, users can interact with their data in a more natural and intuitive way. Whether you're a data analyst, a business professional, or someone with a keen interest in data visualization, this tool makes it easy to generate insightful visualizations with minimal effort.

## Features

- **Natural Language Querying**: Interact with the dashboard using plain English queries to generate visualizations.
- **Multiple Charts**: Display various types of visualizations (e.g., bar charts, line charts, scatter plots) simultaneously on the dashboard.
- **Real-time Data Interaction**: Update and interact with the dashboard in real-time based on user input.
- **Extensible**: Easily extend the functionality by adding more types of visualizations and custom queries.

## Use Cases

- **Business Intelligence**: Quickly generate visual reports for sales, marketing, and financial data to support decision-making processes.
- **Data Analysis**: Analyze trends and patterns in your data by creating multiple visualizations on the fly.
- **Educational Purposes**: Use the dashboard as a teaching tool to demonstrate data visualization techniques and concepts.
- **Personal Projects**: Apply the tool to personal datasets to gain insights and improve data storytelling.

## Examples

- Importing a CSV file, choose a chart, and ask the chat box what kind of dashboard they want.

## Running the Streamlit Dashboard Application

This guide provides detailed instructions on how to set up and run the `dashboardOperator.py` Streamlit application, which utilizes the OpenAI API. It is essential to ensure that the `OPENAI_API_KEY` environment variable is set before running the application.

### Requirements

- Python 3.6 or higher
- Streamlit
- OpenAI Python client
- pandas

### Installation

Install the necessary Python libraries using pip:

```bash
pip install streamlit openai pandas
