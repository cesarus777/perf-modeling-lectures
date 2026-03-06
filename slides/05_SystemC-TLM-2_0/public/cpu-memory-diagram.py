import graphviz

dot = graphviz.Digraph(comment='CPU-Memory Diagram')
dot.attr(rankdir='LR') # слева направо
dot.node('CPU', 'CPU\n(initiator)', shape='box')
dot.node('Memory', 'Memory\n(target)', shape='box')
dot.edge('CPU', 'Memory', label='read(addr, data_ptr)')
dot.edge('Memory', 'CPU', label='ok', style='dashed', color='blue')
dot.render('cpu_memory_diagram', format='png', view=True)
