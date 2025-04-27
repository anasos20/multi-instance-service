# FastAPI + APScheduler Multi-Instance Scheduler

This is a simple FastAPI app that uses **APScheduler** to run scheduled tasks from a JSON configuration file.  
Each **instance** from the JSON represents a **separate scheduler** managing multiple **jobs**, all triggered together in batches.

---

## 📁 Project Structure

. ├── main.py ├── settings.json ├── README.md

yaml
Copy
Edit

---

## ⚙️ Installation

```bash
pip install fastapi uvicorn apscheduler
🧩 Example settings.json
Create a settings.json file like this:

json
Copy
Edit
{
  "instance1": [
    {
      "id": "job1",
      "message": "Hello from instance1 - job1"
    },
    {
      "id": "job2",
      "message": "Hello from instance1 - job2"
    }
  ],
  "instance2": [
    {
      "id": "job3",
      "message": "Hello from instance2 - job3"
    },
    {
      "id": "job4",
      "message": "Hello from instance2 - job4"
    }
  ]
}
Each key (like instance1, instance2) creates a scheduler instance, and each object under it defines a job.

🚀 Running the Application
bash
Copy
Edit
uvicorn main:app --reload
The application will load the settings.json on startup and create schedulers and jobs automatically.

🔥 How It Works
Multiple Schedulers: One scheduler per instance.

Multiple Jobs: Each scheduler can manage multiple jobs.

JSON Configuration: Easy to manage your jobs through a simple JSON file.

Batch Execution: All jobs under the same scheduler run according to their triggers.

📦 Optional Features
Want even more?
Let me know — I can help you add:

✅ Endpoints to add, pause, resume, or remove jobs dynamically

✅ Custom triggers (like cron, interval, date)

✅ Health check endpoints to monitor schedulers
