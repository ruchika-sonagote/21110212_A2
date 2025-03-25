for i in {1..3}; do
    echo "running $i"
    pytest >> final_results.txt
done