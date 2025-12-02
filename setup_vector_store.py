#!/usr/bin/env python3
"""
Setup script for OpenAI Vector Store
Creates a vector store for Ask Chopper document RAG system
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def create_vector_store():
    """Create a new vector store for Ask Chopper"""
    try:
        print("Creating vector store for Ask Chopper...")

        vector_store = client.vector_stores.create(
            name="Ask Chopper Documents",
            expires_after={
                "anchor": "last_active_at",
                "days": 30  # Auto-delete after 30 days of inactivity
            },
            metadata={
                "environment": "production",
                "application": "ask_chopper",
                "created_by": "setup_script"
            }
        )

        print(f"✅ Vector Store created successfully!")
        print(f"   ID: {vector_store.id}")
        print(f"   Name: {vector_store.name}")
        print(f"   Status: {vector_store.status}")
        print(f"   Expires after: 30 days of inactivity")
        print()
        print("📝 Add this to your .env file:")
        print(f"   OPENAI_VECTOR_STORE_ID={vector_store.id}")
        print()

        return vector_store

    except Exception as e:
        print(f"❌ Error creating vector store: {e}")
        return None

def configure_assistant(vector_store_id):
    """Configure existing assistant with file_search capability"""
    try:
        assistant_id = os.environ.get("OPENAI_ASSISTANT_ID")
        if not assistant_id:
            print("⚠️  OPENAI_ASSISTANT_ID not found in .env")
            print("   Skipping assistant configuration")
            return None

        print(f"Configuring assistant {assistant_id}...")

        # Update assistant with file_search tool
        assistant = client.beta.assistants.update(
            assistant_id=assistant_id,
            tools=[
                {"type": "file_search"}
            ],
            tool_resources={
                "file_search": {
                    "vector_store_ids": [vector_store_id]
                }
            }
        )

        print(f"✅ Assistant configured with file_search!")
        print(f"   Assistant ID: {assistant.id}")
        print(f"   Tools: {[tool.type for tool in assistant.tools]}")
        print(f"   Vector Store attached: {vector_store_id}")
        print()

        return assistant

    except Exception as e:
        print(f"❌ Error configuring assistant: {e}")
        return None

def main():
    print("=" * 60)
    print("Ask Chopper - Vector Store Setup")
    print("=" * 60)
    print()

    # Check API key
    if not os.environ.get("OPENAI_API_KEY"):
        print("❌ OPENAI_API_KEY not found in .env file")
        print("   Please add your OpenAI API key to .env")
        return

    # Create vector store
    vector_store = create_vector_store()
    if not vector_store:
        return

    # Configure assistant
    configure_assistant(vector_store.id)

    print("=" * 60)
    print("Setup Complete!")
    print("=" * 60)
    print()
    print("Next steps:")
    print("1. Add OPENAI_VECTOR_STORE_ID to your .env file")
    print("2. Run database migrations to add document_uploads table")
    print("3. Restart your Flask application")
    print()

if __name__ == "__main__":
    main()
