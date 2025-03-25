import matplotlib.pyplot as plt

workers = [1, 2, 4, 16]
speedup_no = [0.94, 1.08, 1.02, 0.78]
speedup_load = [0.9, 1.06, 1.06, 0.81]
failures_no = [0, 0, 0, 0]
failures_load = [0, 0, 0, 0]

# Speedup plot
plt.figure(figsize=(10, 5))
plt.plot(workers, speedup_no, marker='o', color='blue', label='--dist no')
plt.plot(workers, speedup_load, marker='o', color='orange', label='--dist load')
plt.xlabel('Worker Count')
plt.ylabel('Speedup Ratio')
plt.title('Speedup Comparison by Worker Count')
plt.xticks(workers)
plt.legend()
plt.grid(True)
plt.savefig("speedup_plot_process.png")

# Failure rate plot
plt.figure(figsize=(10, 5))
plt.plot(workers, failures_no, marker='o', color='red', label='--dist no')
plt.plot(workers, failures_load, marker='o', color='green', label='--dist load')
plt.xlabel('Worker Count')
plt.ylabel('Number of Flaky Tests')
plt.title('Failure Rate Comparison by Worker Count')
plt.xticks(workers)
plt.legend()
plt.grid(True)
plt.savefig("failure_rate_plot_process.png")

print("Plots saved as speedup_plot_process.png and failure_rate_plot_process.png")
