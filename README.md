

# Fastest ScreenShoot Taker Ever

The **Screenshot Taker** is a Python program designed to capture screenshots of user-defined rectangular areas on the screen. It offers a simple and interactive interface through keyboard shortcuts, allowing users to specify the starting and ending points of the desired capture region.

## Features

- **Easy Selection:** Use the "caps lock" key to mark the starting and ending points of the rectangular area for capturing a screenshot.

- **Reload Functionality:** Press "r" to reload the program, allowing for multiple captures under different names.

- **Stop Execution:** Press "s" to gracefully stop the program and view the total number of photos captured.

- **Temporary Keyboard Unhooking:** Press the "tab" key to temporarily unhook the keyboard if you need to use it for other tasks during the program's execution.

- **Validation:** The program checks for valid selections, ensuring that screenshots are taken from the top-left to bottom-right of the screen.

## Usage

1. Run the program and enter the subject or topic name when prompted.
2. Start the selection process by pressing the "caps lock" key.
3. Press "caps lock" again to mark the starting point and once more to specify the ending point for the screenshot.
4. Use "r" to reload the program for capturing under a new name.
5. Press "s" to stop the program gracefully.
6. Utilize "tab" to temporarily unhook the keyboard if needed.

## Important Notes

- The program saves screenshots to the desktop with filenames based on the specified subject and the order of capture.

- Ensure that selections are made from the top-left to bottom-right to avoid errors.

## Dependencies

- [keyboard](https://github.com/boppreh/keyboard): A Python library for working with keyboards.

- [Pillow (PIL Fork)](https://github.com/python-pillow/Pillow): Python Imaging Library (PIL) fork for working with images.

## Getting Started

1. Install the required dependencies by running:
   ```bash
   pip install keyboard Pillow
   ```

2. Run the program:
   ```bash
   python screenshot_taker.py
   ```

3. Follow the on-screen instructions to capture screenshots.

For More Detail you can message me in my Liked-IN : https://www.linkedin.com/in/mohamed-saad-604677263/
