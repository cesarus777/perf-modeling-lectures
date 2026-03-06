import graphviz

# Создаём граф с направлением слева направо и ортогональными линиями
dot = graphviz.Digraph(comment='Hierarchical Module with Export')
dot.attr(rankdir='LR', splines='ortho')

# Родительский модуль – кластер с рамкой
with dot.subgraph(name='cluster_parent') as parent:
    parent.attr(
        label='Parent Module',
        style='rounded',
        color='blue',
        fontcolor='blue',
        penwidth='2'
    )
    # Дочерний блок
    parent.node(
        'child',
        'Child Module',
        shape='box',
        style='rounded',
        fillcolor='lightgrey',
        color='black'
    )
    # Порт на границе родителя (маленький кружок)
    parent.node(
        'port',
        '',
        shape='circle',
        width='0.2',
        height='0.2',
        style='filled',
        fillcolor='red',
        #label=''
    )
    # Невидимое ребро, чтобы разместить порт справа от дочернего блока
    parent.edge('child', 'port', style='invis', weight='100', minlen='2')

# Видимое соединение от дочернего блока к порту с подписью
dot.edge(
    'child', 'port',
    label='sc_export',
    arrowhead='normal',
    penwidth='2',
    fontsize='12',
    fontcolor='red'
)

# Рендерим в PNG и открываем
dot.render('sc_export', format='png', view=True)
