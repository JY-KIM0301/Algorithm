package programmers;

import java.util.*;

/* 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다.
 * 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다. 
 * 단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다.
 * arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다. */

public class P같은숫자는싫어 {
    public int[] solution(int []arr) {
    	ArrayList<Integer> list = new ArrayList<Integer>(); // int타입 ArrayList 선언
    	
    	int preNum = 10;
    	for(int num : arr) {
    		if(preNum != num)
    			list.add(num); // list에 num추가 
    		preNum = num;
    	}
    	int[] answer = new int[list.size()]; // size() -> list의 크기 반환
    	for(int i=0; i<answer.length; i++) {
    		answer[i] = list.get(i).intValue(); // intValue() -> Integer 객체에서 int타입 값을 뽑아내는 메소드
    	}
        return answer;
    }
    
	/*
	 * forEach문을 돌면서 preNum 변수를 생성하고 이전 인덱스의 값을 preNum에 저장해 
	 * 다음 인덱스와 비교하면 간단하게 해결할 수 있다
	 */
}
