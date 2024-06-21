import java.util.*;

class Solution {
    public int solution(int[] arr) {
        int answer = 0;
        int[] prev = new int[arr.length];
        
        while (true) {
            System.arraycopy(arr, 0, prev, 0, arr.length);
            for (int i = 0; i < arr.length; i++) {
                if (arr[i] >= 50 && arr[i] % 2 == 0)    arr[i] /= 2;
                else if(arr[i] < 50 && arr[i] % 2 == 1) arr[i] = arr[i] * 2 + 1;
            }
            if (Arrays.equals(prev, arr))   return answer;
            answer++;
        }
    }
}