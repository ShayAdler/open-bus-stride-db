# "app" should be build from the main Dockerfile
FROM app
RUN apt update && apt install -y graphviz
COPY requirements-docgen.txt ./
COPY bin/ ./bin/
RUN pip install -r requirements-docgen.txt
