# Flask + MongoDB Web Application

This project is a simple web application built using **Flask** (Python) and **MongoDB**. It includes a REST API with three endpoints and a frontend interface to interact with the API. The application is containerized using **Docker** and can be orchestrated using **Docker Swarm**.

---

## Features

1. **REST API**:
   - `GET /`: Returns a welcome message.
   - `POST /api/data`: Accepts data (name and age) and stores it in MongoDB.
   - `GET /api/data`: Retrieves all data stored in MongoDB.

2. **Frontend**:
   - A simple HTML frontend built with **Tailwind CSS**.
   - Displays the welcome message.
   - Provides a form to submit data.
   - Displays data retrieved from MongoDB.

3. **Dockerized**:
   - The application is containerized using Docker.
   - Includes a `Dockerfile` and `docker-compose.yml` for easy setup.

4. **Docker Swarm**:
   - The application can be deployed using Docker Swarm for orchestration.

---

## Prerequisites

- **Docker**: Install Docker from [here](https://docs.docker.com/get-docker/).
- **Docker Compose**: Install Docker Compose from [here](https://docs.docker.com/compose/install/).
- **Git**: Install Git from [here](https://git-scm.com/downloads).

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/JDevShivamGarg/Test-Project.git
cd Test-Project
```

### 2. Build and Run the Application
```bash
docker-compose up --build
```
---

Test-Project   
│   
├── app.py   
├── requirements.txt   
├── Dockerfile   
├── docker-compose.yml   
├── README.md            
├── .gitignore   
├── templates   
│   └── index.html   


---

## License
This project is licensed under the MIT License.

---

## Author
Shivam Garg

GitHub: JDevShivamGarg

Email: shivamcp2694@gmail.com

---

## Acknowledgments
Flask Documentation: https://flask.palletsprojects.com/

MongoDB Documentation: https://www.mongodb.com/docs/

Docker Documentation: https://docs.docker.com/

Tailwind CSS Documentation: https://tailwindcss.com/docs
