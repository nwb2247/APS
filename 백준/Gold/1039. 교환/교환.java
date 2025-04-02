// 백준 1039

import java.io.*;
import java.util.*;

class Main
{
	public static void main(String args[]) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] input = br.readLine().split(" ");
		
		// BFS를 위한 큐 (숫자 문자열, 연산 횟수를 저장)
		String N = input[0];
		int length = N.length();
		int K = Integer.parseInt(input[1]);
		
		// 방문상태 저장
		HashSet<Pair> visited = new HashSet<>();
		
		int maxVal = -1;
		
		Queue<Pair> queue = new LinkedList<>(); // Queue 인터페이스를 LL로 구현했다는 의미
		queue.add(new Pair(N, 0));
		
		// BFS
		while (!queue.isEmpty()) {
			Pair curPair = queue.poll();
			// remove : return head with removing/ raise error if empty
			// poll : return head with removing / return null if empty
			// element : return head without removing / raise error if empty
			// peek : return head without removing / return null if empty
			
			// count가 K라면 max 갱신
			if (curPair.count == K) {
				maxVal = Math.max(maxVal, Integer.parseInt(curPair.N));
				continue;
			}
			
			
			// K가 아니라면 swap 진행
			for (int i=0; i<length-1; i++) {
				for (int j=i+1; j<length; j++) {
					char[] chars = curPair.N.toCharArray();
					char temp = chars[i];
					chars[i] = chars[j];
					chars[j] = temp;
					
					
					if (chars[0] == '0') continue; // 맨 앞자리가 0 이라면 무효, 다음 스왑을 생각함
					String newN = new String(chars); // char array를 String()을 통해 형변환 가능
					
					Pair newPair = new Pair(newN, curPair.count + 1);
					if (!visited.contains(newPair)) {
						visited.add(newPair);
						queue.add(newPair);
					}

				}
			}
		}
		
		System.out.println(maxVal);
		
	}
	
	static class Pair { // Pair는 최상위 클래스(Main)의 인스턴스에 종속되지 않으므로 static으로 구현
		String N;
		int count;
		
		Pair(String N, int count) {
			this.N = N;
			this.count = count;
		}
		
		// HashSet 동작 방식
		// obj의 해시코드를 구해서 동일한 해시 코드가 있는 객체를 찾고 => 해시 코드가 동일한 경우 equals를 통해 객체가 동등한지 확인
		// 즉 equals()가 true를 반환하면, 두 객체의 hashCode()가 동일한 해시값을 갖도록 구현해야한다.
		// equals()와 hashCode()는 항상 함께 구현해야 한다.
		
		@Override
		public boolean equals(Object obj) {
			if (this == obj) return true; // 같은 객체
			if (obj == null || getClass() != obj.getClass()) return false; // null이거나 다른 class라면 false
			
			// (Pair)로 캐스팅하는 이유 :
			// equals()는 기본적으로 Object라는 class에서 정의된 메소드를 오버라이딩한것이다.
			// 따라서 파라미터로 들어온 obj를 Pair로 형변환해야 비교가 가능하다.			
			Pair objToPair = (Pair) obj;

			// N는 String(Object의 상속)이므로 Objects.equals()로 비교
			// count는 int(기본자료형)이므로 ==로 비교
			return Objects.equals(this.N, objToPair.N) && this.count == objToPair.count;
		}
		
		@Override
		public int hashCode() {
			return Objects.hash(N, count);
		}
		
	}
}