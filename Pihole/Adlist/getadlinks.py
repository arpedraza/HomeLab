import requests

# List of URLs to fetch
urls = [
    "https://raw.githubusercontent.com/PolishFiltersTeam/KADhosts/master/KADhosts.txt",
    "https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.Spam/hosts",
    "https://v.firebog.net/hosts/static/w3kbl.txt",
    "https://raw.githubusercontent.com/matomo-org/referrer-spam-blacklist/master/spammers.txt",
    "https://someonewhocares.org/hosts/zero/hosts",
    "https://raw.githubusercontent.com/VeleSila/yhosts/master/hosts",
    "https://winhelp2002.mvps.org/hosts.txt",
    "https://v.firebog.net/hosts/neohostsbasic.txt",
    "https://raw.githubusercontent.com/RooneyMcNibNug/pihole-stuff/master/SNAFU.txt",
    "https://paulgb.github.io/BarbBlock/blacklists/hosts-file.txt",
    "https://adaway.org/hosts.txt",
    "https://v.firebog.net/hosts/AdguardDNS.txt",
    "https://v.firebog.net/hosts/Admiral.txt",
    "https://raw.githubusercontent.com/anudeepND/blacklist/master/adservers.txt",
    "https://v.firebog.net/hosts/Easylist.txt",
    "https://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&showintro=0&mimetype=plaintext",
    "https://raw.githubusercontent.com/FadeMind/hosts.extras/master/UncheckyAds/hosts",
    "https://raw.githubusercontent.com/bigdargon/hostsVN/master/hosts",
    "https://v.firebog.net/hosts/Easyprivacy.txt",
    "https://v.firebog.net/hosts/Prigent-Ads.txt",
    "https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.2o7Net/hosts",
    "https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/hosts/spy.txt",
    "https://hostfiles.frogeye.fr/firstparty-trackers-hosts.txt",
    "https://www.github.developerdan.com/hosts/lists/ads-and-tracking-extended.txt",
    "https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/android-tracking.txt",
    "https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/SmartTV.txt",
    "https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/AmazonFireTV.txt",
    "https://gitlab.com/quidsup/notrack-blocklists/raw/master/notrack-blocklist.txt",
    "https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareHosts.txt",
    "https://osint.digitalside.it/Threat-Intel/lists/latestdomains.txt",
    "https://v.firebog.net/hosts/Prigent-Crypto.txt",
    "https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.Risk/hosts",
    "https://bitbucket.org/ethanr/dns-blacklists/raw/8575c9f96e5b4a1308f2f12394abd86d0927a4a0/bad_lists/Mandiant_APT1_Report_Appendix_D.txt",
    "https://phishing.army/download/phishing_army_blocklist_extended.txt",
    "https://gitlab.com/quidsup/notrack-blocklists/raw/master/notrack-malware.txt",
    "https://v.firebog.net/hosts/RPiList-Malware.txt",
    "https://v.firebog.net/hosts/RPiList-Phishing.txt",
    "https://raw.githubusercontent.com/Spam404/lists/master/main-blacklist.txt",
    "https://raw.githubusercontent.com/AssoEchap/stalkerware-indicators/master/generated/hosts",
    "https://urlhaus.abuse.ch/downloads/hostfile/",
    "https://malware-filter.gitlab.io/malware-filter/phishing-filter-hosts.txt",
    "https://v.firebog.net/hosts/Prigent-Malware.txt",
    "https://zerodot1.gitlab.io/CoinBlockerLists/hosts_browser",
    "https://raw.githubusercontent.com/chadmayfield/my-pihole-blocklists/master/lists/pi_blocklist_porn_top1m.list",
    "https://v.firebog.net/hosts/Prigent-Adult.txt",
    "https://raw.githubusercontent.com/anudeepND/blacklist/master/facebook.txt"
]

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

# Save the result to a file
with open("combined_hosts.txt", "w") as f:
    for entry in unique_list:
        f.write(f"{entry}\n")

print("Combined list created successfully!")
