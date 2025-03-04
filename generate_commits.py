
#!/usr/bin/env python3
import os
import random
import subprocess
import time
from datetime import datetime, timedelta

# List of small changes we can make
CHANGES = [
    # Add comments
    {"type": "comment", "files": ["app/utils/openai_helper.py", "app/models.py", "app.py"]},
    # Modify CSS values 
    {"type": "css", "files": ["static/css/custom.css", "app/static/css/custom.css"]},
    # Modify logging messages
    {"type": "logging", "files": ["app.py", "app/utils/admin_helper.py"]},
    # Modify variable names
    {"type": "variable", "files": ["app.py", "app/utils/admin_helper.py"]},
]

# Comment templates
COMMENTS = [
    "# TODO: Refactor this later",
    "# FIXME: Consider a more efficient approach",
    "# NOTE: This implementation is temporary",
    "# DEBUG: Added for troubleshooting",
    "# This works but could be improved",
    "# Consider caching this result",
    "# Performance optimization needed here",
    "# Security review required",
    "# Added on {date}",
]

# CSS properties to modify
CSS_PROPERTIES = [
    {"property": "margin", "values": ["0.5rem", "0.75rem", "1rem", "1.25rem", "1.5rem"]},
    {"property": "padding", "values": ["0.5rem", "0.75rem", "1rem", "1.25rem", "1.5rem"]},
    {"property": "border-radius", "values": ["4px", "6px", "8px", "10px", "12px"]},
    {"property": "font-size", "values": ["0.8rem", "0.9rem", "1rem", "1.1rem", "1.2rem"]},
]

# Variable name variations
VARIABLE_PREFIXES = ["temp_", "my_", "current_", "new_", "processed_", "updated_"]

def make_commit(message):
    """Create a Git commit with the given message"""
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", message])
    print(f"Created commit: {message}")

def add_comment(file_path):
    """Add a random comment to a file"""
    if not os.path.exists(file_path):
        return False
    
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    if not lines:
        return False
    
    # Choose a random line to add comment after
    insert_pos = random.randint(0, len(lines) - 1)
    comment = random.choice(COMMENTS).replace("{date}", datetime.now().strftime("%Y-%m-%d"))
    
    # Insert the comment
    lines.insert(insert_pos, comment + "\n")
    
    with open(file_path, 'w') as f:
        f.writelines(lines)
    
    return True

def modify_css(file_path):
    """Modify a CSS property in a CSS file"""
    if not os.path.exists(file_path):
        return False
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    if not content:
        return False
    
    # Choose a random CSS property to modify
    prop_to_modify = random.choice(CSS_PROPERTIES)
    property_name = prop_to_modify["property"]
    new_value = random.choice(prop_to_modify["values"])
    
    # Find and replace the property
    import re
    pattern = rf'{property_name}:\s*[^;]+;'
    replacement = f'{property_name}: {new_value};'
    
    # Check if we have a match before replacing
    if re.search(pattern, content):
        modified_content = re.sub(pattern, replacement, content, 1)
        
        with open(file_path, 'w') as f:
            f.write(modified_content)
        
        return True
    
    return False

def modify_logging(file_path):
    """Modify a logging message"""
    if not os.path.exists(file_path):
        return False
    
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    if not lines:
        return False
    
    # Look for logging lines
    log_lines = []
    for i, line in enumerate(lines):
        if "log" in line.lower() and "(" in line and ")" in line:
            log_lines.append(i)
    
    if not log_lines:
        return False
    
    # Choose a random logging line to modify
    line_idx = random.choice(log_lines)
    
    # Add a timestamp or modify the message slightly
    current_time = datetime.now().strftime("%H:%M:%S")
    if "'" in lines[line_idx]:
        lines[line_idx] = lines[line_idx].replace("'", f"'[{current_time}] ", 1)
    elif '"' in lines[line_idx]:
        lines[line_idx] = lines[line_idx].replace('"', f'"[{current_time}] ', 1)
    else:
        return False
    
    with open(file_path, 'w') as f:
        f.writelines(lines)
    
    return True

def modify_variable(file_path):
    """Modify a variable name"""
    if not os.path.exists(file_path):
        return False
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    if not content:
        return False
    
    # Find variable assignments
    import re
    assignments = re.findall(r'(\w+)\s*=\s*', content)
    
    if not assignments:
        return False
    
    # Filter out some common variables we don't want to change
    safe_to_change = [var for var in assignments if var not in ['app', 'db', 'response', 'request', 'session', 'self']]
    
    if not safe_to_change:
        return False
    
    # Choose a random variable to modify
    var_to_modify = random.choice(safe_to_change)
    new_var_name = random.choice(VARIABLE_PREFIXES) + var_to_modify
    
    # Replace all occurrences with the new name
    pattern = r'\b' + var_to_modify + r'\b'
    modified_content = re.sub(pattern, new_var_name, content)
    
    with open(file_path, 'w') as f:
        f.write(modified_content)
    
    return True

def make_random_change():
    """Make a random change to the codebase"""
    change_type = random.choice(CHANGES)
    file_path = random.choice(change_type["files"])
    
    success = False
    
    if change_type["type"] == "comment":
        success = add_comment(file_path)
    elif change_type["type"] == "css":
        success = modify_css(file_path)
    elif change_type["type"] == "logging":
        success = modify_logging(file_path)
    elif change_type["type"] == "variable":
        success = modify_variable(file_path)
    
    return success, change_type["type"], file_path

def generate_commits(num_commits):
    """Generate the specified number of commits with random changes"""
    count = 0
    attempts = 0
    max_attempts = num_commits * 2  # Allow for some failures
    
    while count < num_commits and attempts < max_attempts:
        success, change_type, file_path = make_random_change()
        
        if success:
            commit_message = f"[{change_type}] Made small change to {file_path}"
            make_commit(commit_message)
            count += 1
            
            # Small delay to ensure commits have different timestamps
            time.sleep(0.5)
        
        attempts += 1
    
    return count

if __name__ == "__main__":
    # Try to initialize git if not already initialized
    if not os.path.exists(".git"):
        subprocess.run(["git", "init"])
        print("Initialized git repository")
    
    # Generate 400 commits
    num_commits = 400
    commits_made = generate_commits(num_commits)
    
    print(f"Successfully generated {commits_made} commits")
