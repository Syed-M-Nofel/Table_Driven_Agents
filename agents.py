#   Agents in python
#   Table driven Agents

percepts = []
table = {           #Values and Actions in our dictionary
    (("A", "Dirty"),) : "Remove the Dirt",
    (("A", "Clean"),) : "Move Right",
    (("B", "Dirty"),) : "Remove the Dirt",
    (("B", "Clean"),) : "Move Left",
    (("A", "Clean"), ("A", "Clean")) : "Move Right",
    (("A", "Clean"), ("A", "Dirty")) : "Remove the Dirt",
    (("B", "Dirty"), ("B", "Dirty")) : "Remove the Dirt",
    (("B", "Dirty"), ("B", "Clean")) : "Move left",
    (("A", "Dirty"), ("A", "Dirty")) : "Remove the Dirt",
    (("A", "Dirty"), ("A", "Clean")) : "Move Right",
    (("A", "Clean"), ("A", "Clean"), ("B", "Dirty")) : "Remove the Dirt",
    (("A", "Clean"), ("A", "Dirty"), ("A", "Clean")) : "Move Right"
}

def lookup_table(percepts, table):
    action = table.get(tuple(percepts))
    return action

def table_driven_agent(percept):
    percepts.append(percept)
    action = lookup_table(percepts, table)
    return action

def main():
    print('Percepts \t \t \t Action')
    print(percepts, '\t \t', table_driven_agent(('A', 'Clean')))
    print(percepts, '\t \t', table_driven_agent(('A', 'Clean')))
    print(percepts, '\t \t', table_driven_agent(('B', 'Dirty')))

main()