
  
from operator import itemgetter
import sys
  
current_node = None
current_count = 0
node = None
ans = {}

for line in sys.stdin:
    
    node, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        
        continue
  
    
    if current_node == node:
        current_count += count
    else:
        if current_node:

            ans[current_node] = current_count
        current_count = count
        current_node = node
  

if current_node == node:
    ans[current_node] = current_count


for t in sorted(ans.keys()):
    print(f'{t}\t{ans[t]}')