def harvest_time(month, tuber_size):
  return month == "July" or tuber_size >= 2

def has_curly_hair(father_allele, mother_allele):
  return father_allele == "C" and mother_allele == "C"

def is_safe_to_eat(seafood_type, days_frozen):
  return seafood_type == "mollusk" or days_frozen >= 7

def can_be_president(age, residency):
  return age >= 35 and residency >= 14

def has_free_lobe(father_allele, mother_allele):
  return father_allele == "G" and mother_allele == "G"

