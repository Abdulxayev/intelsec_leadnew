FROM python:3.10-slim

# Install required tools
RUN apt update && apt install -y wget git ca-certificates build-essential

# Install Go manually (1.20 or higher)
ENV GOLANG_VERSION=1.21.0
RUN wget https://go.dev/dl/go${GOLANG_VERSION}.linux-amd64.tar.gz && \
    rm -rf /usr/local/go && \
    tar -C /usr/local -xzf go${GOLANG_VERSION}.linux-amd64.tar.gz && \
    rm go${GOLANG_VERSION}.linux-amd64.tar.gz
ENV PATH="/usr/local/go/bin:/root/go/bin:$PATH"

# Install subfinder
RUN go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest

# Set working directory
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

# Start your bot
CMD ["python", "main.py"]
