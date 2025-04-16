FROM python:3.10-slim

# Install dependencies for subfinder
RUN apt update && apt install -y golang git

# Install subfinder
RUN go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
ENV PATH="/root/go/bin:$PATH"

# Set working directory
WORKDIR /app

# Copy and install Python dependencies
COPY . .
RUN pip install -r requirements.txt

# Run your main script
CMD ["python", "main.py"]
