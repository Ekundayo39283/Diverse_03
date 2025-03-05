import os
from google import genai
from prompts import calendar_agent_system_prompt, main_agent_system_prompt
from calendar_tools import list_calendar_list, list_calendar_events, create_calendar_list, insert_calendar_event
from swarm import Agent
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

api_key = os.getenv('GEMINI_API_KEY')

client = genai.Client(api_key=api_key)
model_name = "gemini-2.0-flash"  # Use the model name as a string

def transfer_to_main_agent():
    return main_agent

def transfer_to_calendar_agent():
    return calendar_agent

main_agent = Agent(
    name='Main_agent',
    model=model_name,  # Pass the model name as a string
    instructions=main_agent_system_prompt,
    functions=[transfer_to_calendar_agent]
)

calendar_agent = Agent(
    name='Calendar_agent',
    model=model_name,  # Pass the model name as a string
    instructions=calendar_agent_system_prompt,
    functions=[transfer_to_main_agent]
)

calendar_agent.functions.extend([list_calendar_list, list_calendar_events, create_calendar_list, insert_calendar_event])