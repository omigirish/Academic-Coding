import javax.swing.*;
import java.awt.event.*;

class InvalidUserException extends Exception {
    InvalidUserException() {
        super();
    }
}

class account {
    private String username, password;

    account(String username, String password) {
        this.username = username;
        this.password = password;
    }

    String get_username() {
        return this.username;
    }

    String get_password() {
        return this.password;
    }
}

class tryGUI implements MouseListener {
    JFrame f;
    JButton b1;
    JButton b2;
    JTextField t1;
    JLabel l1;
    JLabel l2;
    JPasswordField p1;
    account[] ac = new account[5];

    void create_gui() {
        JFrame f = new JFrame();
        f.setLayout(null);
        f.setTitle("Login Page");
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setSize(400, 400);
        f.setVisible(true);

        b1 = new JButton("Login");
        b1.setBounds(100, 600, 100, 50);
        f.getContentPane().add(b1);

        b2 = new JButton("CLEAR");
        b2.setBounds(200, 600, 100, 50);
        f.getContentPane().add(b2);

        t1 = new JTextField();
        t1.setBounds(200, 100, 300, 50);
        f.getContentPane().add(t1);

        p1 = new JPasswordField();
        p1.setBounds(200, 200, 300, 50);
        f.getContentPane().add(p1);

        l1 = new JLabel("USERNAME:");
        l1.setBounds(50, 100, 100, 50);
        f.getContentPane().add(l1);

        l2 = new JLabel("PASSWORD:");
        l2.setBounds(50, 200, 100, 50);
        f.getContentPane().add(l2);

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
            login_manager();

        } else if (me.getSource() == b2) {
            clear();
        }
    }

    public void login_manager() {

        ac[0] = new account("Sushant Sawant", "SS");
        ac[1] = new account("Girish Salunke", "GS");
        ac[2] = new account("Geralt Rivia", "GR");
        ac[3] = new account("Harry Potter", "HP");
        ac[4] = new account("Mohnish Nathani", "MKN");
        String username, password;
        int found = 0;
        username = t1.getText();

        password = String.valueOf(p1.getPassword());

        for (int i = 0; i < 5; i++) {
            String u = ac[i].get_username();
            String p = ac[i].get_password();
            if (username.equals(u) && password.equals(p)) {
                JOptionPane.showMessageDialog(f, "Login Sucessfull.");
                found = 1;
                break;
            }

        }
        if (found == 0) {
            try {
                throw new InvalidUserException();
            } catch (InvalidUserException IUE) {
                JOptionPane.showMessageDialog(f, "Incorrect username or password.");
            }
        }
    }

    public void clear() {
        t1.setText("");
        p1.setText("");
    }

}

class test {

    public static void main(String[] args) {
        tryGUI tg = new tryGUI();
        tg.create_gui();
    }

}
