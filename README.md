# GitHub Webhook Receiver

## Summary
A Flask-based webhook receiver that captures GitHub repository events, stores them in MongoDB, and displays real-time repository activities through a polling-based dashboard.

---

# Overview

GitHub Webhook Receiver is a backend-focused application that listens to GitHub repository events and stores event information in MongoDB for further processing and visualization.

The project demonstrates:
- Webhook integration with GitHub
- Event-driven backend architecture
- MongoDB data storage
- REST API development
- Real-time event monitoring through polling

The application captures repository activities such as:
- Push events
- Pull request events
- Merge events

and displays them through a lightweight web interface that automatically refreshes every 15 seconds.

---

# Problem Statement

Development teams often need visibility into repository activities such as:
- Code pushes
- Pull requests
- Merge operations

Manually tracking these events is inefficient and does not scale.

This project solves that problem by:
- Automatically receiving GitHub webhook events
- Persisting event data in MongoDB
- Providing a dashboard for monitoring repository activity
- Updating activity feeds automatically through periodic polling

---

# Tools and Tech

## Backend
- Python
- Flask
- PyMongo

## Database
- MongoDB Atlas

## Frontend
- HTML
- JavaScript

## Integration
- GitHub Webhooks

---

# Methods

## Webhook Processing

The application receives webhook payloads from GitHub and processes:

### Push Events
- Captures author information
- Captures target branch
- Stores timestamp

### Pull Request Events
- Captures author
- Source branch
- Destination branch
- Event timestamp

### Merge Events
- Captures merge details
- Source branch
- Destination branch
- Timestamp

---

## Database Storage

Event information is stored in MongoDB using the following schema:

```json
{
  "request_id": "7d787b7f388cf6cb7385198f72acdfc5f960748d",
  "author": "Sham1718",
  "action": "PUSH",
  "from_branch": null,
  "to_branch": "main",
  "timestamp": "2026-03-02T15:23:55+05:30"
}
```

### Stored Fields

- request_id
- author
- action
- from_branch
- to_branch
- timestamp

---

## Real-Time Activity Dashboard

The UI automatically polls the backend every:

```text
15 seconds
```

to retrieve and display the latest repository activities.

Supported activity formats:

### Push Event

```text
Author pushed to branch on timestamp
```

### Pull Request Event

```text
Author submitted a pull request from branch A to branch B on timestamp
```

### Merge Event

```text
Author merged branch A to branch B on timestamp
```

---


# How to Run Project

## Clone Repository

```bash
git clone <repository-url>
```

```bash
cd webhook-repo
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment (Windows)

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file in the project root:

```env
MONGO_URI=your_mongodb_connection_string
DB_NAME=github_events
COLLECTION_NAME=events
```

---

## Run Application

```bash
python app.py
```

---

## Default Server

```bash
http://127.0.0.1:5000
```

---

# API Endpoints

## Webhook Endpoint

```http
POST /webhook
```

Receives GitHub webhook events and stores them in MongoDB.

---

## Events Endpoint

```http
GET /events
```

Returns the latest repository events from MongoDB.

---

# Author and Contact

## Author
Shyam Bharaskar

## Contact
- GitHub: https://github.com/Sham1718
- Portfolio: https://shyam-neon.vercel.app/
