from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import json
import time

app = FastAPI()
schedulers = {}  # Store all scheduler instances here

jobs_data = {}
with open("settings.json", "r") as f:
        jobs_data = json.load(f)

# Job function
def print_message(instance: str):
    # print(f"[JOB] {message} - Time: {time.strftime('%X')}")
    for job in jobs_data[instance]:
        print(f"[JOB] {job['message']} - Time: {time.strftime('%X')}")
    print(f"[JOB] {instance} - Time: {time.strftime('%X')}")

# Load jobs from JSON file and start schedulers
def load_jobs_from_json():
    for instance_name, job_list in jobs_data.items():
        scheduler = BackgroundScheduler()
        print(f"Starting scheduler for {instance_name}...")
        # for job in job_list:
        scheduler.add_job(
            print_message,
            args=[instance_name],
            trigger=IntervalTrigger(seconds=10),
            id=instance_name,
            replace_existing=True
        )
        schedulers[instance_name] = scheduler
        scheduler.start()

# Startup event to load jobs when FastAPI starts
@app.on_event("startup")
def startup_event():
    print("Starting all schedulers...")
    load_jobs_from_json()

# Shutdown event to stop schedulers
@app.on_event("shutdown")
def shutdown_event():
    print("Shutting down all schedulers...")
    for scheduler in schedulers.values():
        scheduler.shutdown()

@app.get("/")
def read_root():
    return {"message": "FastAPI + APScheduler is running"}

@app.get("/status")
def get_status():
    return {
        instance: [job.id for job in sched.get_jobs()]
        for instance, sched in schedulers.items()
    }
