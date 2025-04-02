// BJ 17425
// int 대신 long 사용해야 오버플로우 안뜸

import java.io.*;
import java.math.BigInteger;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 테스트 케이스 입력
        int T = Integer.parseInt(br.readLine());
        
        int[] arr_N = new int[T];
        int MaxN = 0;
        for (int t=0; t<T; t++) {
            arr_N[t] = Integer.parseInt(br.readLine());            
            MaxN = Math.max(MaxN, arr_N[t]);
        }
        
	    
	    long[] sum = new long[MaxN+1];
	    for (int i=1; i<=MaxN; i++) {
	    	for (int j=i; j<=MaxN; j += i) { // i : 약수 / j : i의 배수
	    		sum[j] += i;
	    	}
	    }
	    
	    for (int i=1; i<=MaxN; i++) {
	    	sum[i] += sum[i-1];
	    }
	    
	    // 출력줄이 긴 경우, sb를 사용하는 것이 훨씬 빠름
	    StringBuilder sb = new StringBuilder();	    
	    
	    for (int t=0; t<T; t++) {
	    	sb.append(sum[arr_N[t]] + "\n");
	    }
		  
	    System.out.println(sb);

        
    }

            /* 참고
         Collection 클래스 : 자바의 다양한 컬렉션(리스트, 맵, 세트) 자료구조조의 최상위 인터페이스 (즉, 리스트 맵 세트 등은 collection의 상속 클래스임) (add, remove, size 등 메서드)
         Collections 클래스 : Collection을 상속받는 자료구조의 유틸리티 메서드 (sort, reverse, shuffle 등)
         */
}