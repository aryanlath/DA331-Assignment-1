  
import sys, os
out = {}
inl = {}
prev_ranks = {}

if os.path.isfile('./output/out' + '/part-00000'):
    with open('./output/out' + '/part-00000', "r") as f:
        data = f.read().split('\n')
        data.pop(-1)
        for x in data:
            node, count = x.split('\t')
            count = int(count)
            out[node] = count

if os.path.isfile('./output/in' + '/part-00000'):
    with open('./output/in' + '/part-00000', "r") as f:
        data = f.read().split('\n')
        data.pop(-1)

        for x in data:
            node, count = x.split('\t')
            count = int(count)
            inl[node] = count


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




for line in sys.stdin:
    
    if len(line) == 0 or line[0] == '#':
        continue
    f_node, t_node = line.split('\t', 1)
    try:    
        t_node = int(t_node)
    except ValueError:
        continue
    
    p = prev_ranks[f_node]
    o = out[f_node]
    print('%s\t%s' % (t_node, (p/o)))
    if inl[f_node] == 0:
        print('%s\t%s' % (f_node, 0))
    
    
    
