import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
    public static void main(String args[]) throws Exception
    {
        Scanner sc = new Scanner(System.in);
        int T;
        T=sc.nextInt();
 
        for(int test_case = 1; test_case <= T; test_case++)
        {
            int sum = 0, max = 0;
            for (int i = 0; i < 6; i++) {
                int curInt = sc.nextInt();
                sum += curInt;
                max = Math.max(max, curInt);
            }
            int sol = max + (7 - (sum + max) % 7);
            System.out.println(sol);
 
        }

        sc.close();
    }
}