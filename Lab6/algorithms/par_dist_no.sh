# # Process and Thread level parallelism
# for i in {1..3}; do
#     echo "running $i"
#     pytest -n auto --dist no --parallel-threads auto; 
# done

# # Process level parallelism
# for i in {1..3}; do
#     echo "running $i"
#     pytest -n auto --dist no; 
# done

# Thread level parallelism
for i in {1..3}; do
    echo "running $i"
    pytest --dist no --parallel-threads auto; 
done