import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static class Node {
		char val;
		Node prev, next;
	}
	
	static class LinkedList {
		
		Node head;
		
		public LinkedList() {
			head = new Node();
			/*
			 * head는 dummy node로서, 값을 갖지 않는다.
			 * 빈 연결리스트를 쉽게 처리하기 위해 dummy Node를 사용한다.
			 * prev값으로 null을 갖는 경우 그 Node는 head이다.
			 * 빈 연결리스트의 경우 head Node만을 갖는다.
			 */
			 
			head.val = ' ';
			head.prev = null;
			head.next = null;
		}
		
		public Node getHead() {
			return head;
		}
		
		public Node add(Node curNode, char val) {
			
			// 1. 새로운 노드 생성
			Node newNode = new Node();
			newNode.val = val;
			
			// 2. 기존의 curNode.next 참조 기억
			Node nextNode = curNode.next;
			
			// 3. 새로운 노드의 prev, next 값 설정
			newNode.prev = curNode;
			newNode.next = nextNode;
			
			// 4. curNode.next, nextNode.prev 설정
			curNode.next = newNode;
			if (nextNode != null) nextNode.prev = newNode; // 마지막 원소 다음에 추가한 경우, 이 라인은 실행 X
			
			return newNode;
		}
		
		public Node remove(Node curNode) {
			
			// 1. 이전 노드 참조 저장
			Node prevNode = curNode.prev;
			if (prevNode == null) return curNode;
			// 맨 앞 커서면 아무것도 삭제하지 않고, 원래 노드 반환
			
			// 2. 다음 노드 참조 저장
			Node nextNode = curNode.next;
			
			// 3. prevNode.next, nextNode.prev 설정
			prevNode.next = nextNode;
			// head(dummy node)의 존재로 인해 
			// (head 자체를 remove하는게 아닌 이상) prevNode.next가 항상 null 아님이 보장됨
			if (nextNode != null) nextNode.prev = prevNode;
			return prevNode;
		}
		
		public Node L(Node curNode) {
			if (curNode.prev != null) curNode = curNode.prev;
			return curNode;
		}
		
		public Node D(Node curNode) {
			if (curNode.next != null) curNode = curNode.next;
			return curNode;
		}
		
		public String traverse() {
			// head부터 모든 노드 순회하면서 출력
			StringBuilder sb = new StringBuilder();
			Node curNode = head.next;
			while (curNode != null) {
				sb.append(curNode.val);
				curNode = curNode.next;
			}
			return sb.toString();
		}
		
	}
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		char[] chars = br.readLine().toCharArray();
		
		LinkedList ll = new LinkedList();
		Node cursor = ll.getHead();
		for (char c : chars) {
			cursor = ll.add(cursor, c);
		}
		
		int M = Integer.parseInt(br.readLine());
		StringTokenizer st;
		for (int i=0; i<M; i++) {
			st = new StringTokenizer(br.readLine());
			String op = st.nextToken();
			if (op.equals("L")) {
				cursor = ll.L(cursor);
			} else if (op.equals("D")) {
				cursor = ll.D(cursor);
			} else if (op.equals("B")) {
				cursor = ll.remove(cursor);
			} else {
				cursor = ll.add(cursor, st.nextToken().toCharArray()[0]);
			}
//			System.out.println(ll.traverse());
		}
		
		System.out.println(ll.traverse());
		
	}
}