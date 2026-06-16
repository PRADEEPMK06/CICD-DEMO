# Python CI/CD Pipeline with GitHub Actions

## Project Overview

This project demonstrates a simple Continuous Integration and Continuous Deployment (CI/CD) pipeline using Python, Pytest, and GitHub Actions.

The application contains Python functions for:

* Factorial calculation
* Prime number checking

Automated testing is performed using Pytest, and the workflow is scheduled to run daily using GitHub Actions.

---

## Project Structure

```text
CICD-DEMO
├── .github
│   └── workflows
│       └── cicd.yml
├── app
│   ├── __init__.py
│   └── main.py
├── tests
│   └── test_main.py
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## Technologies Used

* Python 3.12
* Pytest
* GitHub Actions
* YAML
* Gmail SMTP Notifications

---

## Application Functions

### check_factorial()

Calculates the factorial of a given number.

Example:

```python
check_factorial(5)
# Output: 120
```

### check_prime()

Checks whether a number is prime.

Example:

```python
check_prime(13)
# Output: True
```

---

## Test Cases

The project uses Pytest for unit testing.

Test scenarios include:

### Factorial Testing

* Positive numbers
* Zero
* One
* Negative numbers

### Prime Number Testing

* Prime numbers
* Non-prime numbers
* Edge cases

Run tests locally:

```bash
python -m pytest
```

---

## CI/CD Workflow

The GitHub Actions workflow consists of four stages:

### 1. Test Stage

* Checkout source code
* Install dependencies
* Execute Pytest test cases

### 2. Build Stage

* Create build directory
* Package application files

### 3. Deploy Stage

* Simulate deployment process

### 4. Notification Stage

* Send email notification after successful execution

---

## Scheduled Execution

The workflow is configured to run automatically every day at 3:00 PM IST.

GitHub Actions Cron Expression:

```yaml
schedule:
  - cron: '30 9 * * *'
```

Explanation:

| Value | Meaning       |
| ----- | ------------- |
| 30    | Minute        |
| 9     | Hour (UTC)    |
| *     | Every Day     |
| *     | Every Month   |
| *     | Every Weekday |

09:30 UTC = 03:00 PM IST

---

## GitHub Actions Workflow

Workflow File:

```text
.github/workflows/cicd.yml
```

Execution Flow:

```text
Schedule Trigger
       ↓
Test
       ↓
Build
       ↓
Deploy
       ↓
Email Notification
```

---

## Email Notification

After successful completion of all stages, an email notification is sent to the configured recipient.

GitHub Repository Secrets:

* EMAIL_USERNAME
* EMAIL_PASSWORD

---

## How to Run Locally

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Tests

```bash
python -m pytest
```

---

## Author

Pradeep MK

Project: Python CI/CD Pipeline using GitHub Actions and Pytest
