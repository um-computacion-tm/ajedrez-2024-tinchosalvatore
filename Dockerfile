FROM python:3-alpine

RUN apk add --no-cache git
RUN git clone https://github.com/um-computacion-tm/ajedrez-2024-tinchosalvatore.git

WORKDIR /ajedrez-2024-tinchosalvatore

RUN pip install -r requirements.txt

CMD ["sh", "-c", "coverage run -m unittest && coverage report -m && python3 -m main.cli"]

# docker buildx build -t ajedrez --no-cache .
# docker run -i ajedrez