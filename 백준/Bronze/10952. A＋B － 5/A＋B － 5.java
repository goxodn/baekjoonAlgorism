import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args){
	
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		Scanner in = new Scanner(System.in);
		while(true){
			try{
				st = new StringTokenizer(in.nextLine());
				int A = Integer.parseInt(st.nextToken());
				int B = Integer.parseInt(st.nextToken());
				if(A==0&&B==0) break;
				int sum = A+B;
				bw.write(sum+"\n");
				bw.flush();
			}catch(Exception e){
				
			}
		}
	
	}

}
