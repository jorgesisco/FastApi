# FastAPI Project Management System

This is a simple Project Management System built using FastAPI, which provides RESTful API endpoints for managing projects and tasks.

## Project structure
```commandline
.
├── Makefile
├── Pipfile
├── Pipfile.lock
├── README.md
├── app
│   ├── __init__.py
│   ├── create_tables.py
│   ├── database.py
│   ├── main.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── project_model.py
│   │   └── task_model.py
│   ├── routers
│   │   ├── __init__.py
│   │   ├── project_router.py
│   │   └── task_router.py
│   └── schemas
│       ├── __init__.py
│       ├── project_schema.py
│       └── task_schema.py
├── requirements.txt
├── run.py
├── test.db
└── tests
    ├── __init__.py
    ├── conftest.py
    └── test_projects.py

```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/jorgesisco/FastApi.git
cd fastapi-project-management
```

2. Create a virtual environment and activate it

Use the make command:
```commandline
make install
```
## Running the server
This run will test the app before running.
```commandline
make run
```

## API Endpoints
- Projects
    - GET /projects: Retrieve all projects
    - POST /projects: Create a new project
    - GET /projects/{project_id}: Retrieve a specific project by ID
    - PUT /projects/{project_id}: Update a specific project by ID
    - DELETE /projects/{project_id}: Delete a specific project by ID
    

- Tasks (Pending to implement)
  - GET /tasks: Retrieve all tasks
  - POST /tasks: Create a new task
  - GET /tasks/{task_id}: Retrieve a specific task by ID
  - PUT /tasks/{task_id}: Update a specific task by ID
  - DELETE /tasks/{task_id}: Delete a specific task by ID

## Testing

To test the routes, type in the ter
```commandline
make test
```

## Limitations

This FastAPI Project Management System is a simple and basic implementation designed for learning purposes. As such, it has some limitations that you may need to consider if you plan to use it in a production environment:

1. **Database**: The project uses SQLite, which is suitable for small-scale applications and prototyping but may not be ideal for large-scale applications with high levels of concurrent users or requiring advanced features found in other databases like PostgreSQL or MySQL.

2. **Authentication and Authorization**: The API does not implement any form of user authentication or authorization. In a real-world application, you would need to implement user management and restrict access to resources based on user roles and permissions.

3. **Error Handling**: The API does not provide comprehensive error handling or customized error messages, which could be helpful for debugging and improving user experience.

4. **Logging**: The project does not include a logging system to track requests, errors, and other relevant information.

5. **Rate Limiting**: The API does not implement any rate limiting, which is essential in a production environment to prevent abuse and ensure fair usage.

6. **Input Validation**: While FastAPI provides basic input validation through Pydantic, more advanced input validation and sanitation may be required for a production application to prevent security vulnerabilities such as SQL injection attacks.

If you decide to expand this project or use it as a base for a production application, you may need to address these limitations to ensure the security, stability, and scalability of your application.