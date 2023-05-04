import java.util.ArrayList;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner scan = new Scanner(System.in);
		Student_people[] student_list = new Student_people[31];
		
		
		for(int i = 0 ; i < 28 ; i++){
			int student_num = scan.nextInt();
			Student_people student = new Student_people();
			student.setHome_work("O");
			student_list[student_num] = student;
			
		}
		for(int i = 1 ; i < 31 ; i++){
			if(student_list[i] == null){
				System.out.println(i);
			}
		}
		
		
		
	}

}

class Student_people{

	private String home_work;
	
	public Student_people(){
		
	}
	
	public String getHome_work() {
		return home_work;
	}

	public void setHome_work(String home_work) {
		this.home_work = home_work;
	}
	
}
