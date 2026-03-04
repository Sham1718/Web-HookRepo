# GitHub Webhook Receiver

This project implements a webhook receiver using Flask that captures GitHub repository events and stores the required information in MongoDB.

The application also provides a simple UI that polls the database every 15 seconds and displays the latest repository activities.

---

## Features

- Receives GitHub webhook events
- Handles Push, Pull Request, and Merge events
- Stores minimal event data in MongoDB
- Displays repository activities in a clean UI
- Polls MongoDB every 15 seconds to fetch updates

---

## Tech Stack

- Python
- Flask
- MongoDB Atlas
- PyMongo
- HTML
- JavaScript

---

## MongoDB Schema

The following fields are stored in the database:

request_id  
author  
action  
from_branch  
to_branch  
timestamp  

Example document:

{
  "request_id": "7d787b7f388cf6cb7385198f72acdfc5f960748d",
  "author": "Sham1718",
  "action": "PUSH",
  "from_branch": null,
  "to_branch": "main",
  "timestamp": "2026-03-02T15:23:55+05:30"
}

---

## Setup Instructions

### 1. Clone the Repository

git clone <repository-url>

cd webhook-repo

---

### 2. Create Virtual Environment

python -m venv venv

Activate the environment:

Windows:

venv\Scripts\activate

---

### 3. Install Dependencies

pip install -r requirements.txt

---

### 4. Configure Environment Variables

Create a `.env` file in the root directory and add:

MONGO_URI=your_mongodb_connection_string  
DB_NAME=github_events  
COLLECTION_NAME=events

---

### 5. Run the Application

python app.py

The server will start on:

http://127.0.0.1:5000

---

## API Endpoints

### Webhook Endpoint

POST /webhook

Receives GitHub events and stores the required data in MongoDB.

---

### Events Endpoint

GET /events

Returns the latest repository events from MongoDB.

---

## UI

The UI is served from the Flask application and displays the latest repository activities.

It automatically polls the backend every **15 seconds** to retrieve new events.

Event formats displayed:

Push

Author pushed to branch on timestamp

Pull Request

Author submitted a pull request from branch A to branch B on timestamp

Merge

Author merged branch A to branch B on timestamp