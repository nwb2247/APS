import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Stack;

public class Main {

	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		Stack<String> operand = new Stack<>();
		Stack<String> operator = new Stack<>();
		
		String[] expression = br.readLine().split("");
		
		StringBuilder sb = new StringBuilder();
		
		for (String s : expression) {
			int ip = inputOperatorPrio(s);
			if (ip == -1) {
				operand.add(s);
			} else {
				if (s.equals(")")) {
					while (!operator.peek().equals("(")) {
						String second = operand.pop();
						String first = operand.pop();
						operand.add(first+second+operator.pop());
					}
					operator.pop(); // "("을 pop
					
				} else if (operator.isEmpty() || ip < outputOperatorPrio(operator.peek())) {
					operator.add(s);
				} else {
					while (!operator.isEmpty() && ip >= outputOperatorPrio(operator.peek())) {
						String second = operand.pop();
						String first = operand.pop();
						operand.add(first+second+operator.pop());
					}
					operator.add(s);
					
				}
			}
			
//			System.out.println(operand.toString());
//			System.out.println(operator.toString());
//			System.out.println("---------------");
		
		}
		
		while (!operator.isEmpty()) {
			String second = operand.pop();
			String first = operand.pop();
			operand.add(first+second+operator.pop());
		}
		
		System.out.println(operand.pop());
		

	}
	
	public static int inputOperatorPrio(String s) {
		int retVal;
		switch(s) {
		case ")" :
		case "(" :
			retVal = 0; // 가장 높은 우선 순위
			break;
		case "*" :
		case "/" :
			retVal = 1;
			break;
		case "+" :
		case "-" :
			retVal = 2;
			break;
		default : // operand
			retVal = -1;
		}
		
		return retVal;
	}
	
	public static int outputOperatorPrio(String s) {
		int retVal;
		switch(s) {
		case ")" :
			retVal = 0;
		case "(" :
			retVal = 3; // 가장 낮은 우선순위
			break;
		case "*" :
		case "/" :
			retVal = 1;
			break;
		case "+" :
		case "-" :
			retVal = 2;
			break;
		default : // operand
			retVal = -1;
		}
		
		return retVal;
	}

}
