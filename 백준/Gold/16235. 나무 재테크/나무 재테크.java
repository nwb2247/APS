import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		// 남아 있는 양분
		int[][] map = new int[N+1][N+1]; // r,c 1부터 시작;
		for (int r=1; r<=N; r++) {
			for (int c=1; c<=N; c++) {
				map[r][c] = 5; // 5로 초기화
			}
		}
		
		// 매년 겨울 주는 양분
		int[][] A = new int[N+1][N+1];
		
		for (int r=1; r<=N; r++) {
			st = new StringTokenizer(br.readLine());
			for (int c=1; c<=N; c++) {
				A[r][c] = Integer.parseInt(st.nextToken());
			}
		}
		
		// 각 구역의 나무 / 제네릭으로는 배열 생성 불가
		ArrayList<ArrayList<ArrayList<Integer>>> tree = new ArrayList<>();
		for (int r=0; r<=N; r++) {
			tree.add(new ArrayList<>());
			for (int c=0; c<=N; c++) {
				tree.get(r).add(new ArrayList<>());
			}
		}
		
		for (int i=0; i<M; i++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			int old = Integer.parseInt(st.nextToken());
			tree.get(x).get(y).add(old);
		}
		
		for (int r=0; r<=N; r++) {
			for (int c=0; c<=N; c++) {
				tree.get(r).get(c).sort(Comparator.naturalOrder());
			}
		}
		
		int[] dr = {-1,-1,-1,0,0,1,1,1};
		int[] dc = {-1,0,1,-1,1,-1,0,1};		
		
		while (K>0) {
			
			// 봄, 여름
			for (int r=1; r<=N; r++) {
				for (int c=1; c<=N; c++) {
					
					// 봄
					ArrayList<Integer> curList = tree.get(r).get(c);
					int dead = 0;
					boolean[] deadIdxs = new boolean[curList.size()];
					for (int i=0; i<curList.size(); i++) {
						int old = curList.get(i);
						if (old <= map[r][c]) {
							map[r][c] -= old;
							curList.set(i, old+1);
						} else {
							deadIdxs[i] = true;
							dead += old/2;
						}
					}
					for (int i=curList.size()-1; i>=0; i--) { // 잘못된 인덱스룰 삭제하는 것을 방지하기 위해 역순 순회
						if (deadIdxs[i]) {
							curList.remove(i);
						}
					}
					
					// 여름
					map[r][c] += dead;			
					
				}
			}
			
			// 가을, 겨울
			for (int r=1; r<=N; r++) {
				for (int c=1; c<=N; c++) {
					
					// 가을
					ArrayList<Integer> curList = tree.get(r).get(c);
					
					for (int i=0; i<curList.size(); i++) {
						int old = curList.get(i);
						if (old%5 == 0) {
							for (int d=0; d<8; d++) {
								int nr = r+dr[d];
								int nc = c+dc[d];
								if (nr<=N && nr>=1 && nc<=N && nc>=1) {
									tree.get(nr).get(nc).add(0, 1);
								}
							}
						}
					}
					
					// 겨울
					map[r][c] += A[r][c];			
					
				}
			}
			
			K--;
		}
		
		// 나무 갯수 카운트;
		int cnt = 0;
		for (int r=1; r<=N; r++) {
			for (int c=1; c<=N; c++) {
				cnt += tree.get(r).get(c).size();
			}
		}
		
		System.out.println(cnt);
		

	}

}
