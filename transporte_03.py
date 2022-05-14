### Transporte em 3 Tipos de Transporte ###


peso = 300
custo = ""

## Transporte Terrestre ##

if peso <= 3:
  custo = peso * 2.5 + 20
elif peso <= 5:
  custo = peso * 5.0 + 20
elif peso <= 7:
  custo = peso * 6.0 + 20
else:
  custo = peso * 8.50 + 20

print("Custo de Transporte Terrestre $", custo)

## Transporte Terrestre Premium ##

custo_premium = 125.0

if peso <= 3:
  custo_premium = peso * 3.5
elif peso <= 5:
  custo_premium = peso * 7.0
elif peso <= 7:
  custo_premium = peso * 10.0
else:
  custo_premium = peso * 13.10

print("Custo de Transporte Premium $", custo_premium)


## Trasnporte por Drone ##

if peso <= 3:
  custo_drone = peso * 5.5
elif peso <= 5:
  custo_drone = peso * 11.0
elif peso <= 7:
  custo_drone = peso * 15.50
else:
  custo_drone = peso * 16.25

print("Transporte por Drone $", custo_drone)

