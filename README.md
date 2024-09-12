Trading Bot 🤖💹
A simple yet powerful trading bot designed to automate trading strategies using Python. This project includes two modes: Simple Mode for manual analysis and Automated Mode for executing trades based on predefined logic.

Features 🚀
Simple Mode:
Analyze screen data and suggest buy/sell actions based on visual patterns.
Easy-to-use graphical interface.
Automated Mode:
Executes buy/sell orders every 10 seconds based on market data analysis.
Tracks and displays win/loss ratios dynamically.
Project Structure 📂

Copy
trading_bot/
│
├── main.py             # Main application entry point
├── simple_mode.py      # Simple trading mode implementation
├── automated_mode.py   # Automated trading mode implementation
├── utils.py            # Utility functions for calculations
└── config.py           # Configuration settings (coords, screen region)
Installation ✨
Clone the repository:
bash

Copy
git clone https://github.com/yourusername/trading_bot.git
Install required packages:
bash

Copy
pip install numpy pandas opencv-python mss pyautogui
Usage 💡
Run main.py to launch the application:
bash

Copy
python main.py
Select between Simple Mode and Automated Mode through the GUI.
