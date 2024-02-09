FROM python:3.9-slim

# Prepare system 
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \ # Graphics library 
RUN apt-get update && apt-get install -y \
    tesseract-ocr 
#  COPY requirements.txt to the image for installation
COPY requirements.txt .


# Install Python dependencies
RUN pip install -r requirements.txt

# Copy your application source code into the Docker image
COPY . /app                                                                                                                                                                 

# Expose any ports if needed by your app
EXPOSE 8080  

# Command to run when the container starts
CMD ["python", "OCR_size.py"]  # Assuming your main script is main.py
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    