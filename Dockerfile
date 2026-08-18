# The sealed package. Built exactly once per merge (step 9 of the standard);
# every environment afterwards runs this same image.
FROM python:3.12-slim

# Stamped by CI at build time — the only difference between builds.
ARG GIT_SHA=unknown
ENV GIT_SHA=${GIT_SHA}

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py VERSION ./

EXPOSE 8000
CMD ["python", "app.py"]
