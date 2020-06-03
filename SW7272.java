import java.io.*;
import java.util.*;

public class SW7272 {
	static Set<Character> AlphabetHavingOneHole = new HashSet<>();
	static char[] c = {'A', 'D', 'O', 'P', 'Q', 'R'};
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		String[] str;
		boolean isSame;
		StringBuilder sb = new StringBuilder();
		
		for(int i=0; i<c.length; i++) {
			AlphabetHavingOneHole.add(c[i]);
		}
		
		for(int t=0; t<T; t++) {
			isSame = true;
			str = br.readLine().split(" ");
			if(str[0].length()!=str[1].length()) {
				isSame = false;
			}
			else {
				for(int i=0; i<str.length; i++) {
					if(numOfHoles(str[0].charAt(i))!=numOfHoles(str[1].charAt(i))) {
						isSame = false;
						break;
					}
				}
			}
			sb.append("#"+(t+1)+" "+ (isSame ? "SAME" : "DIFF")+ "\n");
		}
		sb.delete(sb.length()-1, sb.length());
		System.out.print(sb);
	}
	static int numOfHoles(char c) {
		if(c=='B') return 2;
		else if(AlphabetHavingOneHole.contains(c)) return 1;
		else return 0;
	}
}
