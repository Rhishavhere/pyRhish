class RhishInterpreter:
  def __init__(self):
    self.variables = {}
  
  def execute(self,code):
    lines = code.split("\n")
    for line in lines:
      line = line.strip()
      if not line:
        continue
      if line.startswith("rhish.whisper("):
        self._execute_print(line)
      elif "=" in line:
        self._execute_assign(line)
      else:
        print(f"Rhish Languages Doesn't Understand: {line}")
  
  def _execute_print(self,line):
    content = line[line.index("(") + 1:line.rindex(")")]
    if '"' in content or "'" in content:
      content = content.strip('"').strip("'")
      print(content)
    else:
      value = self.variables.get(content.strip(), "Undefined variable")
      print(value)
      
  def _execute_assign(self,line):
    var_name, expression = line.split("=", 1)
    var_name = var_name.strip()
    expression = expression.strip()
    value = eval(expression, {}, self.variables)
    self.variables[var_name] = value