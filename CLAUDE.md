# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository is a collection of Python tutorials and examples focused on Python testing, specifically designed for QA/testers. It contains multiple tutorials organized into separate directories:

- `basic-pytest-tutorial`: Basic pytest examples and tutorials
- `advanced-pytest-tutorial`: Advanced pytest concepts and examples
- `python-unittest-tutorial`: Examples using Python's unittest framework
- `basic-questions`: Python programming exercises and examples
- `python-for-qa`: Python basics for QA engineers

## Common Commands

### Environment Setup

```bash
# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies for a specific tutorial
cd basic-pytest-tutorial
pip install -r requirements.txt
```

### Running pytest Tests

```bash
# Run all tests in current directory and subdirectories
python -m pytest

# Run tests with verbose output
python -m pytest -v

# Run specific test file
python -m pytest tests/test_feature_login.py

# Run tests matching a specific pattern
python -m pytest -k "login"

# Generate XML test report
python -m pytest --junitxml=results.xml

# Run tests in parallel (requires pytest-xdist)
python -m pytest -n auto
```

### Running unittest Tests

```bash
# Run specific unittest test file
python -m unittest tests/example_method/test_calculate_net_price.py

# Run all unittest tests
python -m unittest discover
```

## Architecture & Code Structure

The repository is organized into multiple independent tutorial sections:

1. **Basic pytest Tutorial**
   - Simple test examples using pytest
   - Demonstrates test discovery, fixtures, and parametrization
   - Located in `basic-pytest-tutorial/`

2. **Advanced pytest Tutorial**
   - Advanced concepts like fixture optimization, custom markers
   - Includes examples of sending test results via email and Slack
   - Uses conftest.py for shared fixtures and hooks
   - Located in `advanced-pytest-tutorial/`

3. **Python unittest Tutorial**
   - Classic unittest framework examples
   - Uses TestCase classes for test organization
   - Located in `python-unittest-tutorial/`

4. **Basic Python Examples**
   - Python language fundamentals and exercises
   - Includes data structures, functions, loops, conditionals
   - Located in `basic-questions/`

### Key Patterns

1. **Pytest Patterns**:
   - Test files are named with `test_` prefix
   - Test functions also use `test_` prefix
   - Uses fixtures for test setup and dependency injection
   - Conftest.py files for shared fixtures and test hooks

2. **Project Dependencies**:
   - Each tutorial section has its own requirements.txt
   - pytest and pytest-xdist are primary dependencies
   - Additional libraries for specific functionality (requests, etc.)

3. **Environment Variables**:
   - Some advanced examples use environment variables for configuration:
     - Email notification: sender.email, receiver.email, sender.password
     - Slack notification: botHookUrl

## Guidelines for Development

- Keep examples in their respective tutorial directories
- Follow the naming conventions established in each section
- Always create and activate the virtual environment before running tests
- When adding new examples, include appropriate documentation in the readme files