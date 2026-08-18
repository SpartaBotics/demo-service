# The recipe for the sealed package: everything the app needs to run,
# frozen into one image. Built ONCE per merge by build.yml; every server
# afterwards runs this exact image.
FROM python:3.12-slim

# Stamped by build.yml — records which commit this package was built from.
ARG GIT_SHA=unknown
ENV GIT_SHA=${GIT_SHA}

WORKDIR /app
COPY app.py .

CMD ["python3", "app.py"]
