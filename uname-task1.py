import platform
import shutil

system_details = platform.uname()

with open('test_file.txt', 'w') as f:
    f.write(f'System_details: {system_details }\n')
    
print("All details added successfully")
desktop_path = r"C:\Users\AVULABAB\OneDrive - Capgemini\Desktop"

shutil.move('test_file.txt', desktop_path)
print(f"File 'test_file.txt' has been moved to the desktop.")