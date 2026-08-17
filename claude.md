# Project Voya: AI-Powered Life Map & Journal

## 1. Project Context
You are an expert full-stack developer and AI engineer assisting with "Voya". 
Voya (short for Voyage) is a location-based personal journaling application that remembers a user's life. It combines map-based memory tracking with AI-driven sentiment analysis, automatic tagging, and a RAG-based personal memory search engine.

## 2. Tech Stack
- **Frontend:** React, TypeScript, Tailwind CSS, React Router, Map library (e.g., Leaflet or Mapbox).
- **Backend:** Python, FastAPI, SQLAlchemy.
- **Database:** PostgreSQL with PostGIS (for spatial queries/location tracking).
- **AI / Search:** Vector Database (ChromaDB or FAISS), LangChain/LlamaIndex for RAG (Retrieval-Augmented Generation), OpenAI/Anthropic API for LLM features.

## 3. Core Principles & Code Style
- **TypeScript First:** Always use strict typing on the frontend. Define explicit interfaces for API responses and component props.
- **FastAPI Best Practices:** Use Pydantic models for request/response validation. Keep route handlers clean and delegate business logic to service layers.
- **Database:** Use SQLAlchemy ORM for relational data and GeoAlchemy2 for PostGIS spatial data.
- **Modularity:** Separate AI logic (embeddings, memory search) from basic CRUD operations.
- **Error Handling:** Implement global exception handlers in FastAPI and meaningful error states in React.

## 4. Key Entities
- **User:** Authentication and profile.
- **Location:** Lat/lng, spatial point (PostGIS), title, city.
- **JournalEntry:** Associated with a location, text content, date, AI-extracted mood, AI-extracted tags.

## 5. Instructions for AI Assistant
- When generating frontend code, ensure mobile-responsive design using Tailwind CSS.
- When writing backend queries involving locations, utilize PostGIS spatial functions (e.g., ST_Distance, ST_DWithin).
- For AI feature requests, prioritize the RAG architecture: embed the journal entry, store in vector DB, and retrieve context before generating answers.
- Explain technical decisions briefly, especially regarding PostgreSQL/PostGIS and vector embeddings, assuming the developers are 3rd-year computer engineering students.
