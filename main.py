from fastapi import FastAPI

app = FastAPI(
    title="DevDebug AI",
    description="AI-first debugging platform for finding, explaining, and fixing application issues.",
    version="0.1.0",
)

@app.get("/")
def read_root():
    """Root endpoint to verify the API is running."""
    return {"message": "Welcome to DevDebug AI"}

@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "ok"}
