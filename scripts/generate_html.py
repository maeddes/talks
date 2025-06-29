import csv
import os
import html

TOPIC_MAP = {
    "springboot": {
        "icon": "https://start.spring.io/images/icon-48x48.png",
        "url": "https://spring.io/projects/spring-boot"
    },
    "buildpacks": {
        "icon": "https://buildpacks.io/images/favicon.png",
        "url": "https://buildpacks.io/"
    },
    "paketo": {
        "icon": "https://paketo.io/v2/images/logo-paketo-light.svg",
        "url": "https://paketo.io/"
    },
    "graalvm": {
        "icon": "https://www.graalvm.org/resources/img/favicon/favicon-light/favicon-light.ico",
        "url": "https://www.graalvm.org/"
    },
    "docker": {
        "icon": "https://www.docker.com/app/uploads/2024/02/cropped-docker-logo-favicon-192x192.png",
        "url": "https://www.docker.com/"
    },
    "kubernetes": {
        "icon": "https://kubernetes.io/icons/favicon-64.png",
        "url": "https://www.kubernetes.io/"
    },
    "java": {
        "icon": "https://wiki.openjdk.org/plugins/servlet/theme/engine/resource/OPENJDKV1/nanoduke.ico",
        "url": "https://www.java.com/"
    },
    "testcontainer": {
        "icon": "https://testcontainers.com/favicon.ico",
        "url": "https://testcontainers.com/"
    },
    "codespaces": {
        "icon": "https://github.githubassets.com/favicons/favicon.png",
        "url": "https://github.com/features/codespaces"
    },
    "gitpod": {
        "icon": "https://www.gitpod.io/favicon192.png",
        "url": "https://www.gitpod.io/"
    },
    "devpod": {
        "icon": "https://cdn.prod.website-files.com/645b6806227d4a212e2d01ca/67d8d69cb6c27444ff45d9c0_Favicon.png",
        "url": "https://devpod.sh/"
    },
    "opentelemetry": {
        "icon": "https://opentelemetry.io/favicons/favicon.ico",
        "url": "https://opentelemetry.io/"
    },
    "jaeger": {
        "icon": "https://www.jaegertracing.io/favicon.ico",
        "url": "https://www.jaegertracing.io/"
    },
    "kiali": {
        "icon": "https://cdn.prod.website-files.com/645b6806227d4a212e2d01ca/67d8d69cb6c27444ff45d9c0_Favicon.png",
        "url": "https://devpod.sh/"
    },
    "istio": {
        "icon": "https://istio.io/latest/favicons/favicon.ico",
        "url": "https://istio.io/"
    },
    "prometheus": {
        "icon": "https://prometheus.io/icon.svg",
        "url": "https://prometheus.io/"
    },
    "grafana": {
        "icon": "https://grafana.com/static/assets/img/fav32.png",
        "url": "https://grafana.com/"
    },
    "cilium": {
        "icon": "https://cilium.io/favicon-32x32.png",
        "url": "https://cilium.io/"
    },
    "ebpf": {
        "icon": "https://ebpf.io/favicon-32x32.png",
        "url": "https://ebpf.io/"
    }


}

def generate_html(input_csv, output_file):
    rows = []
    with open(input_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            country = html.escape(row['country_code'])
            event = f'<a href="{row["event_url"]}" target="_blank" rel="noopener noreferrer">{html.escape(row["event_name"])}</a>'
            date = row['date']
            talk = f'<a href="{row["talk_url"]}" target="_blank" rel="noopener noreferrer">{html.escape(row["talk_title"])}</a>'
            if row.get("co_speaker"):
                talk += f'<br><small>with {html.escape(row["co_speaker"])}</small>'

            topic_icons = []
            topics = row.get("topics", "").split(";")
            for topic in topics:
                topic = topic.strip().lower()
                if topic and topic in TOPIC_MAP:
                    icon = TOPIC_MAP[topic]['icon']
                    link = TOPIC_MAP[topic]['url']
                    topic_icons.append(f'<a href="{link}" title="{topic}" target="_blank" rel="noopener noreferrer"><img src="{icon}" height="25px"></a>')

            assets = []
            if row.get("video_url"):
                assets.append(f'<a href="{row["video_url"]}" target="_blank" rel="noopener noreferrer"><img src="https://openmoji.org/data/color/svg/E044.svg" width="25px" title="Video"></a>')
            if row.get("photo_url"):
                assets.append(f'<a href="{row["photo_url"]}" target="_blank" rel="noopener noreferrer"><img src="https://openmoji.org/data/color/svg/1F4F8.svg" width="25px" title="Fotos"></a>')
            if row.get("slides_url"):
                assets.append(f'<a href="{row["slides_url"]}" target="_blank" rel="noopener noreferrer"><img src="https://openmoji.org/data/color/svg/1F4CA.svg" width="25px" title="Slides"></a>')
            if row.get("github_url"):
                assets.append(f'<a href="{row["github_url"]}" target="_blank" rel="noopener noreferrer"><img src="https://openmoji.org/data/color/svg/E045.svg" width="25px" title="GitHub"></a>')

            if row.get("event_name"):
                html_row = f"<tr><td>{country}</td><td>{event}</td><td>{date}</td><td>{talk}</td><td>{' '.join(topic_icons)}</td><td>{' '.join(assets)}</td></tr>"
                rows.append(html_row)

    html_table = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Talks</title>
        <meta charset="UTF-8">
    </head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.2.0/github-markdown.min.css">
    <body class="markdown-body">
    <h1>Talks</h1>
    <table border="1" cellspacing="0" cellpadding="6">
        <thead>
            <tr>
            <th style="text-align:center;">
                <img src="https://openmoji.org/data/color/svg/1F5FA.svg" width="40px" title="Country">
            </th>
            <th style="text-align:center;">
                <img src="https://openmoji.org/data/color/svg/1F3A1.svg" width="40px" title="Event">
            </th>
            <th style="text-align:center;">
                <img src="https://openmoji.org/data/color/svg/1F4C5.svg" width="40px" title="Date">
            </th>
            <th style="text-align:center;">
                <img src="https://openmoji.org/data/color/svg/1F4AC.svg" width="40px" title="Talk">
            </th>
            <th style="text-align:center;">
                <img src="https://openmoji.org/data/color/svg/E259.svg" width="40px" title="Topics">
            </th>
            <th style="text-align:center;">
                <img src="https://openmoji.org/data/color/svg/E269.svg" width="40px" title="Links">
            </th>
            </tr>
        </thead>
        <tr><th>Country</th><th>Event</th><th>Date</th><th>Title</th><th>Tech Topics</th><th>Links to Assets</th></tr>
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
