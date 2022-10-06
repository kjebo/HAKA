FROM python:3.7

RUN useradd -ms /bin/bash user
USER user
WORKDIR /home/user

COPY --chown=user:user . /app
RUN pip install --user --no-warn-script-location -r /app/requirements.txt
CMD ["/app/dnscan.py", "-d", "meetball.se", "-R", "8.8.8.8"]
