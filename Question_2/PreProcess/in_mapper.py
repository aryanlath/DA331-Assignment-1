
import sys, os


for line in sys.stdin:
    
    if len(line) == 0 or line[0] == '#':
        continue
    

    x, t_node = line.split('\t', 1)

    try:
        
        t_node = int(t_node)
    except ValueError:
        continue

    print('%s\t%s' % (x, 0))
    print('%s\t%s' % (t_node, 1))
    
