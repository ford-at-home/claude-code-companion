# Claude Code Companion

The hands-on companion repository for the **Learn Claude** study guide — a
21-day, self-paced path for developers preparing to work effectively with
Claude Code, Anthropic's agentic coding tool.

> The app is the map; this repo is the territory.

Each day, you read the concepts in the study-guide app, then complete a
hands-on exercise **here**, in your own editor, with Claude Code running
alongside on your own machine.

## What's in this repo

```
modules/
└── day-01 … day-21/
    └── exercises/     the files you edit and complete
```

Each `exercises/` folder holds starter files — function stubs, worksheets, and
built-in structural checks. The concepts, instructions, and "what "done" looks
like" live in the app, not here. That separation is intentional.

## Getting started

1. **Install Claude Code** and sign in — see the official docs.
2. **Clone this repo** and open a day folder in your editor with Claude Code:
   ```bash
   git clone https://github.com/ford-at-home/claude-code-companion.git
   cd claude-code-companion/modules/day-01/exercises
   ```
3. **(Optional) Python + API key.** Most Python exercises run offline with
   structural checks only (look for `API Required: No` in the file header). A
   few call the Anthropic Messages API:
   ```bash
   python3 -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   cp .env.example .env   # then add your ANTHROPIC_API_KEY
   ```
4. **Work the exercise.** Starter `.py` files raise `NotImplementedError` where
   you write code. Run a file to check your structure:
   ```bash
   python3 modules/day-01/exercises/01-canonical-loop.py
   ```
   A completed exercise prints `All structural checks passed.`

## How it pairs with the app

Open the matching day in the study-guide app for the concepts and step-by-step
instructions, then come back here to do the work. Progress tracking and
end-of-module reflections live in the app; the code lives here.

Learn more at [learnclaude.app](https://learnclaude.app).

## License

Copyright © 2026 Ford Prior. All rights reserved. See [LICENSE](LICENSE).
