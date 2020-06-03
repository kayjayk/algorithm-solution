import java.io.*;

public class SW6959 {
	public static void main(String args[]) throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(in.readLine());
		String s;
		char[] res = new char[T];
		
		for(int t=0; t<T; t++) {
			s = in.readLine();
			int count = 0;
			
			while(s.length()>1) {

				int a, b;
				a = Integer.parseInt(s.substring(0, 1));
				b = Integer.parseInt(s.substring(1, 2));
				
				int stringToAdd = a+b;
				
				s = stringToAdd + s.substring(2, s.length());
				count++;
			}
			if(count%2==0) res[t] = 'B';
			else res[t] = 'A';
		}
		
		for(int t=0; t<T; t++) {
			System.out.println("#"+(t+1)+" "+ res[t]);
		}
	}
}
