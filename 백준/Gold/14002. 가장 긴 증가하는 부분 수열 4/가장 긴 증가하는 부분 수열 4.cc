#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <cstring>
#include <array>

using namespace std;
int N, lastIdx, maxIdx;
int* arr, * dp, * ans, * tmp;
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);

	cin >> N;
	arr = new int[N];
	ans = new int[N];
	dp = new int[N];
	lastIdx = 0;

	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}

	for (int i = 0; i < N; i++) {
		ans[i] = 0;
		dp[i] = 0;
	}

	dp[0] = arr[0];

	for (int i = 1; i < N; i++) {
		int s = 0;
		int e = lastIdx;
		if (dp[lastIdx] < arr[i]) {

			lastIdx++;
			ans[i] = lastIdx;
			dp[lastIdx] = arr[i];

		}
		else {
			bool flag = false;
			while (s <= e) {
				int m = (s + e) / 2;
				if (dp[m] == arr[i]) {
					flag = true;
					ans[i] = m;
					break;
				}
				else if (dp[m] > arr[i]) {
					e = m - 1;
				}
				else {
					s = m + 1;
				}
			}
			if (!flag) {
				dp[s] = arr[i];
				ans[i] = s;
			}
		}
	}

	cout << lastIdx + 1 << endl;

	//for (int i = 0; i < N; i++) {
	//	cout << ans[i] << " ";
	//}
	int tempIdx = lastIdx;
	tmp = new int[lastIdx];

	for (int i = N - 1; i > -1; i--) {
		if (ans[i] == lastIdx) {
			tmp[lastIdx] = i;
			lastIdx--;
			if (lastIdx < 0) {
				break;
			}
		}
	}

	for (int i = 0; i <= tempIdx; i++) {
		cout << arr[tmp[i]] << " ";
	}

	return 0;
}