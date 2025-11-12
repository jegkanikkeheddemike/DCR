import pm4py
import os

log = pm4py.read_xes(os.path.join("..","csv2xes","MCruns.xes"))

#return the graph and the log abstraction used for mining
graph, _ = pm4py.discover_dcr(log)
# print(graph)

print("LOG PARSED:",graph)

pm4py.view_dcr(graph)
