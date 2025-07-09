# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

OpenMemory is a personal memory layer for LLMs that allows users to store and retrieve memories while maintaining local control. The project consists of:

- **Backend API** (`api/`): FastAPI application with MCP (Model Context Protocol) server
- **Frontend UI** (`ui/`): Next.js React application for memory management
- **Database**: PostgreSQL with SQLAlchemy ORM and Alembic migrations
- **Vector Store**: Qdrant for semantic search capabilities

## Common Development Commands

### Environment Setup
```bash
# Copy environment files
make env

# Set environment variables manually
export OPENAI_API_KEY=sk-xxx
export USER=your_user_id
```

### Docker Development (Primary)
```bash
# Build and start all services
make build
make up

# Stop services and clean up
make down

# View logs
make logs

# Access API container shell
make shell

# Run database migrations
make migrate
```

### Frontend Development
```bash
# Install dependencies and run in development mode
make ui-dev

# Or run manually
cd ui
pnpm install
pnpm dev
pnpm build
pnpm start
pnpm lint
```

### Backend Development
```bash
# Install dependencies
cd api
pip install -r requirements.txt

# Run tests
pytest
pytest-cov

# Run server manually
uvicorn main:app --host 0.0.0.0 --port 8765 --reload
```

### Database Management
```bash
# Run migrations
make migrate
# or
make upgrade

# Rollback migration
make downgrade
```

## Architecture Overview

### Backend (`api/`)
- **FastAPI Application**: Main API server with CORS middleware
- **MCP Server**: Model Context Protocol server for memory operations
- **Memory Client**: Integration with Mem0 library for memory management
- **Database Models**: SQLAlchemy models for Users, Apps, Memories, Categories, etc.
- **Vector Store**: Qdrant integration for semantic search

### Key Components:
- `main.py`: FastAPI app initialization and router setup
- `app/mcp_server.py`: MCP server implementation with memory tools
- `app/models.py`: Database models and relationships
- `app/utils/memory.py`: Memory client configuration and Docker support
- `app/routers/`: API endpoints for memories, apps, stats, config

### Frontend (`ui/`)
- **Next.js Application**: React-based frontend with TypeScript
- **Redux Store**: State management for memories, apps, filters, UI
- **Tailwind CSS**: Styling with shadcn/ui components
- **React Components**: Memory management, app configuration, stats dashboard

### Key Components:
- `app/layout.tsx`: Root layout with theme provider
- `store/`: Redux slices for state management
- `components/`: Reusable UI components
- `hooks/`: Custom React hooks for API calls

## Environment Variables

### API (`.env` in `api/`)
```env
OPENAI_API_KEY=sk-xxx
USER=your_user_id
```

### UI (`.env` in `ui/`)
```env
NEXT_PUBLIC_API_URL=http://localhost:8765
NEXT_PUBLIC_USER_ID=your_user_id
```

## Database Schema

### Core Models:
- **User**: User management with unique user_id
- **App**: Applications that can access memories
- **Memory**: Individual memory records with vector embeddings
- **Category**: Auto-categorization of memories
- **AccessControl**: Permission management for memory access
- **MemoryAccessLog**: Audit trail for memory access

### Key Relationships:
- Users have many Apps and Memories
- Apps have many Memories (scoped to user)
- Memories belong to Users and Apps
- Categories are associated with Memories via junction table

## MCP Server Integration

The MCP server provides tools for:
- `add_memories`: Store new memories with metadata
- `search_memory`: Semantic search through stored memories
- `list_memories`: List all accessible memories
- `delete_all_memories`: Remove all memories for a user/app

### MCP Client Setup:
```bash
npx @openmemory/install local http://localhost:8765/mcp/<client-name>/sse/<user-id> --client <client-name>
```

## Memory Configuration

Memory client supports multiple providers:
- **LLM**: OpenAI (default), Ollama, Anthropic
- **Embeddings**: OpenAI (default), Ollama
- **Vector Store**: Qdrant (default)

Docker environment automatically adjusts localhost URLs for Ollama integration.

## Testing

### API Tests:
```bash
cd api
pytest
pytest-cov
```

### Frontend Tests:
```bash
cd ui
# No explicit test command configured
```

## Development Notes

- Memory client initialization is lazy and handles graceful failures
- Docker environment detection automatically adjusts Ollama URLs
- Database migrations use Alembic for schema management
- Access control and audit logging track memory usage
- Memory categorization happens automatically via OpenAI integration
- Frontend uses pnpm for package management
- UI state management through Redux with proper TypeScript types

## Port Configuration

- API Server: `localhost:8765`
- UI Development: `localhost:3090`
- Qdrant Vector Store: `localhost:6333`
- PostgreSQL: Internal Docker network

## Deployment

The project uses Docker Compose for deployment with:
- Multi-container setup (API, UI, Qdrant)
- Volume persistence for vector store
- Environment variable configuration
- Auto-reload for development