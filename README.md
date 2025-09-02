# MCP-STUDY

This project is a simple MCP (Model Context Protocol) server that uses Ollama to analyze log files for problems.

## How to run

1.  **Prerequisites:**
    *   Docker
    *   Docker Compose

2.  **Start the server:**

    ```bash
    docker-compose up --build
    ```

    This will start both the Ollama and the server containers. The server will then analyze the `log_file.log` and print the results to the console.

## Analysis Results

The server successfully analyzed the log file and identified the following issues:

*   Database connection failed due to timeout.
*   Low disk space on /dev/sda1.
