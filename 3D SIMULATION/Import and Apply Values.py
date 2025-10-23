import bpy
import math

# Path to your text file containing the data
file_path = "C:\\Users\\AsusIran\\Desktop\\bi-copter\\newer.txt"  # Adjust this to your file's location

# Function to read the file and extract the rotation data
def read_rotation_data(file_path):
    rotation_data = []
    
    with open(file_path, 'r') as file:
        # Skip header line
        file.readline()
        
        for line in file:
            if line.strip():  # Skip empty lines
                parts = line.split()  # Split by spaces
                time_str = parts[0]  # Extract time
                pitch_str = parts[1]  # Extract pitch
                roll_str = parts[2]   # Extract roll
                yaw_str = parts[3]    # Extract yaw
                
                # Store as a tuple (time, pitch, roll, yaw)
                rotation_data.append((float(time_str), float(pitch_str) + 90, float(roll_str), float(yaw_str)))
    
    return rotation_data

# Apply rotation based on the extracted data
def apply_rotations(scene, rotation_data):
    # Current frame time
    current_time = scene.frame_current / scene.render.fps  # Calculate current time in seconds
    main_body = bpy.data.objects.get("Main_Body")  # Make sure to replace with your object's name

    if main_body is None:
        print("Main Body object not found")
        return

    # Loop through the rotation data and apply the rotation at the correct time
    for data in rotation_data:
        time, pitch, roll, yaw = data

        # Only apply the rotation if the current time matches the time in the file
        if abs(current_time - time) < (1 / scene.render.fps):  # Allow small time margin
            # Convert pitch, roll, and yaw to radians and apply them
            main_body.rotation_euler[0] = math.radians(pitch)  # Pitch (x-axis)
            main_body.rotation_euler[1] = math.radians(roll)   # Roll (y-axis)
            main_body.rotation_euler[2] = math.radians(yaw)    # Yaw (z-axis)

# Read the rotation data from the file
rotation_data = read_rotation_data(file_path)

# Add a handler to update the rotations every frame
def update_rotation(scene):
    apply_rotations(scene, rotation_data)

bpy.app.handlers.frame_change_pre.append(update_rotation)

print("Rotation data successfully loaded and script running!")
