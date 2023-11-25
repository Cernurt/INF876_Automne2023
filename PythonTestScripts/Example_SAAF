from Inspector import *
import json

def myFunction(request):
  
  # Import the module and collect data
  inspector = Inspector()
  inspector.inspectMemory()
  large_sum = sum(list(range(1000000)))
  # Add custom message and finish the function
  inspector.addAttribute("message", "Hello " + request['name'] + "!")

  inspector.inspectMemory()
  return inspector.finish()


print(json.dumps(myFunction(dict({'name':'Ryan'}))))




