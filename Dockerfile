# Step 1: Use the official Python image as the base image
FROM python:3.11

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements.txt file into the container
COPY requirements.txt .

# Step 4: Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the application files into the container
COPY . .

# Step 6: Expose the Streamlit default port
EXPOSE 8501

# Step 7: Set environment variables for Streamlit (optional)
ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ENABLE_CORS=false

# Step 8: Run the Streamlit app
CMD ["streamlit", "run", "app.py"]
