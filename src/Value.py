# Returns a value's type. This function attempts to retrieve a type from Vars, ValueExpressions, or Literals. Calls are not currently supported.
def get_value_type(value):
  if isinstance(value, Var):
    return value.type 

  if isinstance(value, ValueExpression):
    exp = value.expression

    # handles struct attribute cases such as params.TokenIn
    if "." in exp:
      struct_attr = value.get_operands()[-1]
      if not isinstance(struct_attr, Var):
        return None

      return str(value.get_operands()[-1].type)

    # handles array cases such as params["tokenInKey"]
    # Note: this case is limited and may return an incorrect type. User beware.
    if "[" in exp:
      if not isinstance(value.get_operands()[0], Var):
        return None

      return str(value.get_operands()[0].type[2:])

  if isinstance(value, Literal):
    return str(value.get_type())

  return None
