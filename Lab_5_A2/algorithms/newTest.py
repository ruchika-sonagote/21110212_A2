import os
import subprocess

# Step 1: Run coverage report and get files with low coverage
print("Generating coverage report...")
subprocess.run(["coverage", "report", "-m"], capture_output=False)

# Step 2: Extract filenames with missing lines
coverage_output = subprocess.run(["coverage", "report", "-m"], capture_output=True, text=True).stdout
uncovered_files = []

for line in coverage_output.split("\n"):
    parts = line.split()
    if len(parts) >= 6 and parts[5] != "100%":
        file_path = parts[0]
        if file_path.endswith(".py") and "tests/" not in file_path:  # Exclude test files
            uncovered_files.append(file_path)
print(len(uncovered_files))                                                                                                                                                                                                                                                                                                                                                                                                                                                 
# Step 3: Run Pynguin on uncovered files
if not uncovered_files:
    print("All files are fully covered! No need to generate additional tests.")
else:
    print(f"Generating tests for {len(uncovered_files)} uncovered files using Pynguin...")
    for file in uncovered_files:
        module_name = file.replace("/", ".").rstrip(".py")  # Convert path to module format
        print(f"Running Pynguin for {module_name}...")
        subprocess.run(["pynguin", "--project-path", ".", "--module-name", module_name, "--output-path", "generated_tests"], capture_output=False)

print("Test generation complete. Check 'generated_tests' folder for new test cases.")
