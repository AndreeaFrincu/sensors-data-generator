FROM python:3
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir schedule random2 requests
WORKDIR /usr/src/app
COPY ./generator.py .
COPY ./post_data.py .
COPY ./job_scheduler.py .
CMD ["job_scheduler.py"]
ENTRYPOINT ["python3"]