import subprocess

def run_terraform(command: str):

    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )

        return {
            "stdout": result.stdout,
            "stderr": result.stderr
        }

    except Exception as e:
        return str(e)