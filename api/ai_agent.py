import os
import langchain
from tavily import TavilyClient
from ultralytics import YOLO
from langchain.agents import Tool, initialize_agent
from langchain_community.chat_models import ChatOpenAI
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.prompts import PromptTemplate, ChatPromptTemplate
import constants
import time
from dotenv import load_dotenv

load_dotenv()

model = YOLO("yolov8m.pt")

llm = ChatOpenAI(
    model_name="gpt-3.5-turbo", temperature=0.7, openai_api_key=os.getenv("OPEN_AI_API")
)


prompt_template = ChatPromptTemplate(
    [
        (
            "system",
            "You are a kid trying to figure out what different activity/game you can play any of the objects. The activity/game must be different. There needs to be an explanation on how to play the suggested games",
        ),
        (
            "user",
            """Give me 3 activity/game I can play with {topics}. They must involve at least one {topics}. Try your best not to have repeat games. In your response, PLEASE INCLUDE HOW TO PLAY THE GAMES SUGGESTED AND BE DETAILED!
            """,
        ),
    ]
)


def scrapeWeb(query):
    client = TavilyClient(api_key=os.getenv("TAVILY_API"))
    results = client.search(query=query)
    if results and "results" in results:
        return "\n".join([result["title"] for result in results["results"]])
    else:
        return "No results found."


tools = [
    Tool(
        name="Search Web", func=scrapeWeb, description="Use this tool to search the Web"
    )
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True,
    return_intermediate_steps=False,
)


def whatIsIt(image):
    results = model.predict(image)
    result = results[0]
    list_objects = []
    for i in range(len(result.boxes)):
        box = result.boxes[i]
        numIndex = int(box.cls.item())
        list_objects.append(constants.DICT_COCO[numIndex])
    return list_objects


def nameGames(nameImage):
    classif = whatIsIt(nameImage)
    prompt = prompt_template.format_prompt(topics=classif).to_messages()
    result = agent.run(prompt)
    print(result)
    return result
