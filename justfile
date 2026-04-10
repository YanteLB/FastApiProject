
#to run the main file
set windows-shell := ["pwsh", "-NoLogo", "-NoProfile", "-Command"]

# Run the main funtion 
runMain:
    @uv run main.py

# Run the uvicorn server for fastapi
runUvicorn:
    @.venv/Scripts/python.exe -m uvicorn main:app --reload