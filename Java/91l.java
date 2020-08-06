import java.lang.*;

abstract class shape { // Implemented Abstract Superclass Shape
    abstract double Area(); // Abstract method to calculate Area

    abstract double Perimeter(); // Abstract method to calculate Perimeter
}

class circle extends shape { // Sub class Circle inherting Class shape.
    double radius; // Stores Radius of circle.

    circle(double a) { // Parameterised Constructor.
        this.radius = a;
    }

    double Area() { // Method overiding method Area declared in Super class.
        double A = 3.14 * radius * radius; // Area=pi*(Square of Radius);
        return A;
    }

    double Perimeter() { // Method overiding method Area declared in Super class.
        double P = 2 * 3.14 * radius; // Perimeter = 2*pi*radius. pi=3.14
        return P;
    }
}

class rectangle extends shape { // Sub class Rectangle inherting Class shape.
    double radius;
    double s1, s2; // S1 & S2 store the length of the two pais of sides of a rectangle.

    rectangle(double a, double b) { // Constructor
        s1 = a;
        s2 = b;
    }

    double Area() { // Method overiding.
        double A = s1 * s2; // Area = length(s1) * breadth(s2)
        return A;
    }

    double Perimeter() { // Method overiding.
        double P = 2 * (s1 + s2); // Perimeter = 2(length+breadth)
        return P;
    }
}

class trapezium extends shape { // Sub class trapezium inherting Class shape.
    double radius;
    double A, B, C, D, H; // A & B store length of parallel sides and C & D store length of unparallel
                          // sides H stores heigth.

    trapezium(double a, double b, double c, double d, double h) { // Constructor
        A = a;
        B = b;
        C = c;
        D = d;
        H = h;
    }

    double Area() { // Method overiding.
        double X = 0.5 * (A + B) * H; // Area= 0.5*(sum of parallel sides)*height.
        return X;
    }

    double Perimeter() { // Method overiding.
        double P = A + B + C + D; // Perimeter is summation of all sides.
        return P;
    }
}

class kite extends shape { // Sub class kite inherting Class shape.
    double radius;
    double A, B, C, D; // A & B store the length of two pairs of equal sides and C & D store length of
                       // 2 diagonals.

    kite(double a, double b, double c, double d) { // Constructor
        A = a;
        B = b;
        C = c;
        D = d;
    }

    double Area() { // Method overiding.
        double A = 0.5 * C * D; // Area = 0.5* Diagonal1*Diagonal2;
        return A;
    }

    double Perimeter() { // Method overiding.
        double P = 2 * A + 2 * B; // Perimeter=2(Length of pair1)+2(length of pair 2).
        return P;
    }
}

class test_shape { // main class
    public static void main(String args[]) { // main method
        circle c = new circle(10.0); // creating object of circle class
        rectangle r = new rectangle(10.0, 10.0); // creating object of rectangle class
        trapezium t = new trapezium(10.0, 12.0, 12.5, 14.8, 5.0); // creating object of trapezium class
        kite k = new kite(10.0, 15.0, 10.0, 10.0); // creating object of kite class
        System.out.println("Area and perimeter of Circle are " + c.Area() + " & " + c.Perimeter());
        System.out.println("Area and perimeter of Rectangle are " + r.Area() + " & " + r.Perimeter());
        System.out.println("Area and perimeter of Trapezium are " + t.Area() + " & " + t.Perimeter());
        System.out.println("Area and perimeter of Kite are " + k.Area() + " & " + k.Perimeter());
    }
}
