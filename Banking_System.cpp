#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;

class Account
{
private:
	int id = 0;				// 고객 계좌번호
	int cash = 0;			// 고객 잔액
	char* name = { 0 };		// 고객명

public:
	Account() {}

	Account(int ID, int Cash, const char* nm)		// 생성자
	{
		id = ID;
		cash = Cash;
		name = new char[sizeof(nm) + 1];
		strcpy(name, nm);
	}

	~Account()										// 소멸자
	{
		delete name;
	}

	void add(int ID, int pscash)					// 추가 입금 함수
	{
		if (id == ID)
		{
			cash += pscash;
		}
	}

	void out(int ID, int pscash)					// 추가 출금 함수
	{
		if (id == ID)
		{
			cash -= pscash;
		}
	}

	int GetData()const { return id; }
	char GetChar()const { return *name; }

	void view() const									// 전체 정보 함수
	{
		cout << "------- 고객 정보 -------" << "\n" << endl;
		cout << "고객 계좌번호 : " << id << endl;
		cout << "고객 이름 : " << name << endl;
		cout << "고객 계좌 잔액 : " << cash << endl;
		cout << "------------------------" << "\n" << endl;
	}

};

class AccountHandler
{
private:
	Account* Save[100] = { NULL };		// 객체 포인트배열
	int cnt;						   // 인원 저장 값

public:

	AccountHandler()
	{
		cnt = 0; 
	}

	void menulist();
	void newcreate();
	void input_money();
	void output_money();
	void custominfo();
	void end();
};

void AccountHandler::menulist()
{
	cout << "======================*은행계좌 프로그램*==========================" << "\n" << endl;
	cout << "1. 계좌 신설" << "\n" << "2. 입금" << "\n" << "3. 출금" << "\n"
		<< "4. 고객 정보" << "\n" << "5. 프로그램 종료" << "\n" << endl;
	cout << "===================================================================" << "\n" << endl;
}

void AccountHandler::newcreate()								//고객 정보 생성
{
	int id, cash;
	char name[10];

	cout << "계좌 번호를 입력하세요 : ";
	cin >> id;
	cout << "고객 이름을 입력하세요 : ";
	cin >> name;
	cout << "초기 입금 금액을 입력하세요 : ";
	cin >> cash;

	Save[cnt++] = new Account(id, cash, name);			//동적 할당 생성

	system("cls");
	cout << "고객 계좌 번호 : " << id << endl;
	cout << "고객 이름 : " << name << endl;
	cout << "계좌 잔액 : " << cash << "원" << endl;
	cout << "[계좌가 생성 되었습니다]" << "\n" << endl;
}

void AccountHandler::input_money()									//입금 함수
{
	int id, cash, i;

	cout << "고객 계좌 번호를 입력하세요 : ";
	cin >> id;
	cout << "입금 할 금액을 입력하세요 : ";
	cin >> cash;

	for (i = 0; i < cnt; i++)
	{
		Save[i]->add(id, cash);					// 기존 금액과 추가 입금 한 값을 더함
	}

	system("cls");
	cout << "고객 계좌 번호 : " << id << endl;
	cout << "입금 금액 : " << cash << "원" << endl;
	cout << "[입금이 완료되었습니다.]" << "\n" << endl;
}

void AccountHandler::output_money()						//출금 함수
{
	int id, cash, i;

	cout << "고객 계좌 번호 : ";
	cin >> id;
	cout << "출금 금액 : ";
	cin >> cash;

	for (i = 0; i < cnt; i++)
	{
		Save[i]->out(id, cash);			// 기존 금액에서 입력한 값만큼 출금
	}

	system("cls");
	cout << "고객 계좌 번호 : " << id << endl;
	cout << "출금 금액 : " << cash << "원" << endl;
	cout << "[출금이 완료되었습니다.]" << endl;

}

void AccountHandler::custominfo()								//고객 정보 리스트
{
	int i;

	for (i = 0; i < cnt; i++)
	{
		Save[i]->view();
	}
}

void AccountHandler::end()										//클래스 동적할당 해제
{
	int i = 0;

	if (i <= cnt)
	{
		delete Save[i];
		exit(1);
	}
}

int main()
{
	int num;
	AccountHandler AH;

	while (1)
	{
		AH.menulist();
		cout << "번호를 선택하세요 : ";
		cin >> num;

		switch (num)
		{
		case 1:
			system("cls");
			AH.newcreate();
			break;

		case 2:
			system("cls");
			AH.input_money();
			break;

		case 3:
			system("cls");
			AH.output_money();
			break;

		case 4:
			system("cls");
			AH.custominfo();
			break;

		case 5:
			AH.end();
			break;

		default:
			if (num == 0 || num > 5)
			{
				cout << "범위를 벗어났습니다. 다시 입력바랍니다.(1~5번)" << endl;
			}
			break;
		}
	}

	return 0;
}