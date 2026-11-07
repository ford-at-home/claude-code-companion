# Week 2 Integration Exercise: Monorepo Setup

## The Scenario

You've joined a new team that's starting a greenfield project — a claims processing platform. The monorepo has three domains:

```
claims-platform/
├── frontend/          # React + TypeScript, Vite build
│   ├── src/
│   │   ├── components/
│   │   ├── hooks/
│   │   └── pages/
│   └── tests/
├── backend/           # Python + FastAPI
│   ├── api/
│   │   ├── routes/
│   │   ├── models/
│   │   └── services/
│   └── tests/
├── infra/             # Terraform + AWS
│   ├── modules/
│   └── environments/
├── .github/
│   └── workflows/
└── .claude/
    ├── CLAUDE.md
    ├── rules/
    └── commands/
```

The team has agreed on these conventions:

**All code:**
- Every PR must have tests
- No hardcoded secrets — use environment variables
- Commit messages follow conventional commits (feat:, fix:, chore:, etc.)

**Frontend (React/TypeScript):**
- Use functional components with hooks (no class components)
- All components must have TypeScript props interfaces
- Use React Query for data fetching, not raw useEffect
- Test with Vitest + React Testing Library

**Backend (Python/FastAPI):**
- All endpoints must validate input with Pydantic models
- Return consistent error shapes: `{"error": str, "code": int, "detail": str | null}`
- Use dependency injection for database connections
- Test with pytest + httpx

**Infrastructure (Terraform):**
- All resources must be tagged with `team`, `environment`, and `cost-center`
- No hardcoded AMI IDs — use data sources
- Modules must have `variables.tf`, `outputs.tf`, and `README.md`

## Your Tasks

Complete these three exercises **in order**:

### 1. `claude_config.md` — Design the CLAUDE.md Hierarchy
Design the full configuration hierarchy: root CLAUDE.md, domain-specific rules in `.claude/rules/`, and explain what goes where and why.

### 2. `ci_pipeline.py` — Build the CI Command
Write a function that generates the correct `claude -p` command for automated PR review in CI, with proper flags for structured output, tool scoping, and safety.

### 3. `prompt_template.py` — Write the Review Prompt
Write the actual prompt that the CI pipeline feeds to Claude, with explicit review criteria and few-shot severity examples.

## How They Connect

```
claude_config.md          ci_pipeline.py          prompt_template.py
(what Claude knows)  →  (how Claude runs)   →  (what Claude does)
```

The configuration hierarchy ensures Claude has the right conventions loaded for each domain. The CI pipeline runs Claude in headless mode with proper guardrails. The prompt template tells Claude exactly what to look for and how to classify findings.
