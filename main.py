import subprocess
import platform
import webbrowser
import time
import tkinter as tk
from tkinter import ttk

def start_browser_with_proxy():
    if platform.system() == 'Linux':
        proxychains_cmd = 'proxychains'
    elif platform.system() == 'Windows':
        proxychains_cmd = 'proxychains4.exe'
    else:
        print("Unsupported operating system.")
        return

    # Define the browser command
    browser_cmd = 'firefox'  # Change this to the browser executable you want to use

    # Try to start the browser with ProxyChains
    try:
        subprocess.Popen([proxychains_cmd, browser_cmd])
    except FileNotFoundError as e:
        print(f"Error starting ProxyChains or browser: {e}")
        return

    # Wait for the browser to start (adjust sleep time as needed)
    time.sleep(5)

    # Open a test URL in the browser to verify proxy settings
    test_url = 'https://www.dnsleaktest.com'
    webbrowser.open(test_url)

# Create the main window for the GUI
window = tk.Tk()
window.title('Proxy Browser Launcher')

# Create and place the launch button
launch_button = ttk.Button(window, text='Launch Browser with Proxy', command=start_browser_with_proxy)
launch_button.pack(pady=20, padx=20)

# Start the GUI event loop
window.mainloop()
