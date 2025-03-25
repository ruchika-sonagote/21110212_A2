for i in {1..10}; do
    echo "running $i"
    pytest >> test_results.txt
done