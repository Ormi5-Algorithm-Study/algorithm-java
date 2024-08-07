import sys
input = sys.stdin.readline
n = int(input())
p = list(map(int, input().split()))
p.sort()
tmp = 0
answer = 0
for i in p:
    tmp += i
    answer += tmp
print(answer)

"""
import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] p = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0; i<n; i++){
            p[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(p);
        int tmp = 0;
        int answer = 0;
        for(int time: p){
            tmp += time;
            answer += tmp;
        }
        br.close();
        System.out.println(answer);
    }
}
"""
