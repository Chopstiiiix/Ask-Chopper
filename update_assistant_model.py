#!/usr/bin/env python3
"""Update OpenAI Assistant to use a model that supports file_search"""

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
ASSISTANT_ID = os.environ.get("OPENAI_ASSISTANT_ID")
VECTOR_STORE_ID = os.environ.get("OPENAI_VECTOR_STORE_ID")

def update_assistant():
    """Update assistant to use gpt-4-turbo-preview which supports file_search"""

    print(f"Updating assistant: {ASSISTANT_ID}")
    print(f"Vector Store: {VECTOR_STORE_ID}")

    try:
        # Get current assistant configuration
        assistant = client.beta.assistants.retrieve(assistant_id=ASSISTANT_ID)
        print(f"\nCurrent configuration:")
        print(f"  Name: {assistant.name}")
        print(f"  Model: {assistant.model}")
        print(f"  Tools: {assistant.tools}")

        # Update to gpt-4-turbo (supports file_search)
        updated_assistant = client.beta.assistants.update(
            assistant_id=ASSISTANT_ID,
            model="gpt-4-turbo",  # Latest model supporting file_search
            tools=[{"type": "file_search"}],
            tool_resources={
                "file_search": {
                    "vector_store_ids": [VECTOR_STORE_ID]
                }
            }
        )

        print(f"\nUpdated configuration:")
        print(f"  Model: {updated_assistant.model}")
        print(f"  Tools: {updated_assistant.tools}")
        print(f"  Tool Resources: {updated_assistant.tool_resources}")
        print(f"\n✅ Assistant updated successfully!")

    except Exception as e:
        print(f"❌ Error updating assistant: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    update_assistant()
