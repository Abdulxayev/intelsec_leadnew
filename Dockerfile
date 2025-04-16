FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "main.py"]

# Install Go
RUN apt update && apt install -y golang git

# Install subfinder
RUN go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest

# Add subfinder to PATH
ENV PATH="/root/go/bin:$PATH"
