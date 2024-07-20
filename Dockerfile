## Use the official Python 3.12 Image
FROM python:3.12-slim

## Set the working directory to /code
WORKDIR /code

## Copy the current directory contents in the container at /code
COPY ./requirements.txt /code/requirements.txt

## Install the requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Expose the port your Streamlit app will run on
EXPOSE 8501

## Setup a new user named "user"
RUN useradd user
## Switch to the "user" user
USER user

## Set home to user's home directory
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

## Set the working directory to the user's home directory
WORKDIR $HOME/app

## Copy the current directory contents into the container at $HOME/app setting the owner to
COPY --chown=user . $HOME/app

## Start the FASTAPI App on port 7860
#CMD ["uvicorn","app.app","--host","0.0.0.0","--port","7860"]

## Start the FASTAPI App
CMD ["streamlit", "run", "app.py"]

