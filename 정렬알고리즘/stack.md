# 스택(Stack) 이란?

모든 작업이 리스트의 한 쪽 끝에서만 수행되는 선형 리스트의 한 형태.  
리스트의 한 쪽 끝(TOP)에서 원소를 삽입하거나 제거하는데 사용한다. 그러므로 리스트에서 Stack에 마지막으로 입력된 원소가 제일 먼저 제거의 대상이 됨.  
Stack을 LIFO (Last in First Out) 라고도 부른다

## 스택 예제
```
문제: 주어진 StackTest클래스가 정상적으로 실행되기 위해 MyStack 클래스를 구현
하시오.

<MyStack 클래스에 대한 요구조건>
1. MyStack클래스는 기본생성자로 생성하면 int 타입의 정수를 10개만 저장하는 Stack 클
래스이다.  
2. 객체 생성 시 생성자 매개변수로 배열의 크기를 지정할 수 있으나 음수가 매개변수로
들어올 경우는 기본적으로 10개의 정수를 저장하도록 한다.
3. push() 메서드로 Stack에 정수를 저장한다.
4. isEmpty() 메서드로 Stack이 비어있는지 확인할 수 있다.
5. ifFull() 메서드로 Stack이 가득찼는지 확인할 수 있다.
6. top() 메서드로 Stack에서 최상위에 저장된 숫자가 뭔지 알 수 있다. top() 메서드를
호출했다고 해서 숫자가 삭제되는 것은 아니다. 꺼낼 숫자가 없는 경우 -1을 리턴한다.
7. pop() 메서드로 Stack에서 최상위에 저장된 숫자를 꺼낼 수 있다. 스택에서 숫자를 꺼
내면 그 숫자는 Stack에서 삭제된다. 꺼낼 숫자가 없는 경우 -1을 리턴한다.
8. java.util.Stack class는 사용하지 않는다.
```

## 정답 소스  
```java
import java.util.Stack;

public class Prob7_Stack_Answer {
	public static void main(String[] args) {
		Stack<Integer> s = new Stack<Integer>();
		
		MyStack2 stack = new MyStack2(10);
		if(stack.isEmpty()){
			System.out.println("스택이 비어있습니다.");
		}
		
		for (int i = 1; i <= 10; i++) {
			stack.push(i);
		}
		
		if(stack.isFull()){
			System.out.println("스택이 가득 찼습니다.");
		}
		
		System.out.println("최상위 숫자 : " + stack.peek());
		System.out.println("최상위에서 꺼낸 숫자 : " + stack.pop());
		System.out.println("최상위에서 꺼낸 숫자 : " + stack.pop());
		System.out.println("");
		System.out.println("== 스택 리스트 ==");
		for (int i = 1; i <= 10; i++) {
			int num = stack.pop();
			if(num != -1)
				System.out.println(num);
		}
		for (int i = 1; i <= 100; i++) {
			stack.push(i);
		}
	}
}

class MyStack2{
	int[] stack;
    int count = 0;
    
	public MyStack2() {
		stack = new int[10];
	}
	
	public MyStack2(int size) {
		stack = new int[size>0?size:10];
	} 
	
	public boolean isEmpty() {
		return count==0 ? true: false;
	}
	
	public boolean isFull() {
		return count==stack.length? true: false;
	}
	
	public void push(int i) {
		if(isFull()) {
			int[] temp = new int[stack.length*2];
			System.arraycopy(stack, 0, temp, 0, stack.length);
			stack = temp;
			temp = null;
		}else {
			stack[count++] = i;
		}
	}
	public int peek() {
		return  count==0?-1:stack[count-1];
	}
	public int pop() {
		int data = -1;
		if(!isEmpty()) {
          data = stack[count-1];
          stack[count-1] = 0;
          count--;
		}
		return data;
	}
	
}
// 출력결과
스택이 비어있습니다.
스택이 가득 찼습니다.
최상위 숫자 : 10
최상위에서 꺼낸 숫자 : 10
최상위에서 꺼낸 숫자 : 9

== 스택 리스트 ==
8
7
6
5
4
3
2
1
```
스택은 자바에서 stack API로 만들수 있다. 나는 api사용없이 구글링해서 구현했지만 ㅎ..  boolean형을 쓰긴 썼지만 활용을 잘 못했던것 같다.  

정답에서는 먼저 생성자 안에 `stack = new int[10];` 으로 스택을 만들어주고 `count`라는 변수를 두어 `count`가 0이면 스택이 비어있고, 아니면 차있다는 의미로 사용했다.  `isFull()` 메소드에서는 `count==stack.legth ? true: false;` 와 같이 삼항연산자를 이용해서 count가 스택의 길이와 같으면 가득 차있는것이고, 아니면 공간이 남아있는것으로 표현했다.  

가장 최상위값을 뽑아내는 `peek()`메소드에서는 count가 0이면 비어있으므로 -1를 반환하고 가득 차있다면, 가장 상위의 값을 도출하기 위해 `stack[count-1]`로 스택 배열의 가장 마지막 위치에 있는 숫자를 출력하도록 구현했다.  
