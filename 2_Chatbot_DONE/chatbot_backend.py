#1 import the OS, Bedrock, ConversationChain, ConversationBufferMemory Langchain Modules
import os
from langchain.llms.bedrock import Bedrock
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import boto3




def demo_chatbot():
    bedrock_client = boto3.Session(profile_name='sebas').client(
        service_name="bedrock-runtime",
        region_name="us-east-1"
    )
    modelID = "anthropic.claude-v2"
    demo_llm = Bedrock(
        client=bedrock_client,
        model_id=modelID,
        model_kwargs= {
            "max_tokens_to_sample": 300,
            "temperature": 0.1,
            "top_p": 0.9,
        }

    )
    return demo_llm



#3 Create a Function for ConversationBufferMemory (llm and max token limit)
def demo_memory():
    llm_data=demo_chatbot()
    memory = ConversationBufferMemory(llm=llm_data, max_token_limit= 512)
    return memory

#4 Create a Function for Conversation Chain - Input text + Memory
def demo_conversation(input_text,memory):
    llm_chain_data = demo_chatbot()

    llm_conversation= ConversationChain(llm=llm_chain_data,memory= memory,verbose=True)

#5 Chat response using Predict (Prompt template)
    chat_reply = llm_conversation.predict(input=input_text)
    return chat_reply
    