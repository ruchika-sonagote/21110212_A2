# Load balancing with pytest-xdist
# # Process and Thread level parallelism
# for i in {1..3}; do
#     echo "running $i"
#     pytest -n auto --dist load --parallel-threads auto; 
# done

# # Process level parallelism
# for i in {1..3}; do
#     echo "running $i"
#     pytest -n auto --dist load; 
# done

# Thread level parallelism
for i in {1..3}; do
    echo "running $i"
    pytest --dist load --parallel-threads auto; 
done