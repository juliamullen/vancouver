def temperature(temperature):
  if temperature < 47:
    return "a chilly {}°".format(temperature)
  if temperature < 65:
    return "a moderate {}°".format(temperature)
  return "a warm {}°".format(temperature)
