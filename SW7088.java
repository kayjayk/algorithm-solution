import java.util.*;
import java.io.*;
public class SW7088 {
	public static void main(String args[]) throws IOException{
		Scanner sc = new Scanner(System.in);
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(in.readLine());
		int N, Q;
		int[][][] res = new int[T][][];
		
		for(int t=0; t<T; t++) {
			String[] s = in.readLine().split(" ");
			N = Integer.parseInt(s[0]);
			Q = Integer.parseInt(s[1]);
			res[t] = new int[Q][3];
			
			int[] cattle = new int[N];
			int[][] grades = new int[3][N];
			int[] count = new int[3];
			
			for(int i=0; i<N; i++) {
				cattle[i] = Integer.parseInt(in.readLine());
				if(cattle[i]==1) {
					count[0]++;
				}
				else if(cattle[i]==2) {
					count[1]++;
				}
				else {
					count[2]++;
				}
				
				for(int j=0; j<3; j++) {
					grades[j][i] = count[j];
				}
			}
			
			int L,R;
			
			for(int i=0; i<Q; i++) {
				s = in.readLine().split(" ");
				L = Integer.parseInt(s[0]) - 1;
				R = Integer.parseInt(s[1]) - 1;
				
				if(L==0) {
					res[t][i][0] = grades[0][R];
					res[t][i][1] = grades[1][R];
					res[t][i][2] = grades[2][R];
				}
				else {
					res[t][i][0] = grades[0][R] - grades[0][L-1];
					res[t][i][1] = grades[1][R] - grades[1][L-1];
					res[t][i][2] = grades[2][R] - grades[2][L-1];
				}

			}
		}
		
		for(int t=0; t<T; t++) {
			System.out.println("#"+(t+1));
			for(int i=0; i<res[t].length; i++) {
				for(int j=0; j<3; j++) {
					System.out.print(res[t][i][j]);
					if(j==2) break;
					System.out.print(" ");
				}
				System.out.println();
			}
		}
	}
}