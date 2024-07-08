# Given a call, retrieve all calls within a call. 
def get_all_recursive_calls(call):
  results = [call]
  stack = [call]

  while stack:
      current_call = stack.pop()
      call_func = current_call.get_function()
      
      # IMPROVEMENT: the `"init" in call_func.name` grep more than anything is an attempt to reduce the amount of work the query does. since this check is designed to remove false positives, im ok with cutting corners here for now. right now if i remove this grep even just 100 query results ends up taking an ungodly amount of time to process.
      if is_none(call_func):
          continue

      callee_values = call_func.callee_values()
      for call_value in callee_values:
          results.append(call_value)

          if current_call.signature != call_value.signature:
            stack.append(call_value)
  
  return results