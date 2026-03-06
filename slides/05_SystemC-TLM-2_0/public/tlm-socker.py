import graphviz

dot = graphviz.Digraph(comment='TLM Socket')
dot.attr(rankdir='LR')

# Первый узел с шестерёнкой (используем HTML-подобную метку)
dot.node('A', '⚙ Compute Module\n(initiator)', shape='box', style='filled, rounded', fillcolor='black', fontcolor='white')

# Второй узел – чёрный ящик (заливка чёрным)
dot.node('B', 'Target Module\n(target)', shape='box', style='filled, rounded', fillcolor='black', fontcolor='white')

# Ребро: двунаправленная стрелка, жирная линия
dot.edge('A', 'B', label='TLM Socket', dir='both', penwidth='3', arrowhead='normal', arrowtail='normal')

dot.render('tlm_socket_graphviz', format='png', view=True)
