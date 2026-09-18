# AI WordPress Builder

Build, audit, automate, and modernize WordPress websites with AI.

AI WordPress Builder is a generic framework for safe AI-assisted WordPress automation. It is designed for WordPress and Elementor workflows and supports local and remote LLM providers such as Ollama, OmniRouter, and OpenAI-compatible APIs.

## Goals

- Audit existing WordPress installations
- Inspect and work with Elementor structured data
- Extract and migrate content from source documents
- Plan website structures and page content with AI
- Generate controlled WordPress and Elementor changes
- Support local Ollama models and remote LLM routers
- Keep production changes reviewable, backed up, and verifiable
- Support multiple independent website projects

## Architecture

```
AI Agent
   |
   v
LLM Provider Layer
   |-- Ollama
   |-- OmniRouter
   |-- OpenAI-compatible APIs
   |
   v
WordPress Engine
   |-- WordPress REST API
   |-- Elementor data
   |
   v
Website
```

## Safety model

The framework is read-only by default.

Production writes should follow:

1. Discover
2. Audit
3. Backup
4. Plan
5. Review
6. Dry-run
7. Apply
8. Verify

Never commit credentials, application passwords, API keys, customer data, or site-specific production exports.

## Quick start

```bash
git clone https://github.com/multexpk-labs/ai-wordpress-builder.git
cd ai-wordpress-builder
chmod +x setup.sh audit.sh backup.sh inspect-elementor.sh
./setup.sh
```

Copy `.env.example` to `.env` and configure a WordPress API account and optional LLM provider.

## Project structure

```text
ai-wordpress-builder/
├── prompts/
├── scripts/
├── src/aiwp/
├── docs/
├── projects/
├── tests/
├── setup.sh
├── audit.sh
├── backup.sh
├── inspect-elementor.sh
├── .env.example
└── README.md
```

Site-specific implementations belong under `projects/<project-name>/` and should not be mixed into the generic core.

## Roadmap

- WordPress REST automation
- Elementor inspection and controlled editing
- Document/content extraction
- LLM abstraction
- Ollama integration
- OmniRouter integration
- AI content planning
- AI Elementor generation
- Human approval workflow
- Automated publishing and verification
- Multi-site project management
- Web-based builder UI

## License

MIT
