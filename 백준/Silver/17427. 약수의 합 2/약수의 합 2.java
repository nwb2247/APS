import java.io.*;
import java.math.BigInteger;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        long count = 0;
        for (int i=1; i<=N; i++) {
            count += (N/i) * i;
        }

        System.out.println(count);

        
    }
}