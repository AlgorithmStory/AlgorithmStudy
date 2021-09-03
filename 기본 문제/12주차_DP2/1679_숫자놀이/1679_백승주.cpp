#include <iostream>
#include <vector>
#include <string>
#include <sstream>
using namespace std;

#define MAX_INT 2147483647;

int main() {
	int n;				// 주어지는 숫자 개수
	int limit;			// 숫자 사용 횟수 <=50
	vector<int> numbers;// 주어지는 숫자 배열

	string str;
	string line;
	
	cin >> n;
	cin.ignore();

	getline(cin, line);
	stringstream ss(line);

	while (getline(ss, str, ' ')) {
		numbers.push_back(stoi(str));
	}
	
	cin >> limit;
	vector<int> min_numbers = {0};	//각 인덱스 번호를 만드는데 필요한 숫자의 최소 개수
	int value = 0;					//만들어 줄 숫자 변수
	int min_cnt;
	vector<int>::iterator iter;
	/*
		1. min_nubers의 각 인덱스에는 주어진 인덱스를 만들 수 있는 최소 숫자 갯수가 들어감
		2. 현재 value에서 최소로 만들 수 있는 숫자의 갯수는 이전에 만들었던 최소 숫자의 + 1로 구할 수 있음
			ex) 예제 입력조건에서
				value = 3 일때 
				min_number[3] = min_munber[0] + 1 OR min_number[2] + 1 이 될거임 이 중 더 작은 수를 고름
				이 과정을 숫자 사용 제한 횟수에 도달할때까지 반복				
	*/
	while (true) {
		value++;	// 루프가 돌 때마다 만들어줄 정수의 값을늘려줌
		min_cnt = MAX_INT;	// 사용한 숫자의 최소 개수
		for (iter = numbers.begin(); iter != numbers.end(); ++iter) {
			int number = *iter;	// 숫자 배열에 들어있는 숫자
			if (value - number >= 0) {
				//가지고 있는 숫자를 하나 더 사용해서 만들 수 있는 최소 개수를 구함
				min_cnt = min_cnt < min_numbers[value - number] + 1 ? min_cnt : min_numbers[value - number] + 1;
			}
			else break;
		}
		min_numbers.push_back(min_cnt);
		if (min_cnt > limit) break; //사용한 숫자의 수가 limit이상이면 while loop를 빠져나옴
	}
	if (value % 2 == 0) {// 홀순 승
		cout << "holsoon win at " << value;
	}
	else {				// 짝순 승
		cout << "jjaksoon win at " << value;
	}

	return 0;
}