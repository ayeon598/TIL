package samsung01;

public class UserSolution {
	public void playGame(int N) {
		boolean[] pairs = new boolean[2 * N];
		
	}
}

/*//첫 번째 아이디어(2.31736s)
public class UserSolution
{
   public void playGame(int N)
   {
       int[] pairs = new int[2 * N]; // 페어 여부 확인 배열
       int countPairs = 0;
       
       for (int i = 0; i < 2 * N - 1; i++) {
       	if (countPairs == N) break;
           if (pairs[i] == 1) continue; // 이미 페어를 찾은 경우 건너뜀
           
           for (int j = i + 1; j < 2 * N; j++) {
               if (pairs[j] == 1) continue; // 이미 페어를 찾은 경우 건너뜀

               if (Solution.checkCards(i, j, 0)) {
                   pairs[i] = 1;
                   pairs[j] = 1;
                   countPairs++;
                   break; // i에 대한 페어를 찾았으므로 내부 루프 종료
               }
           }
       }
   }
}*/

/*public class UserSolution {
   public void playGame(int N) {
       boolean[] used = new boolean[2 * N]; // 사용된 인덱스 체크

       for (int i = 0; i < 2 * N; i++) {
           if (used[i]) continue; // 이미 매칭된 경우 건너뜀

           for (int j = i + 1; j < 2 * N; j++) {
               if (used[j]) continue; // 이미 매칭된 경우 건너뜀

               if (Solution.checkCards(i, j, 0)) {
                   used[i] = true;
                   used[j] = true;
                   break; // i의 페어를 찾았으므로 루프 종료
               }
           }
       }
   }
}*/

/*//두 번째 아이디어 - 투 포인터(2.38963s)
import java.util.*;

public class UserSolution {
   public void playGame(int N) {
       boolean[] used = new boolean[2 * N];
       int foundPairs = 0;

       // 투 포인터로 페어 찾기
       int left = 0, right = 1;
       while (foundPairs < N) {
           if (used[left]) {
           	left++;
           	right = left + 1;
           	continue; } // 이미 찾은 카드 건너뜀
           if (used[right]) { right++; continue; } // 이미 찾은 카드 건너뜀
           
           // 두 카드의 숫자가 같다면 페어를 찾음!
           if (Solution.checkCards(left, right, 0)) {
               used[left] = true;
               used[right] = true;
               foundPairs++;
               left++;
               right = left + 1;
           } else {
               right++; // 숫자가 다르면 right 이동
           }
       }
   }
}*/

/*//세 번째 아이디어(2.74022s)
import java.util.*;

public class UserSolution {
   public void playGame(int N) {
   	List<Integer> list = new ArrayList<>();
   	for (int i=0; i<2*N; i++) {
   		list.add(i);
   	}
   	int left = 0, right = 1;
   	while (list.size()>0) {
   		int a = list.get(left);
   		int b = list.get(right);
   		if (Solution.checkCards(a, b, 0)) {
   			list.remove(right);
   			list.remove(left);
   			left = 0;
   			right = 1;
   		} else {
   			right++;
   		}
   	}
   }
}*/

/*//네 번째 아이디어(제한시간 초과-testcase 9번까지 실행됨)
import java.util.*;

public class UserSolution {
   public void playGame(int N) {
   	Map<Integer, Integer> cardMap = new HashMap<>();
		
		for (int i=0; i<2*N-1; i++) {
			if (cardMap.containsValue(i)) continue;
			int j = i+1;
			while (Solution.checkCards(i, j, 0) == false) {
				j++;
			}
			cardMap.put(i, j);
		}
   }
}*/
