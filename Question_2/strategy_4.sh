

echo "Strategy : Clipped influence of neighbouring nodes along with their outlinks with damping factor"
echo "Enter damping Factor"
read d
echo "Enter tolerance"
read tol
echo "Enter Clipping factor in between 0 and 1"
read lb

path=output/temp2
path2=output/tempi/_SUCCESS
while [ ! -f "$path" ]; do
    hadoop jar hadoop-streaming-3.3.6.jar -input output/web-Google.txt -output output/tempi -mapper "python3 strategy_4/ranker4_mapper.py $d $lb" -reducer "python3 strategy_4/ranker4_reducer.py $tol"
    
    if [ ! -f "$path2" ]; then
        echo "ERROR, EXITING..."
        break
    fi
    
    rm -rf ./output/tempi
done

rm -rf ./output/temp2