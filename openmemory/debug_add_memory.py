#!/usr/bin/env python3
"""
Debug script to test add_memories function directly
"""

import os
import sys
import json
import asyncio
import logging
from pathlib import Path

# Add the api directory to the path
sys.path.insert(0, str(Path(__file__).parent / "api"))

from app.mcp_server import add_memories, user_id_var, client_name_var
from app.utils.memory import get_memory_client

# Set up logging
logging.basicConfig(level=logging.INFO)

async def test_add_memory():
    """Test the add_memories function directly"""
    
    # Set context variables
    user_id = "bst"
    client_name = "test-client"
    
    # Set context vars
    user_id_var.set(user_id)
    client_name_var.set(client_name)
    
    print(f"Testing add_memories with user_id='{user_id}', client_name='{client_name}'")
    
    # Test memory client directly first
    print("\n1. Testing memory client initialization...")
    memory_client = get_memory_client()
    if memory_client:
        print("✓ Memory client initialized successfully")
    else:
        print("✗ Memory client failed to initialize")
        return
    
    # Test adding a memory
    print("\n2. Testing add_memories function...")
    test_text = "I love hiking in the mountains on weekends"
    
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
            else:
                print("⚠️  Result is not in expected format")
                
        except json.JSONDecodeError:
            print("Result is not valid JSON")
            
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_add_memory())