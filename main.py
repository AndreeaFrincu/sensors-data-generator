import os
import job_scheduler

job_scheduler.postData(os.environ['ENDPOINT'], os.environ['LOCATION'], os.environ['COLLECTOR'])