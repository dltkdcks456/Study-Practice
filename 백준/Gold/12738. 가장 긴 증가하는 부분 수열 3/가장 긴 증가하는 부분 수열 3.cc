#include <bits/stdc++.h>
using namespace std;
int N, lastIdx;
int * arr, * dp;
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);
	
	cin >> N;
	arr = new int[N];
	dp = new int[N];
	lastIdx = 0;

	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}

	memset(dp, 0, sizeof(dp));

	dp[0] = arr[0];

	for (int i = 1; i < N; i++) {
		int s = 0;
		int e = lastIdx;
		if (dp[lastIdx] < arr[i]) {
			dp[++lastIdx] = arr[i];
		}
		else {
			bool flag = false;
			while (s <= e) {
				int m = (s + e) / 2;
				if (dp[m] == arr[i]) {
					flag = true;
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
			}
			
			
			
		}
	}

	cout << lastIdx + 1 << endl;
	return 0;

}