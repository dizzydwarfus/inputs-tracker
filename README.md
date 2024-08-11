# Key Press Tracker

Key Press Tracker is a Python application designed to log mouse clicks and keyboard key presses. The application provides a graphical user interface (GUI) that allows users to select activity categories and start or stop the input tracking process. It logs the events into separate JSON files for further analysis.

## Table of Contents

- [Key Press Tracker](#key-press-tracker)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Project Structure](#project-structure)
  - [Dependencies](#dependencies)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/key_press_tracker.git
   cd key_press_tracker

2. **Create and activate a virtual environment:**
   
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:
   
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application**
   To start the GUI application, run:

   ```bash
   python app.py
   ```

2. **Select Category:**
   - Use the category selector to choose the current activity type (e.g., programming, gaming).

3. **Start tracking:**
   - Click the "Run" button to begin logging mouse and keyboard events.
   - Click the "Exit" button to stop the application.
  
## Project Structure

```bash
key_press_tracker/
│
├── app.py                # Main application file for the GUI
├── tracker.py            # Handles event listening and logging
├── utils/
│   ├── _globals.py       # Contains global constants
│   ├── _logger.py        # Logger configuration
│   └── utils.py          # Utility functions for logging events
├── data/                 # Directory for storing event.json files
├── venv/                 # Virtual environment directory
├── .gitignore            # Git ignore file
└── logs.log              # Log file for debugging
```

## Dependencies
- **ttkbootstrap:** A modern tkinter theme.
- **pynput:** A library to monitor and control mouse and keyboard input.
- **logging:** Python's built-in logging module.