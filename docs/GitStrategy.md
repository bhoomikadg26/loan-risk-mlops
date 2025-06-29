# Git Strategy: Git Flow

## Branches
- `main`: Production-ready code
- `develop`: Integration branch
- `feature/*`: Feature branches for tasks

## Workflow
1. Start from `develop` branch
2. Create: `git checkout -b feature/task-name`
3. Work, commit, push: `git push origin feature/task-name`
4. Pull request to `develop`

## Why Git Flow?
- Keeps production code stable
- Helps with collaboration
