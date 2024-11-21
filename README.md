# Project Environment Setup Guide

This guide provides step-by-step instructions to set up the required environment and install necessary packages for this project.

---

## Prerequisites

Ensure you have Python 3.11 installed on your machine.

---

## Environment Setup

1. **Create a virtual environment named `DSI314`:**

   ```bash
   python3.11 -m venv DSI314
content_copy
Use code with caution.
Markdown

Verify the Python version:

python --version
content_copy
Use code with caution.
Bash

Activate the virtual environment:

.\DSI314\Scripts\activate  (Windows)
source DSI314/bin/activate (macOS/Linux)
content_copy
Use code with caution.
Bash

Confirm the virtual environment files are created:

ls
content_copy
Use code with caution.
Bash
Install Required Packages

Check for the requirements.txt file in the project folder. Ensure it is present before proceeding.

Activate the virtual environment (if not already active):

.\DSI314\Scripts\activate (Windows)
source DSI314/bin/activate (macOS/Linux)
content_copy
Use code with caution.
Bash

Install dependencies from the requirements.txt file:

pip install -r requirements.txt
content_copy
Use code with caution.
Bash
content_copy
Use code with caution.
