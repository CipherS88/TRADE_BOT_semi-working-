import cv2
import numpy as np
import mss
import time
import pyautogui
import pandas as pd
from config import BUY_BUTTON_COORDS, SELL_BUTTON_COORDS, SCREEN_REGION

# Global variables to track wins and losses
wins = 0
losses = 0

def capture_screen(region=None):
    with mss.mss() as sct:
        monitor = sct.monitors[1] if not region else {"top": region[0], "left": region[1], "width": region[2], "height": region[3]}
        img = sct.grab(monitor)
        return np.array(img)

def draw_win_loss_ratio(img):
    global wins, losses
    ratio_text = f"Wins: {wins} | Losses: {losses} | Win/Loss Ratio: {wins/(losses + 1):.2f}"
    cv2.putText(img, ratio_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

def analyze_market_data(prices):
    prices['SMA'] = prices['Close'].rolling(window=5).mean()
    return prices

def decide_trade(prices):
    if prices['Close'].iloc[-1] > prices['SMA'].iloc[-1]:
        return "buy"
    elif prices['Close'].iloc[-1] < prices['SMA'].iloc[-1]:
        return "sell"
    return "hold"

def execute_trade(action):
    global wins, losses
    print(f"Executing {action} order...")

    if action == "buy":
        pyautogui.click(*BUY_BUTTON_COORDS)  # buy button
    elif action == "sell":
        pyautogui.click(*SELL_BUTTON_COORDS)  # sell button

    time.sleep(1)  # Wait for the order to process

    # Simulate win/loss 
    result = np.random.choice(["win", "loss"])  #  win/loss 
    if result == "win":
        wins += 1
    else:
        losses += 1

def run_automated_mode():
    region = SCREEN_REGION
    price_data = []

    while True:
        screen_img = capture_screen(region)
        current_price = np.random.rand() * 1.2  # Simulated 
        price_data.append({"Close": current_price})

        if len(price_data) > 5:  # Calculate indicators 
            prices_df = pd.DataFrame(price_data)
            prices_df = analyze_market_data(prices_df)
            action = decide_trade(prices_df)

            print(f"Automated Action: {action}")
            execute_trade(action)

        # Draw the win/loss ratio on the screen
        draw_win_loss_ratio(screen_img)

        # Display the updated image (optional, for debugging)
        # cv2.imshow("Trading Bot", screen_img)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

        time.sleep(10)  # Wait before the next action

    # cv2.destroyAllWindows()
