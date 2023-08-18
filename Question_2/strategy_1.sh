

echo "Strategy : Considering the influence of the neighbouring nodes along with their outlinks"
echo "Enter tolerance value"
read tol

path=output/temp2
path2=output/tempi/_SUCCESS
while [ ! -f "$path" ]; do
    hadoop jar hadoop-streaming-3.3.6.jar -input output/web-Google.txt -output output/tempi -mapper "python3 strategy_1/ranker1_mapper.py" -reducer "python3 strategy_1/ranker1_reducer.py $tol"
    
    if [ ! -f "$path2" ]; then
        echo "ERROR, EXITING..."
        break
    fi

    rm -rf ./output/tempi
done

rm -rf ./output/temp2