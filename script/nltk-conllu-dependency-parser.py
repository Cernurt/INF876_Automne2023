# Train a ProbabilisticProjectiveDependencyParser using CoNLL-U treebank from Universal Dependencies https://github.com/UniversalDependencies
# In this script we are using Indonesian treebank https://github.com/UniversalDependencies/UD_Indonesian

from pprint import pprint
from nltk.parse import (
    DependencyGraph,
    ProbabilisticProjectiveDependencyParser
)

# open treebank file
with open('id-ud-train.conllu', 'r') as f:
    # parse dependency graphs from file
    graphs = [DependencyGraph(entry, top_relation_label='root') for entry in f.read().decode('utf-8').split('\n\n') if entry]
    
    # train ProbabilisticProjectiveDependencyParser 
    ppdp = ProbabilisticProjectiveDependencyParser()
    print('Training Probabilistic Projective Dependency Parser...')
    ppdp.train(graphs)
    
    # try to parse a sentence
    # and print tree ordered by probability (most probable first)
    sent = ['Melingge', 'adalah', 'gampong', 'di', 'kecamatan', 'Pulo', 'Aceh', '.']
    print('Parsing \'' + " ".join(sent) + '\'...')
    print('Parse:')
    for tree in ppdp.parse(sent):
        pprint(tree)