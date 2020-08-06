import java.awt.*;
import java.awt.event.*;

public class Gui2
{
 Frame f;
 TextField t1,t2;
 Label l3,l4;
 Button b1,b2;
 Gui2()
 {
  f=new Frame();

  Label l1=new Label("A : ");
  l1.setBounds(50,50,20,40);
  Label l2=new Label("B : ");
  l2.setBounds(50,100,20,40);

  t1=new TextField();
  t1.setBounds(70,60,80,20);
  t2=new TextField();
  t2.setBounds(70,110,80,20);

  b1=new Button("Add");
  b1.setBounds(145,160,80,40);
  b1.addActionListener(new MyListenerAdd());

  b2=new Button("Multiply");
  b2.setBounds(240,160,80,40);
  b2.addActionListener(new MyListenerMult());

  f.add(l1);
  f.add(l2);
  f.add(t1);
  f.add(t2);
  f.add(b1);
  f.add(b2);

  f.addWindowListener(new WindowAdapter(){
   public void windowClosing(WindowEvent ag){
  System.exit(0);
}
});
  f.setTitle("calculator");
  f.setSize(500,500);
  f.setLayout(null);
  f.setBackground(Color.yellow);
  f.setVisible(true);
 }
 class MyListenerAdd implements ActionListener
 {
  public void actionPerformed(ActionEvent ae)
  {
   double a=Double.parseDouble(t1.getText());
   double b=Double.parseDouble(t2.getText());
   l3=new Label("The result of add is "+(a+b));
   l3.setBounds(50,220,300,40);
   f.add(l3);
  }
 }
 class MyListenerMult implements ActionListener
 {
  public void actionPerformed(ActionEvent ae)
  {
   double a=Double.parseDouble(t1.getText());
   double b=Double.parseDouble(t2.getText());
   l4=new Label("The result of mult is "+(a*b));
   l4.setBounds(50,250,300,40);
   f.add(l4);
  }
 }
 public static void main(String[] args)
 {
  Gui2 g=new Gui2();
 }
}