public class Day15_01 {
    public int[] solution(int[] arr) {

        for (int i = 0; i < arr.length; i++) {
            if (arr[i]>=50 && arr[i] % 2 == 0) {
                arr[i] = arr[i] / 2;
            }
            else if(arr[i]<=50 && arr[i] % 2 == 1) {
                arr[i] = arr[i] * 2;
            }
        }
        return arr;
    }
}