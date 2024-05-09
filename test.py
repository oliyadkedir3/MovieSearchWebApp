import os
import datetime
import subprocess

def create_commits_for_year(year):
    start_date = datetime.date(year, 1, 1)
    end_date = datetime.date(year, 12, 31)

    delta = datetime.timedelta(days=1)
    current_date = start_date

    while current_date <= end_date:
        filename = f"commit_{current_date.strftime('%Y-%m-%d')}.txt"
        with open(filename, 'w') as f:
            f.write(f"Commit for {current_date}")
        subprocess.run(['git', 'add', filename])
        subprocess.run(['git', 'commit', '-m', f'Commit for {current_date}'])
        current_date += delta

if __name__ == "__main__":
    year = int(input("Enter the year to make contributions for: "))
    create_commits_for_year(year)
