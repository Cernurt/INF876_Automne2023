from Inspector import *
import json
import tracemalloc

tracemalloc.start()
from objgraph import typestats

print(typestats())
large_sum = sum(list(range(1000000)))


"""
def myFunction(request):
  
  # Import the module and collect data
  inspector = Inspector()
  inspector.inspectMemory()
  # Add custom message and finish the function
  inspector.addAttribute("message", "Hello " + request['name'] + "!")

  inspector.inspectMemory()
  return inspector.finish()


print(json.dumps(myFunction(dict({'name':'Ryan'}))))
"""
print(tracemalloc.get_traced_memory())




