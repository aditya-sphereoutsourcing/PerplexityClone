
#!/usr/bin/env python3
import os
import random
import subprocess
from datetime import datetime, timedelta

def get_commit_hashes():
    """Get all commit hashes from the git repository"""
    result = subprocess.run(
        ["git", "log", "--format=%H"], 
        capture_output=True, 
        text=True
    )
    commit_hashes = result.stdout.strip().split('\n')
    return commit_hashes

def redistribute_commit_dates(start_date_str="2025-01-01", end_date=None):
    """
    Redistribute commit dates between start_date and end_date
    with times between 8am and 8pm
    """
    # Parse start date or use default
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    
    # Use today as end date if not specified
    if end_date is None:
        end_date = datetime.now()
    
    # Get all commit hashes
    commit_hashes = get_commit_hashes()
    total_commits = len(commit_hashes)
    
    if total_commits == 0:
        print("No commits found in repository")
        return
    
    print(f"Found {total_commits} commits")
    
    # Calculate the time range in seconds
    time_range = (end_date - start_date).total_seconds()
    
    # Distribute commits evenly across the time range
    for i, commit_hash in enumerate(commit_hashes):
        # Calculate an evenly distributed date for this commit
        progress = i / (total_commits - 1) if total_commits > 1 else 0
        seconds_offset = time_range * progress
        
        # Set the date for this commit
        commit_date = start_date + timedelta(seconds=seconds_offset)
        
        # Adjust time to be between 8am and 8pm (8-20 hours)
        hour = random.randint(8, 20)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)
        
        commit_date = commit_date.replace(
            hour=hour, 
            minute=minute, 
            second=second
        )
        
        # Format the date in ISO 8601 format
        date_str = commit_date.strftime("%Y-%m-%dT%H:%M:%S")
        
        # Set the date using git filter-branch
        env = os.environ.copy()
        env["GIT_COMMITTER_DATE"] = date_str
        env["GIT_AUTHOR_DATE"] = date_str
        
        # Use git filter-branch to change the commit date
        subprocess.run([
            "git", "filter-branch", "--force", "--env-filter",
            f'if [ $GIT_COMMIT = "{commit_hash}" ]; then '
            f'export GIT_AUTHOR_DATE="{date_str}"; '
            f'export GIT_COMMITTER_DATE="{date_str}"; '
            f'fi',
            commit_hash + "^..HEAD"
        ], env=env)
        
        # Print progress
        print(f"Set date for commit {i+1}/{total_commits} to {date_str}")

if __name__ == "__main__":
    # Check if git repo exists
    if not os.path.exists(".git"):
        print("No git repository found. Initializing...")
        subprocess.run(["git", "init"])
    
    # Redistribute commit dates
    redistribute_commit_dates()
    
    print("Completed redistributing commit dates")
