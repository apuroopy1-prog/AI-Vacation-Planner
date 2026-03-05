# trip planner CA
import os
from crewai import Agent, Task, Crew, Process

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "your_openai_api_key_here")

# Defining Agents

# Agent 1: The Expert Travel Agent
city_selector = Agent(
    role='Expert Travel Agent',
    goal='Select the best city for a vacation based on specific criteria.',
    backstory="""An experienced travel agent with a passion for
    discovering hidden gems and creating unforgettable travel
    experiences.""",
    verbose=True
)

# Agent 2: The Local Tour Guide
tour_guide = Agent(
    role='Local Tour Guide',
    goal='provide an amazing itinerary with the best local attractions and food spots.',
    backstory="""A knowledgeable local tour guide who knows thecity's secrets, from the best street food to the most stunning viewpoints.""",
    verbose=True
)

# Agent 3: The Travel Logistics Manager
logistics_manager = Agent(
    role='Travel Logistics Manager',
    goal='Find the best flights and accommodation for the trip.',
    backstory="""A meticulous planner who specializes in finding the most convenient and cost effective travel options.""",
    verbose=True
)   

#Defining Tasks

# Task 1: City Selection
city_selection_task = Task(
    description='Select the best city for a vacation based on user preferences.',
    expected_output='A detailed report on the selected city, including reasons for its selection based on user preferences.',
    agent=city_selector
)   

# Task 2: Itinerary Planning
itinerary_planning_task = Task(
    description='Create a detailed itinerary for the selected city, including must-see attractions and dining options.',
    expected_output='A day-by-day itinerary with descriptions of attractions and recommended dining spots.',
    agent=tour_guide,
    context=[city_selection_task]
)

# Task 3: Travel Logistics
travel_logistics_task = Task(
    description='Find the best flights and accommodation for the trip.',
    expected_output='A comprehensive list of flight options and accommodation recommendations, including prices and booking links.',
    agent=logistics_manager,
    context=[city_selection_task]
)

# Creating a Crew
crew = Crew(
    agents=[city_selector, tour_guide, logistics_manager],
    tasks=[city_selection_task, itinerary_planning_task, travel_logistics_task],
    process=Process.sequential,
    verbose=True
)

# Execute the Crew (using .kickoff() to get a result)
print("Starting the trip planning process...")
result = crew.kickoff()

# Print the final results
print("\n\n########################")
print("## Here is your complete vacation plan:")
print("########################\n")
print(result)
