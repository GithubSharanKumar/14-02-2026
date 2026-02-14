import subprocess

destination = "google.com"

with subprocess.Popen(f"tracert -h 5 {destination}", stdout=subprocess.PIPE, text=True, shell=True) as proc:
    for line in proc.stdout:
        print(line.strip())