# Google Form Monitor

A lightweight Python application that monitors a Google Form using GitHub Actions and sends a Discord notification when the form becomes available.

After the first successful notification, the GitHub Actions workflow automatically disables itself to prevent duplicate alerts.

## Features

* Monitor a Google Form every 5 minutes
* Detect when a form changes from **closed** to **open**
* Send a Discord webhook notification
* Automatically disable the GitHub Actions workflow after the first notification
* Manual workflow trigger for testing

## Project Structure

```text
.
├── .github/
│   └── workflows/
│       └── monitor.yml
├── monitor.py
├── requirements.txt
└── README.md
```

## Requirements

* Python 3.12+
* requests

Install dependencies locally:

```bash
pip install -r requirements.txt
```

## Configuration

Create the following **Repository Secrets**:

| Secret            | Description                              |
| ----------------- | ---------------------------------------- |
| `GOOGLE_FORM_URL` | Google Form URL (`https://.../viewform`) |
| `DISCORD_WEBHOOK` | Discord Webhook URL                      |

## GitHub Actions

The workflow runs automatically every 5 minutes.

```yaml
schedule:
  - cron: "*/5 * * * *"
```

You can also run it manually from the **Actions** tab using **Run workflow**.

## Workflow Permissions

The workflow requires the following permissions:

```yaml
permissions:
  actions: write
  contents: read
```

These permissions allow the workflow to disable itself after sending the notification.

## Notification Flow

```text
GitHub Actions
        │
        ▼
Check Google Form
        │
 ┌──────┴──────┐
 │             │
Closed       Open
 │             │
Exit      Send Discord Notification
              │
              ▼
Disable Workflow
              │
              ▼
      No More Scheduled Runs
```

## Running Locally

```bash
python monitor.py
```

When running locally, set the required environment variables before execution.

## License

MIT