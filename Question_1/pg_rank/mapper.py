
import sys
  

for line in sys.stdin:
   
    if len(line) == 0 or line[0] == '#':
        continue
    

    x, target_node = line.split('\t', 1)


    try:
        
        target_node = int(target_node)
    except ValueError:
        continue

    print('%s\t%s' % (target_node, 1))
    print('%s\t%s' % (x, 0))
    
