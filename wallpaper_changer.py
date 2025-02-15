import os
import ctypes

def change_background(image_path):
    """
    Changes the desktop background on a Windows system.

    Args:
        image_path (str): Full path to the image file.
    """
    # Verify the file exists
    if not os.path.exists(image_path):
        print(f"Error: File not found at {image_path}")
        return

    # Update the Windows registry to set the wallpaper
    os.system(f'reg add "HKEY_CURRENT_USER\\Control Panel\\Desktop" /v Wallpaper /t REG_SZ /d "{image_path}" /f')

    # Refresh the system parameters to apply the new wallpaper
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
    print("Desktop background updated successfully!")







# Set the image path and execute the command

