
def findAlphabet(dictionary):
    '''
    given a dictionary of words in unknown lexicographic order,
    this function returns one possible alphabet.
    '''
    alphabetGraph = createLexicographicGraph(dictionary)
    alphabet = createOrder(alphabetGraph)
    return alphabet

def createLexicographicGraph(dictionary):
    '''
    creates a directed graph of all the used characters in a
    given dictionary 
    '''
    alphabetGraph = {} # maps a set of characters that come later in lexicographic order to every character
    lastWord = None
    for word in dictionary:
        if lastWord != None:
            letterIndex = 0
            compareLength = min(len(word), len(lastWord))
            while letterIndex < compareLength:
                if lastWord[letterIndex] != word[letterIndex]:
                    alphabetGraph[lastWord[letterIndex]].add(word[letterIndex])
                    break
                else:
                     letterIndex +=1
        for letter in word:
            if not (letter in alphabetGraph):
                alphabetGraph[letter] = set()
        lastWord = word
    return alphabetGraph

def createOrder(graph): 
    '''
    finds a topological ordering by finding the
    reverse post order (DFS): 
    '''
    alphabet = []
    visited = {}
    for key in graph:
        visited[key] = False
    def visit(node):
        if node in graph:
            if not visited[node]:
                visited[node] = True
                for neighbour in graph[node]:
                    visit(neighbour)
                alphabet.append(node) # post order
    for characterNode in graph:
        visit(characterNode)
    alphabet.reverse()
    return alphabet


#########################
# really short test:
#########################
import random

import unittest 
class TestFindAlphabet(unittest.TestCase): 
    def testExampleCase(self):
        dictionary = ['ART', 'RAT', 'CAT', 'CAR']
        self.assertTrue(findAlphabet(dictionary) == ['A', 'T', 'R', 'C'] or findAlphabet(dictionary) == ['T', 'A', 'R', 'C']) 
        return
    def testLoremIpsum(self): 
        # checks that english lexicographic order is correctly identified with 10000 word gibberish
        dictionary = self.createDictionary(10000)
        alphabet = findAlphabet(dictionary)
        self.assertTrue(alphabet == sorted(alphabet))
    def createDictionary(self, length):
        lipsum = ''
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ                  ' # more spaces to make them more likely
        for i in range(length):
            lipsum += random.choice(letters)
        dictionary = []
        currentWord = ''
        for char in lipsum:
            char = char.lower()
            if char == ' ':
                dictionary.append(currentWord)
                currentWord = ''
            else:
                currentWord += char
        dictionary.sort()
        return dictionary

if __name__ == '__main__': unittest.main()
