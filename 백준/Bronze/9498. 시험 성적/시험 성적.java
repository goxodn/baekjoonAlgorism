import java.util.Scanner;
class Main{
	public static void main(String args[]) {
		Scanner in = new Scanner(System.in);
		String hakjum;
		int score = in.nextInt();

		if (score >= 90)
			hakjum = "A";
		else if (score >= 80)
			hakjum = "B";
		else if (score >= 70)
			hakjum = "C";
		else if (score >= 60)
			hakjum = "D";
		else
			hakjum = "F";
		
		System.out.println(hakjum);
	}
}