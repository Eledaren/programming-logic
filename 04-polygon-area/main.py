def area(polygon):
  if polygon == 1:
    sqr_area = int(input('Enter the side of a square: '))
    return sqr_area * 2
  elif polygon == 2:
    rec_base = int(input('Enter the base of the rectangle: '))
    rec_height = int(input('Enter the height of the rectangle: '))
    return rec_base * rec_height
  elif polygon == 3:
    tri_base = int(input('Enter the base of the triangle: '))
    tri_height = int(input('Enter the height of the triangle: '))
    return tri_base * tri_height / 2
  else:
    return 'Invalid input'

print('\t Polygon area calculator \n')
polygon = int(input('Enter 1 for cube, 2 for rectangle or 3 for triangle: '))

print(area(polygon))