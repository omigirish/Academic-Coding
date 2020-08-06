import java.io.*;

class student { // Class for students (Superclass)
    private int roll_no; // Class variables
    private String name;

    public void setName(String name) { // Implementin setter methods
        this.name = name;
    }

    public void setRoll_no(int roll_no) {
        this.roll_no = roll_no;
    }

    public String getName() { // implementing getter methods.
        return name;
    }

    public int getRoll_no() {
        return roll_no;
    }

}

interface NSS { // declarin interface NSS
    final float weightage = 0.1f; // The fixed weightage for nss is 10%.

    public void get_weightage();
}

class test_marks extends student implements NSS { // Subclass test marks inheriting Superclass Student And inheriting
                                                  // interface NSS
    private int m1, m2, m3; // Sub class variables for storing marks.

    public void setM1(int m1) { // Implementing Setter methods
        this.m1 = m1;
    }

    public void setM2(int m2) {
        this.m2 = m2;
    }

    public void setM3(int m3) {
        this.m3 = m3;
    }

    public int getM1() { // Implementing Getter methods
        return m1;
    }

    public int getM2() {
        return m2;
    }

    public int getM3() {
        return m3;
    }

    int get_sub_total() { // method for calculating total
        return (m1 + m2 + m3);
    }

    public void get_weightage() { // Implementation of Interface method.
        float weight = weightage;
    }

    float get_NSS_Marks() { // Method to calculate marks weightage of NSS
        return (NSS.weightage * get_sub_total());
    }

    float get_total() { // Method to add total and NSS marks.
        return (get_sub_total() + get_NSS_Marks());
    }
}

class result { // Main Class
    public static void main(String[] args) throws IOException { // Main method
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // Creating object of Buffered reader
                                                                                  // class.
        test_marks[] tm = new test_marks[3]; // Creating array of objects of test_marks Class.
        for (int i = 0; i < 3; i++) { // for loop to feed data in objects
            tm[i] = new test_marks();
            tm[i].setRoll_no((i + 1));
            System.out.println("Enter name of student: ");
            tm[i].setName(br.readLine());
            System.out.println("Enter the marks in Subject 1: ");
            tm[i].setM1(Integer.parseInt(br.readLine()));
            System.out.println("Enter the marks in Subject 2: ");
            tm[i].setM2(Integer.parseInt(br.readLine()));
            System.out.println("Enter the marks in Subject 3: ");
            tm[i].setM3(Integer.parseInt(br.readLine()));
        }
        for (int i = 0; i < 3; i++) { // for loop to get data from objects.
            System.out.println("Result of Roll NO." + (i + 1));
            System.out.println("Name:" + tm[i].getName());
            System.out.println("Marks in subject 1: " + tm[i].getM1());
            System.out.println("Marks in subject 2: " + tm[i].getM2());
            System.out.println("Marks in subject 3: " + tm[i].getM3());
            System.out.println("Sub total: " + tm[i].get_sub_total());
            System.out.println("Final marks(Adding NSS Weightage): " + tm[i].get_total());
            System.out.println();

        }
    }
}
