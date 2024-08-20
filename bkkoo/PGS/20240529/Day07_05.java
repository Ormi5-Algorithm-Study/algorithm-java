import java.util.ArrayList;

public class Day07_05 {
    public static int[] solution(int[] arr) {
        ArrayList<Integer> list = new ArrayList<>();

        int index = 0;
        while (index < arr.length) {
            if (list.isEmpty() || list.get(list.size() - 1) < arr[index]) {
                list.add(arr[index]);
                index++;
                continue;
            }
            if (list.get(list.size() - 1) >= arr[index]) {
                list.remove(list.size() - 1);
            }
        }

        int[] stk = new int[list.size()];

        for (int i = 0; i < list.size(); i++) {
            stk[i] = list.get(i);
        }

        return stk;
    }
}
