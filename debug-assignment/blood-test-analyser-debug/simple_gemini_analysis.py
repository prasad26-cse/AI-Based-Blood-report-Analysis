#!/usr/bin/env python3
"""
Simple test script for direct Gemini API calls
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai

def test_simple_gemini():
    """Test simple Gemini API call"""
    print("🧪 Testing Simple Gemini API Call...")
    
    # Load environment variables
    load_dotenv()
    
    # Get API key
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        api_key = "AIzaSyA1Dtd982x-3ZYKxfjXGrB-DvHkTqcl940"
        print("Using provided Gemini API key.")
    
    try:
        # Configure Gemini with API key
        genai.configure(api_key=api_key)
        
        # Create model
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Simple test
        response = model.generate_content("Hello! Please respond with 'Gemini is working correctly!'")
        
        print("✅ Simple Gemini test successful!")
        print(f"Response: {response.text}")
        return True
        
    except Exception as e:
        print(f"❌ Error in simple Gemini test: {e}")
        return False

if __name__ == "__main__":
    print("=" * 50)
    test_simple_gemini()
    print("=" * 50) 