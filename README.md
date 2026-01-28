![License](https://img.shields.io/github/license/ifaakash/gh-prune)
![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)
![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Maintained](https://img.shields.io/badge/Maintained%3F-yes-green.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/ifaakash/gh-prune)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)
<!--![PyPi](https://img.shields.io/pypi/v/gh-prune)-->

                                       
  __ _| |__           _ __  _ __ _   _ _ __   ___ 
 / _` | '_ \   ____  | '_ \| '__| | | | '_ \ / _ \
| (_| | | | | |____| | |_) | |  | |_| | | | |  __/
 \__, |_| |_|        | .__/|_|   \__,_|_| |_|\___|
 |___/               |_|                          

       >> GitHub Workflow Cleaner <<

**gh-prune** is a command-line utility designed to help you manage and prune GitHub Actions workflow runs efficiently. It interacts with the GitHub CLI (`gh`) to list, inspect, and delete workflow runs, helping you maintain a clean repository and manage usage limits.

## Prerequisites

Before using `gh-prune`, ensure you have the following installed:

1.  **Python 3.x**
2.  **GitHub CLI (`gh`)**:
    *   macOS: `brew install gh`
    *   Windows/Linux: See [GitHub CLI Installation](https://cli.github.com/manual/installation)
3.  **Python Dependencies**:
    *   `typer`
    *   `rich`

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/ifaakash/gh-prune.git
    cd gh-prune
    ```

2.  Install dependencies:
    ```bash
    pip install typer rich
    ```

3.  Authenticate with GitHub:
    ```bash
    gh auth login --hostname github.com
    ```

## Build and Run Locally

To build and run the project locally, it is highly recommended to use a separate virtual environment (`venv`).

1.  **Create and Activate Virtual Environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2.  **Build and Install**:
    ```bash
    rm -rf dist/
    python3 -m build
    pip3 install dist/gh_prune-*.whl --force-reinstall
    ```

## Usage

The tool is executed via `doctor.py`. Below are the available commands.

### 1. Health Check (`doctor`)

Verifies that the GitHub CLI is installed and correctly authenticated.

```bash
python3 doctor.py doctor
```

### 2. List Workflows (`workflow-list`)

Lists all workflows in a specified repository, showing their names, IDs, and states.

**Syntax:**
```bash
python3 doctor.py workflow-list [OWNER/REPO]
```

**Example:**
```bash
python3 doctor.py workflow-list ifaakash/gh-prune
```

### 3. List Workflow Runs (`workflow-run-list`)

Lists the recent runs of a specific workflow file.

**Syntax:**
```bash
python3 doctor.py workflow-run-list [OWNER/REPO] [WORKFLOW_FILENAME]
```

**Example:**
```bash
python3 doctor.py workflow-run-list ifaakash/gh-prune pylint.yml
```

### 4. Delete Old Runs (`workflow-run-delete`)

Deletes old workflow runs but keeps a specified number of the most recent ones. Useful for cleaning up history while retaining the latest status.

**Syntax:**
```bash
python3 doctor.py workflow-run-delete [OWNER/REPO] [WORKFLOW_FILENAME] --keep [N] --limit [M]
```

**Options:**
*   `--keep`: Number of recent runs to keep (default: 5).
*   `--limit`: Number of runs to fetch for processing (default: 30).
*   `--yes` / `-y`: Skip confirmation prompt.

**Example:**
```bash
python3 doctor.py workflow-run-delete ifaakash/news-agent cron-workflow.yml --keep 180 --limit 200
```

### 5. Prune All Runs (`workflow-run-prune`)

Deleting **ALL** runs for a specific workflow up to a specified limit. **Use with caution.**

**Syntax:**
```bash
python3 doctor.py workflow-run-prune [OWNER/REPO] [WORKFLOW_FILENAME] --limit [M]
```

**Options:**
*   `--limit`: Number of runs to fetch and delete (default: 30).
*   `--yes` / `-y`: Skip confirmation prompt.

**Example:**
```bash
python3 doctor.py workflow-run-prune ifaakash/news-agent cron-workflow.yml --limit 200
```

## Help

To see a tabular summary of commands and examples directly in the terminal, run:

```bash
python3 doctor.py docs
```
