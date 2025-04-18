import java.io.*;
import java.util.*;

public class Main {

    static class Node implements Comparable<Node> {
        int end;
        long dist;

        public Node(int end, long dist) {
            this.end = end;
            this.dist = dist;
        }

        @Override
        public int compareTo(Node o) {
            return Long.compare(this.dist, o.dist);
        }
    }

    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken()); // 정점 수
        int M = Integer.parseInt(st.nextToken()); // 간선 수
        int K = Integer.parseInt(st.nextToken()); // 목적지 수

        // 역방향 그래프 만들기
        ArrayList<ArrayList<Node>> reverseGraph = new ArrayList<>();
        for (int i = 0; i <= N; i++) {
            reverseGraph.add(new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());

            reverseGraph.get(e).add(new Node(s, d)); // 역방향 간선
        }

        // 목적지 배열
        st = new StringTokenizer(br.readLine());
        PriorityQueue<Node> pq = new PriorityQueue<>();
        long[] dist = new long[N + 1];
        Arrays.fill(dist, Long.MAX_VALUE / 2);

        while (st.hasMoreTokens()) {
            int dest = Integer.parseInt(st.nextToken());
            dist[dest] = 0;
            pq.offer(new Node(dest, 0)); // 목적지를 시작점으로 큐에 넣음
        }

        // 다익스트라
        boolean[] visited = new boolean[N + 1];
        while (!pq.isEmpty()) {
            Node cur = pq.poll();

            if (visited[cur.end]) continue;
            visited[cur.end] = true;

            for (Node next : reverseGraph.get(cur.end)) {
                if (dist[next.end] > dist[cur.end] + next.dist) {
                    dist[next.end] = dist[cur.end] + next.dist;
                    pq.offer(new Node(next.end, dist[next.end]));
                }
            }
        }

        // 가장 먼 노드 찾기
        int num = 0;
        long max = 0;

        for (int i = 1; i <= N; i++) {
            if (dist[i] > max) {
                max = dist[i];
                num = i;
            }
        }

        System.out.println(num);
        System.out.println(max);
    }
}
