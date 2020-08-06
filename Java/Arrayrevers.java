import java.io.*;

class test {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] A = new char[10];
        char temp;
        for (int i = 0; i < 10; i++) {
            System.out.println("Enter a character to be stored at Index at Index:");
            A[i] = (br.readLine()).charAt(0);
        }
        for (int i = 0; i < 5; i++) {
            temp = A[i];
            A[i] = A[9 - i];
            A[9 - i] = temp;

        }
        for (int i = 0; i < 10; i++) {
            System.out.print(A[i] + " ");
        }
        System.out.println();
    }
}