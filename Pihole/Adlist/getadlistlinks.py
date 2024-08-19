import requests
import os

# Load URLs from the external text file
urls_file_path = "adlinks.txt"
urls = []

if os.path.exists(urls_file_path):
    with open(urls_file_path, "r") as f:
        urls = [line.strip().strip(',') for line in f if line.strip()]

combined_list = []

# Function to process each line
def process_line(line):
    line = line.strip()
    
    if not line or line.startswith(("#", "!")):
        return None
    
    if line.startswith("||"):
        cleaned_url = line[2:].rstrip("^")
        return f"0.0.0.0 {cleaned_url}"
    elif line.startswith("127.0.0.1"):
        return line.replace("127.0.0.1", "0.0.0.0", 1)
    elif line.startswith("0.0.0.0"):
        return line
    else:
        return None

# Fetch and process the content from each URL
for url in urls:
    try:
        response = requests.get(url)
        response.raise_for_status()
        lines = response.text.splitlines()
        for line in lines:
            processed = process_line(line)
            if processed:
                combined_list.append(processed)
    except requests.RequestException as e:
        print(f"Failed to download content from {url}: {e}")

# Remove duplicates
unique_list = sorted(set(combined_list))

# Load excluded domains
excluded_domains = set()
if os.path.exists("excluded.txt"):
    with open("excluded.txt", "r") as f:
        excluded_domains = set(line.strip() for line in f if line.strip())

# Filter out the excluded domains
initial_count = len(unique_list)
final_list = []
for entry in unique_list:
    parts = entry.split()
    if len(parts) < 2:
        continue  # Skip improperly formatted lines
    domain = parts[1]  # Get the domain part
    if not any(excluded_domain in domain for excluded_domain in excluded_domains):
        final_list.append(entry)

# Calculate how many entries were removed
removed_count = initial_count - len(final_list)
print(f"Number of entries removed due to exclusions: {removed_count}")

# Save the result to a file
with open("combined_hosts.txt", "w") as f:
    for entry in final_list:
        f.write(f"{entry}\n")

print("Combined list created successfully!")
