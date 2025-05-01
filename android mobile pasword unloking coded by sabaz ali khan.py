import os

# ADB command to try disabling lock screen (works only on some rooted devices or specific conditions)
def disable_lockscreen():
    try:
        os.system("adb shell locksettings clear --old 4321")  # Replace 4321 with your current PIN
        print("Lock screen disable attempt completed.")
    except Exception as e:
        print(f"Error: {e}")

disable_lockscreen()