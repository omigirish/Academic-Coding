import java.io.*;
import java.net.*;
class UDPServer
{
   public static void main(String args[]) throws Exception
      {
	int count=0 ,i=0;
	         String Sentence;

         DatagramSocket serverSocket = new DatagramSocket(9876);
            byte[] receiveData = new byte[1024];
            byte[] sendData = new byte[1024];
            while(true)
               {
                     i=0;count=0;
                  DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
                  serverSocket.receive(receivePacket);
                  Sentence= new String( receivePacket.getData());
              
            System.out.println("Received:\n " + Sentence);
            
                  InetAddress IPAddress = receivePacket.getAddress();
                  int port = receivePacket.getPort();
                  i=0;
                  while(Sentence.charAt(i)!='\0')
                  {
                  if(Sentence.charAt(i)=='a' || Sentence.charAt(i)=='e' || Sentence.charAt(i)=='i'|| Sentence.charAt(i)=='o'|| Sentence.charAt(i)=='u' || Sentence.charAt(i)=='A' || Sentence.charAt(i)=='E' || Sentence.charAt(i)=='I'|| Sentence.charAt(i)=='O'||Sentence.charAt(i)=='U')
                  {
                  count++;
                  }
                  i++;
                  }
System.out.println("no of consonents are:" + (i-count));
int ans=i-count;

                              Sentence=Integer.toString(ans);
                  sendData = Sentence.getBytes();
                  DatagramPacket sendPacket =new DatagramPacket(sendData, sendData.length, IPAddress, port);
                  serverSocket.send(sendPacket);
                
                              
                                             }
      }
}


