
import sys, os

tol = sys.argv[1]
tol = float(tol)

out = {}
prev_ranks = {}

if os.path.isfile('./output/out' + '/part-00000'):
    with open('./output/out' + '/part-00000', "r") as f:
        data = f.read().split('\n')
        data.pop(-1)
        for x in data:
            node, count = x.split('\t')
            count = int(count)
            out[node] = count


if os.path.isfile('./output/' + '/result_1.txt'):
    with open('./output/' + '/result_1.txt', "r") as f:
        data = f.read().split('\n')
        data.pop(-1)
        for x in data:
            node, count = x.split('\t')
            count = float(count)
            prev_ranks[node] = count

else:
    for t in out.keys():
        prev_ranks[t] = 1/len(out)
  
current_node = None
curr_sum = 0
prev_node = None
ans = {}
  

for line in sys.stdin:
    
    prev_node, rank = line.split('\t', 1)
 
    try:
        rank = float(rank)
    except ValueError:
        
        continue
  
    
    if current_node == prev_node:
        curr_sum += rank
        
    else:
        if current_node:

            ans[current_node] = (curr_sum)
        curr_sum = rank
        current_node = prev_node


if current_node == prev_node:
    ans[current_node] = (curr_sum)
S = 0.0
for t in ans.values():
    S+=t

S = (1-S)/len(out)

for t in ans.keys():
    ans[t]+=S


f = open('./output/' + '/result_1.txt', 'w')

delta = 0.0

for t in sorted(ans.keys()):
    delta += abs(prev_ranks[t] - ans[t])
    print(f'{t}\t{ans[t]}')
    f.write(f'{t}\t{ans[t]}\n')
f.close()

if(delta <=tol):
    f = open('./output/' + '/temp2', 'w')
    f.close()