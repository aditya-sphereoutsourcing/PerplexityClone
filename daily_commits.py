
#!/usr/bin/env python3
import os
import random
import subprocess
from datetime import datetime, timedelta

def make_minor_change(file_path="README.md"):
    """Make a small change to a file to create a commit"""
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write("# Project Documentation\n\nThis file was updated on " + datetime.now().strftime("%Y-%m-%d"))
        return True
    
    with open(file_path, 'a') as f:
        f.write(f"\n\nUpdate on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    return True

def create_commit_with_date(date_str):
    """Create a commit with a specific date"""
    # Parse date
    date = datetime.strptime(date_str, "%Y-%m-%d")
    
    # Generate a random time between 8am and 8pm
    hour = random.randint(8, 20)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    
    commit_date = date.replace(hour=hour, minute=minute, second=second)
    date_time_str = commit_date.strftime("%Y-%m-%dT%H:%M:%S")
    
    # Files that might be modified
    files_to_modify = [
        "README.md", 
        "app/models.py", 
        "app/utils/openai_helper.py",
        "app/auth/routes.py",
        "app/main/routes.py",
        "app/static/css/custom.css"
    ]
    
    # Choose a random file to modify
    modified_file = random.choice(files_to_modify)
    
    # Make a small change to create a commit
    if make_minor_change(modified_file):
        # Set the environment variables for the commit date
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = date_time_str
        env["GIT_COMMITTER_DATE"] = date_time_str
        
        # Create the commit
        subprocess.run(["git", "add", "."], env=env)
        commit_message = f"Update for {date.strftime('%Y-%m-%d')}"
        subprocess.run(["git", "commit", "-m", commit_message], env=env)
        
        print(f"Created commit for {date.strftime('%Y-%m-%d')} at {hour:02d}:{minute:02d}:{second:02d}")
        return True
    
    return False

def create_commits_from_date_list(date_list):
    """Create commits for each date in the list"""
    # Check if git repo exists
    if not os.path.exists(".git"):
        print("No git repository found. Initializing...")
        subprocess.run(["git", "init"])
    
    total_dates = len(date_list)
    successful_commits = 0
    
    for i, date_str in enumerate(date_list):
        print(f"Processing date {i+1}/{total_dates}: {date_str}")
        if create_commit_with_date(date_str):
            successful_commits += 1
    
    print(f"Successfully created {successful_commits} commits out of {total_dates} dates")

# List of dates to create commits for
dates = [
    "2025-01-01", "2025-01-02", "2025-01-03", "2025-01-04", "2025-01-05",
    "2025-01-06", "2025-01-07", "2025-01-08", "2025-01-09", "2025-01-10",
    "2025-01-11", "2025-01-12", "2025-01-13", "2025-01-14", "2025-01-15",
    "2025-01-16", "2025-01-17", "2025-01-18", "2025-01-19", "2025-01-20",
    "2025-01-21", "2025-01-22", "2025-01-23", "2025-01-24", "2025-01-25",
    "2025-01-26", "2025-01-27", "2025-01-28", "2025-01-29", "2025-01-30",
    "2025-01-31", "2025-02-01", "2025-02-02", "2025-02-03", "2025-02-04",
    "2025-02-05", "2025-02-06", "2025-02-07", "2025-02-08", "2025-02-09",
    "2025-02-10", "2025-02-11", "2025-02-12", "2025-02-13", "2025-02-14",
    "2025-02-15", "2025-02-16", "2025-02-17", "2025-02-18", "2025-02-19",
    "2025-02-20", "2025-02-21", "2025-02-22", "2025-02-23", "2025-02-24",
    "2025-02-25", "2025-02-26", "2025-02-27", "2025-02-28", "2025-03-01",
    "2025-03-02", "2025-03-03", "2025-03-04"
]

if __name__ == "__main__":
    create_commits_from_date_list(dates)
