import sys
input = sys.stdin.readline
n = int(input())
arr = [ [0 for _ in range(100)] for _ in range(100)]
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1 # 넓이에 해당하는 좌표는 1
result = 0
for i in range(100):
    result += arr[i].count(1) #1의 총 개수 = 넓이
print(result)

"""
import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st;
        int[][] arr = new int[100][100];
        while(n>0){
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            for(int i = x; i<x+10; i++){
                for(int j=y; j<y+10; j++){
                    arr[i][j] = 1;
                }
            }
            n--;
        }
        //1의 개수
        int answer = 0;
        for(int i=0; i<100; i++){
            for(int j=0; j<100; j++){
                if(arr[i][j]==1) answer++;
            }
        }
        System.out.println(answer);
    }
}
"""
