import java.awt.*;

class trygui {
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

    void create_gui() {
        Frame f = new Frame();
        f.setLayout(null);
        f.setTitle("WELCOME");
        f.setSize(400, 400);
        f.setVisible(true);

        b1 = new Button("ADD");
        b1.setBounds(100, 600, 100, 50);
        f.add(b1);

        b2 = new Button("CLOSE");
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

    }

    public static void main(String args[]) {
        trygui tg = new trygui();
        tg.create_gui();
    }
}