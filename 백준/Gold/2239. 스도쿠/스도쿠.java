import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
	
	static int[][] map;
	static List<int[]> blanks;
	static StringBuilder sb;
	static boolean[][] checkRow, checkCol, checkBox;

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		sb = new StringBuilder();
		
		map = new int[9][9];
		blanks = new ArrayList<>();
		
		checkRow = new boolean[9][9+1];
		checkCol = new boolean[9][9+1];
		checkBox = new boolean[9][9+1];
		
		for (int r=0; r<9; r++) {
			char[] chars = br.readLine().toCharArray();
			for (int c=0; c<9; c++) {
				map[r][c] = chars[c]-'0';
				if (map[r][c] != 0) {
					checkRow[r][map[r][c]] = true;
					checkCol[c][map[r][c]] = true;
					checkBox[toBox(r, c)][map[r][c]] = true;
				} else {
					blanks.add(new int[] {r,c});
				}
			}
		}
		
		if (!blanks.isEmpty()) {
			solve(0);
		} else {
			for (int r=0; r<9; r++) {
				for (int c=0; c<9; c++) {
					sb.append(map[r][c]);
				}
				sb.append("\n");
			}
			System.out.println(sb.toString());
		}
		
		
		
		

	}
	
	private static boolean solve (int cnt) {
		
		if (cnt == blanks.size()) {
			for (int r=0; r<9; r++) {
				for (int c=0; c<9; c++) {
					sb.append(map[r][c]);
				}
				sb.append("\n");
			}
			System.out.println(sb.toString());
			return true;
		}
		
		int r = blanks.get(cnt)[0];
		int c = blanks.get(cnt)[1];
		
		for (int i=1; i<=9; i++) {
			if (!isValid(r,c,i)) continue;
			map[r][c] = i;
			checkRow[r][i] = true;
			checkCol[c][i] = true;
			checkBox[toBox(r, c)][i] = true;
			
			if (solve(cnt+1)) return true;
			
			checkRow[r][i] = false;
			checkCol[c][i] = false;
			checkBox[toBox(r, c)][i] = false;
		}
		
		
		
		
		
		
		return false;
		
	}
	
	private static boolean isValid (int r, int c, int i) { 
		return !checkRow[r][i] && !checkCol[c][i] && !checkBox[toBox(r,c)][i]; 
	}
	
	private static int toBox (int r, int c) {
		return (r/3)*3+c/3;
	}

}
