FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV VIRTUAL_ENV=/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN python -m venv $VIRTUAL_ENV
RUN . /venv/bin/activate && pip install django

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
