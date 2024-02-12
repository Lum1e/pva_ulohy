def find_middle_point(x1, y1, x2, y2, x3, y3):

    if (x1, y1) != (x2, y2) and (x1, y1) != (x3, y3) and (x2, y2) != (x3, y3):

        sorted_points = sorted([(x1, y1), (x2, y2), (x3, y3)])


        midpoint_x = sorted_points[1][0]
        midpoint_y = sorted_points[1][1]

        return f"Prostřední bod mezi body {sorted_points[0]} a {sorted_points[2]}: ({midpoint_x}, {midpoint_y})."
    else:
        return "Nelze určit prostřední bod, protože některé body jsou stejné."



def are_points_collinear(x1, y1, x2, y2, x3, y3):

    vector1 = (x2 - x1, y2 - y1)
    vector2 = (x3 - x1, y3 - y1)


    determinant = vector1[0] * vector2[1] - vector1[1] * vector2[0]


    if abs(determinant) < 1e-10:
        return True
    else:
        return False

def calculate_midpoint(x1, y1, x2, y2):

    midpoint_x = (x1 + x2) / 2
    midpoint_y = (y1 + y2) / 2
    return midpoint_x, midpoint_y

def main():
    try:

        x1, y1 = map(float, input("Zadejte souřadnice prvního bodu (oddělené mezerou): ").split())
        x2, y2 = map(float, input("Zadejte souřadnice druhého bodu (oddělené mezerou): ").split())
        x3, y3 = map(float, input("Zadejte souřadnice třetího bodu (oddělené mezerou): ").split())


        if are_points_collinear(x1, y1, x2, y2, x3, y3):
            print("Body leží na společné přímce.")


            result = find_middle_point(x1, y1, x2, y2, x3, y3)
            print(result)
        else:
            print("Body neleží na společné přímce.")
    except ValueError:

        print("Chyba: Zadávejte pouze číselné hodnoty.")

if __name__ == "__main":
    main()