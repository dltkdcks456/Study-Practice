import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb;
	static int N, M, option, left, right, k;
	static int[] arr, seg, lazy;
	
	public static void main(String[] args) throws IOException {
		N = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		arr = new int[N];
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		int l = 0, tmp = 1;
		while(tmp < N) {
			tmp <<= 1;
			l++;
		}
		seg = new int[(int) Math.pow(2, l + 1)];
		lazy = new int[(int) Math.pow(2, l + 1)];
		
		initSeg(1, 0, N - 1);
		
		M = Integer.parseInt(br.readLine());
		sb = new StringBuilder();
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			option = Integer.parseInt(st.nextToken());
			if (option == 1) {
				left = Integer.parseInt(st.nextToken());
				right = Integer.parseInt(st.nextToken());
				k = Integer.parseInt(st.nextToken());
				updateSeg(1, 0, N - 1, left, right, k);
			} else {
				left = Integer.parseInt(st.nextToken());
				right = Integer.parseInt(st.nextToken());
				sb.append(findSeg(1, 0, N - 1, left, right)).append('\n');
			}
		}
		System.out.println(sb);
	}
	
	static int initSeg(int treeIdx, int leftIdx, int rightIdx) {
		if (leftIdx == rightIdx) {
			seg[treeIdx] = arr[leftIdx];
			return seg[treeIdx];
		}
		int midIdx = (leftIdx + rightIdx) / 2;
		int leftV = initSeg(treeIdx * 2, leftIdx, midIdx);
		int rightV = initSeg(treeIdx * 2 + 1, midIdx + 1, rightIdx);
		seg[treeIdx] = leftV ^ rightV;
		return seg[treeIdx];
	}
	
	static int findSeg(int treeIdx, int leftIdx, int rightIdx, int findLeftIdx, int findRightIdx) {
		propagate(treeIdx, leftIdx, rightIdx);
		if (leftIdx > findRightIdx || rightIdx < findLeftIdx) {
			return -1;
		}
		if (leftIdx >= findLeftIdx && rightIdx <= findRightIdx) {
			return seg[treeIdx];
		}
		int midIdx = (leftIdx + rightIdx) / 2;
		int leftV = findSeg(treeIdx * 2, leftIdx, midIdx, findLeftIdx, findRightIdx);
		int rightV = findSeg(treeIdx * 2 + 1, midIdx + 1, rightIdx, findLeftIdx, findRightIdx);
		if (leftV == -1 && rightV == -1) {
			return -1;
		} else if(leftV == -1) {
			return rightV;
		} else if (rightV == -1) {
			return leftV;
		} else {
			return leftV ^ rightV;
		}
	}
	
	static void updateSeg(int treeIdx, int leftIdx, int rightIdx, int updateLeftIdx, int updateRightIdx, int value) {
		propagate(treeIdx, leftIdx, rightIdx);
		if (leftIdx > updateRightIdx || rightIdx < updateLeftIdx) {
			return;
		}
		if (leftIdx >= updateLeftIdx && rightIdx <= updateRightIdx) {
			lazy[treeIdx] = value;
			propagate(treeIdx, leftIdx, rightIdx);
			return;
		}
		int midIdx = (leftIdx + rightIdx) / 2;
		updateSeg(treeIdx * 2, leftIdx, midIdx, updateLeftIdx, updateRightIdx, value);
		updateSeg(treeIdx * 2 + 1, midIdx + 1, rightIdx, updateLeftIdx, updateRightIdx, value);
		
		seg[treeIdx] = seg[treeIdx * 2] ^ seg[treeIdx * 2 + 1];
	}
	
	static void propagate(int treeIdx, int leftIdx, int rightIdx) {
		if (lazy[treeIdx] > 0) {
			if (leftIdx != rightIdx) {
				lazy[treeIdx * 2] ^= lazy[treeIdx];
				lazy[treeIdx * 2 + 1] ^= lazy[treeIdx];
			}
			int roopCnt = rightIdx - leftIdx + 1;
			if (roopCnt % 2 == 1) {
				seg[treeIdx] ^= lazy[treeIdx];
			}
			lazy[treeIdx] = 0;
		}
	}
	
}
