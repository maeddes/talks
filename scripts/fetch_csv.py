import requests

# Your public CSV export link from Google Sheets
CSV_URL = "https://docs.google.com/spreadsheets/d/1TW71wIFpP9u2jedjqvU8-B9NhDwQIgfUqR-T5IZcbkQ/export?format=csv&gid=0"

# Output file path
OUTPUT_FILE = "data/download.csv"

def download_csv():
    print(f"Downloading CSV from: {CSV_URL}")
    response = requests.get(CSV_URL)
    response.encoding = "utf-8"  # Make sure UTF-8 is used!
    response.raise_for_status()

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(response.text)

    print(f"Saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    download_csv()
