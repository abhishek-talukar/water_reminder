from plyer import notification
import time

def water_reminder():
    # Define the path to your icon file
    icon_path = r"E:\abhishek IS\python projects\water reminder\images.ico"

    # Infinite loop to send reminders at regular intervals
    while True:
        # Send a desktop notification
        notification.notify(
            title="**Please drink water now",
            message="Water is vital to our health. It plays a key role in many of our body's functions, including bringing nutrients to cells, getting rid of wastes, protecting joints and organs, and maintaining body temperature.",
            app_icon=icon_path,
            timeout=10  # Notification stays on screen for 10 seconds
        )
        
        # Wait for 1 hour (3600 seconds) before the next reminder
        time.sleep(3600)

if __name__ == "__main__":
    # Start the water reminder function
    water_reminder()
