#!/usr/bin/env python3
"""
Debug script to test adding a unique memory
"""

import os
import sys
import json
import asyncio
import logging
from pathlib import Path
import uuid

# Add the api directory to the path
sys.path.insert(0, str(Path(__file__).parent / "api"))

from app.mcp_server import add_memories, user_id_var, client_name_var
from app.utils.memory import get_memory_client

# Set up logging
logging.basicConfig(level=logging.INFO)

async def test_unique_memory():
    """Test adding a unique memory"""
    
    # Set context variables
    user_id = "bst"
    client_name = "gemini-cli"  # Use the same client name as Gemini-CLI
    
    # Set context vars
    user_id_var.set(user_id)
    client_name_var.set(client_name)
    
    print(f"Testing add_memories with user_id='{user_id}', client_name='{client_name}'")
    
    # Test adding a completely unique memory
    print("\n1. Testing add_memories with unique content...")
    unique_id = str(uuid.uuid4())[:8]
    test_text = f"My favorite coffee shop is Bean There Done That on Main Street. They make excellent espresso and their wifi is super fast. I go there every Tuesday morning at 9:30 AM. Unique ID: {unique_id}"
    
    try:
        result = await add_memories(test_text)
        print(f"Result: {result}")
        
        # Parse the result if it's JSON
        try:
            result_json = json.loads(result)
            print(f"Parsed result: {json.dumps(result_json, indent=2)}")
            
            if isinstance(result_json, dict) and 'results' in result_json:
                if len(result_json['results']) == 0:
                    print("⚠️  WARNING: Results array is empty!")
                else:
                    print(f"✓ Successfully added {len(result_json['results'])} memory results")
                    for i, result_item in enumerate(result_json['results']):
                        print(f"  Result {i+1}: {result_item.get('event')} - {result_item.get('memory')}")
            else:
                print("⚠️  Result is not in expected format")
                
        except json.JSONDecodeError:
            print("Result is not valid JSON")
            
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_unique_memory())