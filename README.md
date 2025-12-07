# Email App & Playwright BDD Tests

## Overview

This project contains a simple static email web application and automated UI tests using Playwright, Pytest, and Pytest-BDD. The app allows users to log in, compose emails, attach files, and select contacts from a static directory.

## Features

- Simple HTML email app (`email_app.html`)
- Static contact directory for quick recipient selection
- Login, compose, send email, attach file, and logout functionality
- Automated UI tests with Playwright (Python)
- BDD scenarios written in Gherkin
- Test reports generated in HTML

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd annea
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   playwright install
   ```

### Running the App

1. Start a local HTTP server in the project root:
   ```bash
   python -m http.server 8080
   ```
2. Open [http://localhost:8080/email_app.html](http://localhost:8080/email_app.html) in your browser.

### Running Tests

1. Run tests with HTML report:
   ```bash
   pytest --html=report.html
   ```
2. View the report at `report.html`.

## Usage

- Log in with email: `test@user.com` and password: `password123`
- Select a contact from the directory or enter manually
- Compose and send emails with optional attachments
- Run automated tests to verify functionality
