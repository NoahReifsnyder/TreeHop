# Problem File for Blocks World
from BWD import *
from random import *
from ExpectationsGenerator import *
state = None
policy = None

def run():
    global state, policy
    agent = 'Agent1'
    state = treehop.State('state')
    state.weights = {}
    state.acquired = {agent: (0, 0)}
    state.under = {}
    state.on = {}
    state.top = {}
    state.top_acquired = {}
    state.collected = {agent: 0}
    top_list = Queue()
    goal_set = {}  # goals for goal regression
    for i in range(0, 3):
        top_list.put(None)
    n = 500
    collection_weight = 500
    max_weight = 50
    variance = 2
    for i in range(0, n):
        under = top_list.get()
        state.under[i] = None
        state.under[under] = i
        state.on[i] = under
        top_list.put(i)
        temp = round((random() * (max_weight - (2 * variance))) + variance, 2)
        state.weights[i] = (temp - variance, temp + variance)
        state.top[i] = False
        state.top_acquired[i] = False
    while not top_list.empty():
        i = top_list.get()
        state.top[i] = True
    goals = [('achieve_goal', agent, collection_weight)]
    treehop.declare_goals(goals)
    policy = treehop.pyhop_t(state, goals, True)
    treehop.print_policy(policy, state)
    gen_expectations(policy, state, goal_set)

run()