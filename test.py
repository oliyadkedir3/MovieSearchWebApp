import datetime
import subprocess
import os

def generate_fake_commits():
    # Define the start and end dates for the year 2023
    start_date = datetime.datetime(2023, 1, 1)
    end_date = datetime.datetime(2023, 12, 31)

    # Loop through each day of the year
    current_date = start_date
    while current_date <= end_date:
        # Set the GIT_COMMITTER_DATE environment variable
        os.environ['GIT_COMMITTER_DATE'] = current_date.strftime('%Y-%m-%d 12:00:00')
        # Generate a fake commit message
        commit_message = f"Fake commit on {current_date.strftime('%Y-%m-%d')}"
        # Execute the fake commit
        subprocess.run(['git', 'commit', '--allow-empty', '-m', commit_message])
        # Move to the next day
        current_date += datetime.timedelta(days=1)

if __name__ == "__main__":
    generate_fake_commits()
