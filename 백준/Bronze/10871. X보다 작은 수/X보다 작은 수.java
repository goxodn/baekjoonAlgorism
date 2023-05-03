/*
정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)

둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.

출력
X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. X보다 작은 수는 적어도 하나 존재한다.
*/

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main{
    public static void main(String args[]){
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringTokenizer st2;
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        try{
            
            st2 = new StringTokenizer(br.readLine());

            int N = Integer.parseInt(st2.nextToken());
            int X = Integer.parseInt(st2.nextToken());
            
            st = new StringTokenizer(br.readLine());
            
            for(int i=0;i<N;i++){
            	int a = Integer.parseInt(st.nextToken());
                if(a<X){
                    bw.write(a+" ");
                }
            }
            bw.flush();
            
        }catch(IOException e){
            e.printStackTrace();
        }
        
    }
}


