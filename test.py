import os
import datetime
import subprocess

def create_commits_for_year(year, repo_path):
    start_date = datetime.date(year, 1, 1)
    end_date = datetime.date(year, 12, 31)

    delta = datetime.timedelta(days=1)
    current_date = start_date

    while current_date <= end_date:
        filename = os.path.join(repo_path, f"commit_{current_date.strftime('%Y-%m-%d')}.txt")
        with open(filename, 'w') as f:
            f.write(f"Commit for {current_date}")
        
        subprocess.run(['git', 'add', filename], cwd=repo_path)
        subprocess.run(['git', 'commit', '-m', f'Commit for {current_date}', '--date', current_date.strftime('%Y-%m-%d %H:%M:%S')], cwd=repo_path)
        
        current_date += delta

if __name__ == "__main__":
    year = 2023  # Year for which you want to create commits
    repo_path = input("Enter the path to your Git repository: ")
    create_commits_for_year(year, repo_path)
