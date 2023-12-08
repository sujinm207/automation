import os
import datetime

def delete_old_files(directory, file_prefix, hours_threshold):
    """Get current time, set threshold time"""
    current_time = datetime.datetime.now()
    threshold_time = current_time - datetime.timedelta(minutes=hours_threshold)
    
    # Check if any files with the specified prefix and extension exist
    matching_files = [filename for filename in os.listdir(directory) if filename.startswith(file_prefix) and filename.endswith('.zip')]

    if not matching_files:
        print(f"No files found with prefix '{file_prefix}' and '.zip' extension in the directory.")
        return
    
    """Loop through directory files"""
    for filename in matching_files:
        """Get file path and creation time"""
        file_path = os.path.join(directory, filename)
        file_creation_time = datetime.datetime.fromtimestamp(os.path.getctime(file_path))

        try:
            # Check if file creation time is more than specified hours ago
            if file_creation_time < threshold_time:
                os.remove(file_path)
                print(f"Deleted: {filename}")
            else:
                print(f"Not deleted: {filename} - File is not old enough to delete.")
        except Exception as e:
            print(f"Error deleting {filename}: {e}")

# Specify the directory containing the files using a raw string
directory_path = r"C:\Users\tempadmin\Pictures\Camera Roll"
# Specify the file prefix to match
file_prefix = 'ri_rms_data'
# Specify the threshold in hours
hours_threshold = 2

# Call the function to delete old files
delete_old_files(directory_path, file_prefix, hours_threshold)
