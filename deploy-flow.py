from dotenv import load_dotenv
from mira_sdk.exceptions import FlowError
from mira_sdk import MiraClient,Flow
import os

load_dotenv()
api_key ='sb-d8a0e3d0fbafb3ff3c64d1872c3e0a34'

client = MiraClient(config={"API_KEY": api_key})

flow = Flow(source="flow.yaml")
try:
	client.flow.deploy(flow)
except FlowError as e:
	print(f"Error occured: {str(e)}")