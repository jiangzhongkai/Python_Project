"""-*- coding: utf-8 -*-
 @author  : Peter_Bonnie
 @fileName    : dfa.py
"""
"""
desc:
      Write a program that reads a description of a deterministic ﬁnite automaton (DFA) 
      and then classiﬁes input strings as accepted or rejected by the DFA.
    :param:
      5-tuple: (Q,Σ,δ,q0,F), 
          Q :the set of states;
          Σ :the alphabet of possible input symbols;
          δ : the set of transition rules;
          q0 : the start state;
          F :the set of ﬁnal (accepting) states.
    :output:
          accepted or rejected
"""

class DFA(object):

    def __init__(self,Q,F,deta,sigma,q0):
        """
        :param Q: the set of states
        :param F: the set of ﬁnal (accepting) states
        :param deta:the alphabet of possible input symbols
        :param sigma:transit function
        :param q0: the start state
        """
        self.Q=Q
        self.F=F
        self.deta=deta
        self.sigma=sigma
        self.q0=q0

    """
    deta:[{'q0':{'a':'q1'}},{'q1':{'b':'q2'}},...]
    """
    def is_accept(self,x):

        index=self.get_item(self.q0)
        for char in list(x):
            if char in self.deta[index][self.q0].keys():
                self.q0=self.deta[index][self.q0][char]
                index=self.get_item(self.q0)
            else:
                print("rejected")
                return 0
        if self.q0 in self.F:
            print("accepted")
        else:
            print("rejected")

        return 0

    def get_key(self):
        """get key of transit function """
        temp_dict={}
        cnt=0
        for state in self.deta:
            for key,value in state.items():
                temp_dict[key]=cnt
            cnt+=1
        return temp_dict

    def get_item(self,start):

        temp_dict=self.get_key()
        for key,value in temp_dict.items():
            if key==start:
                return value

def get_transit_rules(input_string):

    if len(input_string.split(' '))>4:
        start_state = input_string.split(' ')[0]
        end_state = input_string.split(' ')[2]
        link_symbol = input_string.split(' ')[4]
        return (start_state,end_state,link_symbol)
    else:
        return

if __name__=="__main__":
    import sys

    commandLine=dict()
    temp_commandLines=sys.stdin.readlines()

    commandLine['states']=temp_commandLines[0].strip('\n').split(':')[1].lstrip()
    commandLine['symbols']=temp_commandLines[1].strip('\n').split(':')[1].lstrip()

    begin_index=3
    end_index=3
    for i in range(len(temp_commandLines)):
        if temp_commandLines[i].startswith('begin'):
            begin_index=i
        if temp_commandLines[i].startswith('end_'):
            end_index=i

    commandLine['transit_rules']=temp_commandLines[begin_index+1:end_index]
    for i in range(len(commandLine['transit_rules'])):
        commandLine['transit_rules'][i]=commandLine['transit_rules'][i].strip('\n')

    commandLine['start']=temp_commandLines[end_index+1].strip('\n').split(':')[1].lstrip()
    commandLine['final']=temp_commandLines[end_index+2].strip('\n').split(':')[1].lstrip()

    commandLine['input_string']=temp_commandLines[end_index+3:]
    for i in range(len(commandLine['input_string'])):
        commandLine['input_string'][i]=commandLine['input_string'][i].strip('\n')

    states=commandLine['states'].split(' ')
    symbols=commandLine['symbols'].split(' ')

    transits_rule=[]
    temp_list=[]
    for rule in commandLine['transit_rules']:
        temp_list.append(get_transit_rules(rule))

    for state in states:
        temp_dict = dict()
        temp_dict[state] = dict()
        for st in temp_list:
            if state==st[0]:
                temp_dict[state][st[2]]=st[1]
        transits_rule.append(temp_dict)

    start=commandLine['start']
    final=commandLine['final'].split(' ')

    for in_str in commandLine['input_string']:
        dfa = DFA(Q=states, F=final, deta=transits_rule, sigma=symbols, q0=start)
        in_str=list(in_str)
        dfa.is_accept(in_str)




