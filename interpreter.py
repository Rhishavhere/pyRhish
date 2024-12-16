class RhishInterpreter:
  def __init__(self):
    self.variables = {}
    self.rhish = type('Rhish', (), {
      'whisper': self._execute_print,
      'listen': self._execute_input
    })()
  
  def execute(self,code):
    lines = code.split("\n")
    for line in lines:
      line = line.strip()
      if not line:
        continue
      try:
        if "=" in line:
          self._execute_assign(line)
        else:
          eval(line, {'rhish': self.rhish}, self.variables)
      except Exception as e:
        print(f"Rhish Language Doesn't Understand: {line}")
        print(f"Error: {e}")
  
  def _execute_assign(self,line):
    var_name, expression = line.split("=", 1)
    var_name = var_name.strip()
    expression = expression.strip()
    value = eval(expression, {'rhish': self.rhish}, self.variables)
    self.variables[var_name] = value
  
  def _execute_print(self, line=None, *args):
    if line and isinstance(line, str) and line.startswith("rhish.whisper"):

      content = line[line.index("(") + 1:line.rindex(")")]
      args = [arg.strip() for arg in content.split(',')]
    else:

      args = [line] + list(args)

    output = []
    for arg in args:
      if isinstance(arg, str) and (arg.startswith('"') or arg.startswith("'")):
        output.append(arg.strip('"').strip("'"))
      else:
        try:

          value = eval(str(arg), {'rhish': self.rhish}, self.variables)
          output.append(str(value))
        except:

          output.append(str(arg))
    
    print(''.join(output))

  def _execute_input(self, line=None):
    if line:
      content = line[line.index("(") + 1:line.rindex(")")]
      prompt = content.strip('"').strip("'") if content else ""
    else:
      prompt = ""
    user_input = input(prompt)
    try:
      return int(user_input)
    except ValueError:
      return user_input
