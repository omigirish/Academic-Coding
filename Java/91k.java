import java.util.*;

class Student {
    Scanner sc = new Scanner(System.in);
    String name;
    int roll_no, subj1, subj2, subj3, total;

    Student(int a, String str, int S1, int S2, int S3) {
        roll_no = a;
        name = str;
        subj1 = S1;
        subj2 = S2;
        subj3 = S3;
        total = get_total(S1, S2, S3);
    }

    int get_total(int a, int b, int c) {
        int t;
        t = a + b + c;
        return t;
    }

    void update_marks() {
        System.out.println("Enter marks in subject 1:");
        subj1 = sc.nextInt();
        System.out.println("Enter marks in subject 2:");
        subj2 = sc.nextInt();
        System.out.println("Enter marks in subject 3:");
        subj3 = sc.nextInt();
        total = get_total(subj1, subj2, subj3);
    }

    void display() {

        System.out.println(roll_no + "\t" + name + "\t" + subj1 + "\t" + subj2 + "\t" + subj3 + "\t" + total + "\t");

    }
}

class test {

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        Student[] s = new Student[6];
        s[0] = new Student(1, "Cesa", 95, 90, 80);
        s[1] = new Student(2, "Joey", 85, 70, 60);
        s[2] = new Student(3, "Jane", 65, 90, 70);
        s[3] = new Student(4, "Jack", 45, 50, 80);
        s[4] = new Student(5, "Jill", 65, 95, 80);
        s[5] = new Student(0, " ", 0, 0, 0);

        System.out.println("DO you wish to update any marks? y/n?");
        if (sc.next().charAt(0) == 'y') {
            System.out.println("Enter a roll no: ");
            s[(sc.nextInt()) - 1].update_marks();
        }
        for (int i = 0; i < 5; i++)
            for (int j = 0; j < 5; j++) {
                if (s[j].total < s[j + 1].total) {
                    s[5] = s[j];
                    s[j] = s[j + 1];
                    s[j + 1] = s[5];
                }
            }
        System.out.println(
                "Roll_no" + "\t" + "Name" + "\t" + "Subj1" + "\t" + "Subj2" + "\t" + "Subj3" + "\t" + "Total" + "\t");
        for (int i = 0; i < 5; i++) {
            s[i].display();

        }

    }
}