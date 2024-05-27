
print ('Задача №2. Квадрат и прямоугольник.')
print ('Введите длину стороны квадрата:')
length_sq = int (input())
if length_sq <= 0:
  print ('Значение должно быть больше 0!')
else:
  print ('Периметр квадрата со стороной', length_sq, ':', length_sq * 4)
  print ('Площадь квадрата со стороной', length_sq, ':', length_sq * length_sq)
print()
print ('Введите длину и высоту прямоугольника:')
length_rec = int (input())
heght_rec = int (input())
if length_rec and heght_rec > 0:
  print ('Периметр прямоугольника со длиной', length_rec, 'и высотой', heght_rec, ':', (length_rec * 2) + (heght_rec * 2))
  print ('Площадь прямоугольника со длиной', length_rec, 'и высотой', heght_rec, ':', (length_rec * heght_rec))
else:
  print ('Значение должно быть больше 0!')