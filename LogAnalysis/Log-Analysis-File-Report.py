# Create a sample log file (app.log)
sample_logs = """[2025-09-11 10:00:00] INFO - Application started
[2025-09-11 10:01:23] WARNING - Low memory detected
[2025-09-11 10:02:45] INFO - User logged in
[2025-09-11 10:03:12] ERROR - Database connection failed
[2025-09-11 10:04:33] INFO - Data loaded successfully
[2025-09-11 10:05:47] WARNING - High CPU usage
[2025-09-11 10:06:19] INFO - Request processed
[2025-09-11 10:07:52] ERROR - File not found
[2025-09-11 10:08:14] INFO - Cache updated
[2025-09-11 10:09:36] WARNING - Disk space running low
"""

# Write sample logs to app.log
with open('app.log', 'w') as f:
    f.write(sample_logs)

# Initialize counters
info_count = 0
warning_count = 0
error_count = 0

# Process the log file
with open('app.log', 'r') as log_file:
    for line in log_file:
        if '] INFO - ' in line:
            info_count += 1
        elif '] WARNING - ' in line:
            warning_count += 1
        elif '] ERROR - ' in line:
            error_count += 1

# Generate report
total_entries = info_count + warning_count + error_count
print("\nLog File Analysis Report")
print("-----------------------")
print(f"INFO entries: {info_count}")
print(f"WARNING entries: {warning_count}")
print(f"ERROR entries: {error_count}")
print(f"Total entries: {total_entries}")