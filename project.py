class Node:
    """ base class """
    def __init__(self, name,utility):
        """
        :param name: name of this node
        :param utility: utility of this node
        """
        self.name = name
        self.utility = utility

    def get_expected_utility(self):
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")


class ChanceNode(Node):

    def __init__(self, name, future_nodes, probs, utility):
        """
        :param future_nodes: future nodes connected to this node
        :param probs: probability of the future nodes
        """
        Node.__init__(self, name, utility)
        self.futureNodes = future_nodes
        self.probs = probs

    def get_expected_utility(self):
        exp_utility=self.utility
        i=0
        for node in self.futureNodes:
            exp_utility+=self.probs[i]*node.get_expected_utility()
            i+=1
        return exp_utility


class TerminalNode(Node):

    def __init__(self, name,utility):
        Node.__init__(self, name, utility)

    def get_expected_utility(self):
        return self.utility


class DecisionNode(Node):

    def __init__(self, name, future_nodes,utility):
        Node.__init__(self, name, utility)
        self.futureNode = future_nodes

    def get_expected_utility(self):

        utility_outcomes=dict()
        for node in self.futureNode:
            utility_outcomes[node.name]=node.get_expected_utility()
        return utility_outcomes

# create the terminal nodes
#sURGICAL
TS1 = TerminalNode('TS1', 38)
TS2 = TerminalNode('TS2', 37.9)
TS3 = TerminalNode('TS3', 35.0)
TS4 = TerminalNode('TS4', 34.1)
TS5 = TerminalNode('TS5', 31.2)
TS6 = TerminalNode('TS6', 10.3)
TS7 = TerminalNode('TS7', 9.2)
TS8 = TerminalNode('TS8', 0)

#non- sURGICAL
TNS1 = TerminalNode('TNS1', 38)
TNS2 = TerminalNode('TNS2', 37.9)
TNS3 = TerminalNode('TNS3', 36.9)
TNS4 = TerminalNode('TNS4', 36.0)
TNS5 = TerminalNode('TNS5', 35.0)
TNS6 = TerminalNode('TNS6', 29.3)
TNS7 = TerminalNode('TNS7', 28.2)
TNS8 = TerminalNode('TNS8', 0)

# Chance NODE FOR Scan-Surgery
SE = ChanceNode("SE",[TS3, TS6], [1.0, 0.0], 0)
SE2 = ChanceNode("SE2", [TS5, TS7],[1.0, 0.0], 0)
SD2 = ChanceNode("SD2",[TS4, SE2],[0.985,0.015], 0)
SD = ChanceNode("SD", [TS2, SE], [0.985, 0.015], 0)
SC2 = ChanceNode("SC2",[SD, SD2, TS8], [0.987, 0.012, 0.001], 0)
SC = ChanceNode("SC", [TS2, TS4, TS8],[0.987, 0.012, 0.001], 0)
SB = ChanceNode("SB",[SC, SC2],[0.64,0.36], 0)
SA = ChanceNode("SA",[TS1, SB],[0.86,0.14], 0)

# Chance NODE FOR non-Scan-Surgery
NSE = ChanceNode("NSE",[TNS3, TNS6], [0.9, 0.1], 0)
NSE2 = ChanceNode("NSE2",[TNS5, TNS7],[0.9, 0.1], 0)
NSD2 = ChanceNode("NSD2",[TNS4, NSE2], [0.9, 0.1], 0)
NSD = ChanceNode("NSD",[TNS2, NSE], [0.9, 0.1], 0)
NSC2 = ChanceNode("NSC2",[NSD, NSD2, TNS8],[0.978, 0.02, 0.002], 0)
NSC = ChanceNode("NSC", [TNS2, TNS4, TNS8],[0.978, 0.02, 0.002], 0)
NSB2 = ChanceNode("NSB2",[TNS1, NSC2], [0.88, 0.12], 0)
NSB = ChanceNode("NSB",[TNS1, NSC], [0.987,0.013], 0)
NSA = ChanceNode("NSA",[NSB, NSB2], [0.95, 0.05], 0)


# create DecisionNode
D1 = DecisionNode('D1', [SA, NSA], 0)

# print the expect utility of C1
print(D1.get_expected_utility())
