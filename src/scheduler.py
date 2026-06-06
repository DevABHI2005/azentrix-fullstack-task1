from apscheduler.schedulers.blocking import BlockingScheduler
from main import run_pipeline

# Run once immediately when scheduler starts
run_pipeline()

scheduler = BlockingScheduler()

# Run every 24 hours
scheduler.add_job(
    run_pipeline,
    trigger="interval",
    seconds=15
)

print("Scheduler Started...")
print("Pipeline will run every 15 seconds.")

try:
    scheduler.start()

except (KeyboardInterrupt, SystemExit):
    print("Scheduler Stopped.")