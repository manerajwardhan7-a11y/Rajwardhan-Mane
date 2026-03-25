import shapes

print(shapes.triangle_area(5, 6))

area = shapes.rectangle_area(10, 5)
print(f"Area of Rectangle: {area}")

if area > 30:
    triangle_area = shapes.triangle_area(10, 5)
    print(f"Area of Triangle: {triangle_area}")
else:
    print("Invalid choice")

print("Choose a shape:")
print("(1) Circle")
print("(2) Rectangle")
print("(3) Triangle")

choice = int(input("Enter your choice [1-3]: "))

if choice == 1:
    r = float(input("Enter radius of circle: "))
    area = shapes.circle_area(r)
    print(f"Area of Circle: {area}")
elif choice == 2:
    length = float(input("Enter length of rectangle: "))
    width = float(input("Enter width of rectangle: "))
    area = shapes.rectangle_area(length, width)
    print(f"Area of Rectangle: {area}")
elif choice == 3:
    length = float(input("Enter base of triangle: "))
    height = float(input("Enter height of triangle: "))
    area = shapes.triangle_area(length, height)
    print(f"Area of Triangle: {area}")
else:
    print("Invalid choice")