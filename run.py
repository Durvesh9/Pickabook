import uvicorn
import os
from dotenv import load_dotenv

if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()
    
    # Check for API Key
    if not os.getenv("REPLICATE_API_TOKEN"):
        print("WARNING: REPLICATE_API_TOKEN is not set in environment variables.")
        print("Please create a .env file or export the variable before running.")

    print("Starting Pickabook Python Server...")
    print("Open http://localhost:8000 in your browser.")
    
    # Run the application
    # reload=True allows auto-restart on code changes (dev mode)
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)