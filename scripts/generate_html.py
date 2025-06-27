import csv
import os
import html

TOPIC_MAP = {
    "kubernetes": {
        "icon": "https://openmoji.org/data/color/svg/E5B4.svg",
        "url": "https://kubernetes.io/"
    },
    "observability": {
        "icon": "https://openmoji.org/data/color/svg/1F441-FE0F-200D-1F5E8-FE0F.svg",
        "url": "https://opentelemetry.io/"
    },
    "cloud": {
        "icon": "https://openmoji.org/data/color/svg/2601.svg",
        "url": "https://cloud.google.com/"
    },
    "codespaces": {
        "icon": "https://openmoji.org/data/color/svg/1F5A5.svg",
        "url": "https://github.com/features/codespaces"
    },
    "gitpod": {
        "icon": "https://openmoji.org/data/color/svg/1F4BB.svg",
        "url": "https://www.gitpod.io/"
    },
    "devpod": {
        "icon": "https://openmoji.org/data/color/svg/1F4F1.svg",
        "url": "https://devpod.sh/"
    }
}

def generate_html(input_csv, output_file):
    rows = []
    with open(input_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            country = row['country_code']
            event = f'<a href="{row["event_url"]}">{row["event_name"]}</a>'
            date = row['date']
            talk = f'<a href="{row["talk_url"]}">{row["talk_title"]}</a>'
            if row.get("co_speaker"):
                talk += f'<br><small>with {html.escape(row["co_speaker"])}</small>'

            assets = []
            if row.get("slides_url"):
                assets.append(f'<a href="{row["slides_url"]}"><img src="https://openmoji.org/data/color/svg/1F4CA.svg" width="25px" title="Slides"></a>')
            if row.get("video_url"):
                assets.append(f'<a href="{row["video_url"]}"><img src="https://openmoji.org/data/color/svg/E044.svg" width="25px" title="Video"></a>')
            if row.get("github_url"):
                assets.append(f'<a href="{row["github_url"]}"><img src="https://openmoji.org/data/color/svg/E045.svg" width="25px" title="GitHub"></a>')

            topic_icons = []
            topics = row.get("topics", "").split(";")
            for topic in topics:
                topic = topic.strip().lower()
                if topic and topic in TOPIC_MAP:
                    icon = TOPIC_MAP[topic]['icon']
                    link = TOPIC_MAP[topic]['url']
                    topic_icons.append(f'<a href="{link}" title="{topic}"><img src="{icon}" width="25px"></a>')

            html_row = f"<tr><td>{country}</td><td>{event}</td><td>{date}</td><td>{talk}</td><td>{' '.join(assets)}</td><td>{' '.join(topic_icons)}</td></tr>"
            rows.append(html_row)

    html_table = """
    <html>
    <head><title>Talks</title></head>
    <body>
    <h1>Talks</h1>
    <table border="1" cellspacing="0" cellpadding="6">
        <tr><th>Country</th><th>Event</th><th>Date</th><th>Title</th><th>Assets</th><th>Topics</th></tr>
        {}
    </table>
    </body>
    </html>
    """.format("\n".join(rows))

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_table)

    print(f"✅ HTML generated: {output_file}")

# Run it
generate_html("data/talks.csv", "output/index.html")
