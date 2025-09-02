from langchain_community.llms import Ollama

def analyze_log(log_file_path):
    """Analyzes a log file for problems using Ollama."""
    try:
        with open(log_file_path, 'r') as f:
            log_content = f.read()

        llm = Ollama(model="llama2", base_url="http://localhost:11435")

        prompt = f"""Analyze the following log file and identify any errors or potential problems.

        {log_content}

        Provide a summary of the findings."""

        response = llm.invoke(prompt)

        print("\n--- Analysis Results ---")
        print(response)
        print("--- End of Analysis ---\n")

    except FileNotFoundError:
        print(f"Error: Log file not found at {log_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    analyze_log("log_file.log")
