import java.awt.*;
import java.awt.event.*;

class student {
    String name;
    int roll_no, marks1, marks2;

    student(String name, int roll_no, int marks1, int marks2) {
        this.name = name;
        this.roll_no = roll_no;
        this.marks1 = marks1;
        this.marks2 = marks2;

    }

    public String get_name() {
        return this.name;
    }

    public int get_roll_no() {
        return this.roll_no;
    }

    public int get_marks1() {
        return this.marks1;
    }

    public int get_marks2() {
        return this.marks2;
    }
}

class trygui implements MouseListener {
    Frame f;
    Button b1;
    Button b2;
    TextField t1;
    TextField t2;
    TextField t3;
    TextField t4;
    Label l1;
    Label l2;
    Label l3;
    Label l4;
    int i = 0;
    student[] st = new student[50];

    void create_gui() {
        Frame f = new Frame();
        f.setLayout(null);
        f.setTitle("Student Registration Form.");
        f.setSize(400, 400);
        f.setVisible(true);

        b1 = new Button("ADD");
        b1.setBounds(100, 600, 100, 50);
        f.add(b1);

        b2 = new Button("CLEAR");
        b2.setBounds(200, 600, 100, 50);
        f.add(b2);

        t1 = new TextField();
        t1.setBounds(200, 100, 300, 50);
        f.add(t1);

        t2 = new TextField();
        t2.setBounds(200, 200, 100, 50);
        f.add(t2);

        t3 = new TextField();
        t3.setBounds(200, 300, 100, 50);
        f.add(t3);

        t4 = new TextField();
        t4.setBounds(200, 400, 100, 50);
        f.add(t4);

        l1 = new Label("NAME");
        l1.setBounds(50, 100, 100, 50);
        f.add(l1);

        l2 = new Label("ROLL_NO");
        l2.setBounds(50, 200, 100, 50);
        f.add(l2);

        l3 = new Label("MARKS1");
        l3.setBounds(50, 300, 100, 50);
        f.add(l3);

        l4 = new Label("MARKS2");
        l4.setBounds(50, 400, 100, 50);
        f.add(l4);

        b1.addMouseListener(this);
        b2.addMouseListener(this);

    }

    public void mousePressed(MouseEvent me) {
    }

    public void mouseReleased(MouseEvent me) {
    }

    public void mouseEntered(MouseEvent me) {
    }

    public void mouseExited(MouseEvent me) {
    }

    public void mouseClicked(MouseEvent me) {

        if (me.getSource() == b1) {
            add_new_student(i);
            i++;
        } else if (me.getSource() == b2) {
            clear();
        }
    }

    public void add_new_student(int i) {
        int roll_no;
        int m1, m2;
        String name;
        roll_no = Integer.parseInt(t2.getText());
        name = t1.getText();
        m1 = Integer.parseInt(t3.getText());
        m2 = Integer.parseInt(t4.getText());
        st[i] = new student(name, roll_no, m1, m2);
        System.out.println("Student " + st[i].get_name() + " with roll no: " + st[i].get_roll_no() + " has scored "
                + st[i].get_marks1() + "in subject1 & " + st[i].get_marks2() + " in subject2");
    }

    public void clear() {
        t1.setText("");
        t2.setText("");
        t3.setText("");
        t4.setText("");
    }

    public static void main(String args[]) {
        trygui tg = new trygui();
        tg.create_gui();

    }
}
