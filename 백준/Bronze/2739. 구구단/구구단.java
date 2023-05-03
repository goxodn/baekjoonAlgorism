import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner user_input = new Scanner(System.in);
		
		int multiplecation_number = user_input.nextInt();
		
		for(int i = 1 ; i < 10 ; i ++){
			System.out.println(multiplecation_number + " * " + i + " = " + (multiplecation_number * i));
		}
	}
}
