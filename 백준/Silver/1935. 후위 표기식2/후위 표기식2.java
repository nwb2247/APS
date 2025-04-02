// BJ 1935 후위 표기식 2

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Stack;

public class Main {

	public static void main(String[] args) throws Exception {
		
//		System.out.println((int) 'A'); // 65
//		System.out.println((int) 'Z'); // 90
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());		
		
		char[] expression = br.readLine().toCharArray();
		HashSet<Character> operatorSet = new HashSet<>();
		operatorSet.add('+');
		operatorSet.add('-');
		operatorSet.add('*');
		operatorSet.add('/');
		
		double[] var = new double[N];
		for (int i=0; i<N; i++) {
			var[i] = Integer.parseInt(br.readLine());
		}
		
		Stack<Double> operandStack = new Stack<>();
		
		for (char c : expression) {
			if (operatorSet.contains(c)) {
				double second = operandStack.pop();
				double first = operandStack.pop();
				double retVal=0;
				switch (c) {
				case '+' :
					retVal = first + second;
					break;
				case '-' :
					retVal = first - second;
					break;
				case '*' :
					retVal = first * second;
					break;
				case '/' :
					retVal = first / second;
					break;
				}
				operandStack.add(retVal);
			} else { // c is operand
				operandStack.add(var[((int) c)-65]);
			}
		}
		
		String sol = String.format("%.2f", operandStack.pop());
		
		System.out.println(sol);
	
		
		
	}
}
