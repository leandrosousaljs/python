lar = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = lar * alt
print(f'''Sua parede tem a dimensão de {lar}x{alt} e sua área é de {area}m²
Para pintar essa parede, você precisará de {area/2}l de tinta''')
