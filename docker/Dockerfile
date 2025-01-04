FROM tensorflow/serving

WORKDIR /app


COPY . /app

RUN pip install flask tensorflow

CMD ["python", "app/server.py"]