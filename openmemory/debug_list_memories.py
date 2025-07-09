#!/usr/bin/env python3
"""
Debug script to list existing memories
"""

import os
import sys
import json
import asyncio
import logging
from pathlib import Path

# Add the api directory to the path
sys.path.insert(0, str(Path(__file__).parent / "api"))

from app.mcp_server import list_memories, user_id_var, client_name_var
from app.utils.memory import get_memory_client

# Set up logging
logging.basicConfig(level=logging.INFO)

async def test_list_memories():
    """Test the list_memories function directly"""
    
    # Set context variables
    user_id = "bst"
    client_name = "test-client"
    
    # Set context vars
    user_id_var.set(user_id)
    client_name_var.set(client_name)
    
    print(f"Testing list_memories with user_id='{user_id}', client_name='{client_name}'")
    
    # Test listing memories
    print("\n1. Testing list_memories function...")
    
    try:
        result = await list_memories()
        print(f"Result type: {type(result)}")
        
        # Parse the result if it's JSON
        try:
            result_json = json.loads(result)
            print(f"Number of memories: {len(result_json)}")
            
            for i, memory in enumerate(result_json):
                print(f"\nMemory {i+1}:")
                print(f"  ID: {memory.get('id')}")
                print(f"  Memory: {memory.get('memory')}")
                print(f"  Hash: {memory.get('hash')}")
                print(f"  Created: {memory.get('created_at')}")
                
        except json.JSONDecodeError:
            print("Result is not valid JSON")
            print(f"Raw result: {result}")
            
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_list_memories())