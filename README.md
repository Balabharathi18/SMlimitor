# Social Media Limit App

This is a Kivy-based Python application that allows users to set a time limit for social media usage on their mobile device. Once the time limit is reached, the app will lock the social media apps and notify the user that the time is up.

## Features
- Set time limits for social media usage.
- Timer to track the time spent on social media.
- Notifications to alert when the time limit is reached.
- Cross-platform support (works on Android and other platforms like Windows and Linux for testing).

## Requirements
- Python 3.x
- Kivy (for building the GUI)
- Plyer (for cross-platform notifications)

## Installation

### 1. Install Python
Ensure that Python 3.x is installed on your system. If not, install it from [python.org](https://www.python.org/).

### 2. Install Required Libraries

Run the following command to install the required libraries:
pip install -r requirements.txt
python main.py


## Packaging for Android:
pip install buildozer
buildozer init

## Build the APK
buildozer -v android debug
buildozer android deploy run


### Notes on Locking Social Media Apps:
As mentioned earlier, locking apps directly on Android requires more in-depth native Android programming, which goes beyond Kivy's cross-platform capabilities. However, you can monitor app usage with Android's UsageStatsManager and show notifications or warnings. For actual locking, you would need to implement more advanced Android features, such as Device Admin APIs or Accessibility Services.

Let me know if you need further clarification or more detailed instructions for any part of the project!
