import os
import streamlit as st

# Get the OpenAI API key from Streamlit secrets
openapi_key = st.secrets["OPENAI_API_KEY"]

# Set the OpenAI API key as an environment variable
os.environ["OPENAI_API_KEY"] = openapi_key



def generate_restaurant_name_and_items(cuisine):
    
      from langchain.llms import OpenAI
      from langchain.prompts import PromptTemplate
      from langchain.chains import LLMChain, SequentialChain
      
      # Initialize the LLM
      llm = OpenAI(temperature=0.7)
      
      # Define the prompt template for generating restaurant names
      prompt_template_name = PromptTemplate(
          input_variables=["cuisine"],  # Corrected spelling
          template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this.",
      )
      
      # Create the LLMChain for generating restaurant names
      name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")
      
      # Define the prompt template for generating menu items
      prompt_template_items = PromptTemplate(
          input_variables=["restaurant_name"],
          template="Suggest some menu items for a restaurant named {restaurant_name}. Return it as a comma-separated list.",
      )
      
      # Create the LLMChain for generating menu items
      food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")
      
      # Create the SequentialChain
      chain = SequentialChain(
          chains=[name_chain, food_items_chain],
          input_variables=["cuisine"],  # Corrected spelling
          output_variables=["restaurant_name", "menu_items"],
      )
      
      # Run the chain
      output = chain({'cuisine': cuisine})
      return output

if __name__ == "__main__":
    print(generate_restaurant_name_and_items('Indian'))