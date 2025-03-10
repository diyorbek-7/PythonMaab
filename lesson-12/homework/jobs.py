import requests
from bs4 import BeautifulSoup
import sqlite3
import csv

db_name = "jobs.db"
table_name = "jobs"
url = "https://realpython.github.io/fake-jobs"


# Database setup
def setup_database():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_title TEXT,
            company TEXT,
            location TEXT,
            description TEXT,
            application_link TEXT,
            UNIQUE(job_title, company, location)
        )
    """)
    conn.commit()
    conn.close()


# Scrape job listings
def scrape_jobs():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = []

    for card in soup.find_all("div", class_="card-content"):
        job_title = card.find("h2", class_="title").text.strip()
        company = card.find("h3", class_="company").text.strip()
        location = card.find("p", class_="location").text.strip()
        description = card.find("div", class_="description").text.strip()
        application_link = card.find("a", text="Apply")['href']

        jobs.append((job_title, company, location, description, application_link))

    return jobs


# Store jobs in SQLite with incremental loading
def store_jobs(jobs):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    for job in jobs:
        cursor.execute(f"""
            INSERT INTO {table_name} (job_title, company, location, description, application_link)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(job_title, company, location) DO UPDATE SET
                description = excluded.description,
                application_link = excluded.application_link
        """, job)

    conn.commit()
    conn.close()


# Filter jobs by location or company
def filter_jobs(filter_by, value):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name} WHERE {filter_by} = ?", (value,))
    results = cursor.fetchall()
    conn.close()
    return results


# Export filtered results to CSV
def export_to_csv(filename, jobs):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Job Title", "Company", "Location", "Description", "Application Link"])
        writer.writerows(jobs)


# Run the script
if __name__ == "__main__":
    setup_database()
    jobs = scrape_jobs()
    store_jobs(jobs)

    # Example: Export jobs filtered by location
    filtered_jobs = filter_jobs("location", "Remote")
    export_to_csv("filtered_jobs.csv", filtered_jobs)
    print("Job scraping and storage completed!")
