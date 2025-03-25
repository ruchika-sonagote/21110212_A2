import subprocess
import time
import statistics
configs = [
    "--dist no",
    "--dist load"
]
worker_counts = [1, 2, 4, "auto"]
repetitions = 3
Tseq = 3.104
results = []
# Run each parallel config with different worker counts
for config in configs:
    for workers in worker_counts:
        parallel_times = []
        flaky_tests = set()

        print(f"Running config: {config}, Workers: {workers}")
        for i in range(repetitions):
            print(f"  Repetition {i+1}")
            start = time.time()
            command = f"pytest -n {workers} {config}"
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            parallel_times.append(time.time() - start)

            # Detect flaky tests from output
            for line in result.stdout.split("\n"):
                if "FAILED" in line:
                    flaky_tests.add(line.strip())

        # Calculate average parallel time and speedup ratio
        Tpar = statistics.mean(parallel_times)
        speedup = Tseq / Tpar

        results.append({
            "config": config,
            "workers": workers,
            "Tpar": round(Tpar, 2),
            "speedup": round(speedup, 2),
            "flaky_tests": len(flaky_tests)
        })
print("\nExecution Results:")
print(f"{'Mode':<20} {'Workers':<10} {'Tpar (s)':<10} {'Speedup':<10} {'Flaky Tests':<10}")
print("=" * 60)
for r in results:
    print(f"{r['config']:<20} {r['workers']:<10} {r['Tpar']:<10} {r['speedup']:<10} {r['flaky_tests']:<10}")
