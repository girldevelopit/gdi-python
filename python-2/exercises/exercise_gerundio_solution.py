"""
Complete the gerundio function which translates Spanish infinitive verbs into the gerund form. It should take a single argument, the infinite verb. If the verb ends in "ar", the "ar" should be replaced with "ando". For "er" or "ir", replace them with "iendo".
"""
def gerundio(verb):
  """
  >>> gerundio('cantar')
  'cantando'
  >>> gerundio('volver')
  'volviendo'
  >>> gerundio('abrir')
  'abriendo'
  >>> gerundio('armar')
  'armando'
  """
  ending = verb[-2:]
  if ending == 'ar':
    return verb[:-2] + 'ando'
  elif ending == 'er' or ending == 'ir':
    return verb[:-2] + 'iendo'
  return verb
  #### Alternative: use endswith()
  if verb.endswith('ar'):
    return verb[:-2] + 'ando'
  elif verb.endswith('er') or verb.endswith('ir'):
    return verb[:-2] + 'iendo'
  return verb