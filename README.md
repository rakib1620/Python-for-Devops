# Python for DevOps

Regular, hands-on Python practice aimed at DevOps engineering — automation, log analysis, file handling, system checks, and scripting tasks that come up in real DevOps work.

This repo is a learning log, not a polished project. Each script focuses on one practical problem, written while learning the underlying Python concept (loops, conditions, functions, file handling, etc.) through a DevOps-relevant lens instead of abstract puzzles.

## Why this repo exists

- Build solid Python fundamentals while staying motivated by practical, job-relevant context
- Create a visible, consistent record of practice (commit history = progress log)
- Lay groundwork for future scripting/automation work, and eventually AI/LLM-related Python work

## Structure

```
Python-for-Devops/
├── README.md
├── logs/              # Log parsing & analysis scripts
├── files/             # File handling & system checks
├── servers/            # Server/status data handling (lists, dicts)
└── automation/         # Small automation/utility scripts
```

Each script is self-contained with a short docstring at the top explaining what it practices — open any file to understand its purpose, no separate index needed.

## Topics covered (growing over time)

- **Loops & Conditions** — `for`, `while`, filtering data based on rules
- **Functions** — parameters, return values, writing reusable logic
- **Strings** — searching, matching keywords (e.g. finding "ERROR" in log lines)
- **Lists & Dictionaries** — filtering, counting, looking up structured data (e.g. server status lists, config-style dicts)
- **File Handling** — reading log/config files, checking if files/paths exist
- **Basic OOP** — organizing related logic into classes (e.g. a simple log parser)

## Example use cases practiced here

| Area | Example problem |
|---|---|
| Logs | Find and count lines in a log file containing `ERROR` or `FAILED` |
| Files | Check if a file/directory exists; create it if missing |
| Servers | Loop through a list of servers and flag the ones marked "down" |
| Automation | Small reusable functions for repetitive checks (e.g. status validation) |

## Workflow

- One problem → one file, named after what it does (e.g. `log_error_finder.py`, not `practice1.py`)
- Commits go straight to `main` — solo practice, no branching overhead
- ~1 hour of practice daily: learn a small concept, solve a related problem, commit

## Roadmap

- [x] Loops, conditions, functions — fundamentals
- [ ] Lists & dictionaries — data handling
- [ ] File handling — reading logs/configs
- [ ] Basic OOP — structuring scripts properly
- [ ] Small end-to-end script (e.g. a basic log analyzer tool)

---
*Learning Python by solving the kind of small problems DevOps work actually involves.*