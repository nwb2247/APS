import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        // 나머지 연산 법칙 이용
        /*
            (A+B)%M = ((A%M) + (B%M)) % M 
            (A*B)%M = ((A%M) * (B%M)) % M 

         */


        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        ArrayList<Integer> arr = new ArrayList<>();

        String line;
        while((line = br.readLine()) != null) {

            if (line.isEmpty()) break;
            arr.add(Integer.parseInt(line));
        }

        

        for (int M : arr) {

            int curRemain = 1;
            int curCount = 1;   

            while (true) {
                 
                if (curRemain % M == 0) {
                    System.out.println(curCount);
                    break;
                }

                curRemain = ((((curRemain % M) * (10 % M)) % M) + (1 % M)) % M;
                curCount++;

            }
             
        }
    }
}