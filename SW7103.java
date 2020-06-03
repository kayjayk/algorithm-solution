import java.io.*;
import java.math.*;

public class SW7103 {
	static int MAX = 32767;
	static int sqMAX = (int) Math.sqrt(32767);
	static int[] numOfSq = new int[sqMAX];
	static int[] numList = new int[MAX+1];
	static int[] limit = {90, 104, 127, 181};
	
	public static void main(String args[]) throws IOException{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(in.readLine());
		int N;
		
		int[] selectedNum = {0, 0, 0, 1};
		
		selection(selectedNum);		
		
		for(int t=0; t<T; t++) {
			N = Integer.parseInt(in.readLine());
			System.out.println("#" + (t+1) + numList[N]);
		}
	}
	
	static void selection(int[] arr) {
		if(arr[0]>90) return;
		int[] copyArr = arr.clone();
		
		for(int i=0; i<4; i++) {
			if(arr[i]>limit[i]) {
				copyArr[i-1]++;
				for(int j=i; j<4; j++) {
					copyArr[j] = copyArr[i-1];
				}
				
				selection(copyArr);
				return;
			}
		}
		
		int sum = 0;
		for(int i=0; i<4; i++) {
			sum += Math.pow(arr[i], 2);
		}
		if(sum<=MAX)
			numList[sum]++;
		
		copyArr[3] += 1;
		System.out.println(sum +", " + copyArr[3]);
		
		selection(copyArr);
	}
}
