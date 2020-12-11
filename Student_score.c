#include <stdio.h>
#include <windows.h>
#define COUNT 10
int input_count(void);
void input_score(int* count, char(*np)[12], int* kp, int* ep, int* mp, int* tp, double* ap);
void calc_grade(int count, double* avg, char* grade);
void print_score(int count, char(*name)[12], int* kor, int* eng, int* mat, int* tot, double* avg, char* grade);

int main()
{
	int kor[COUNT];
	int eng[COUNT];
	int mat[COUNT];
	int tot[COUNT];
	double avg[COUNT];
	char name[COUNT][12];  // [10][12]는 12개의 문자를 COUNT  갯수만큼 만들겠다는 의미
	int count;
	char grade[10];

	count = input_count();
//	count = input_score(count, name, kor,eng, mat, tot, avg);
	input_score(&count, name, kor, eng, mat, tot, avg);
	calc_grade(count, avg, grade);
	print_score(count, name, kor, eng, mat, tot, avg, grade);

	

	return 0;
}

int input_count(void)
{
	int count;

	do
	{
		printf("처리할 학생수를 입력하세요(최대 학생수(%d)) : ", COUNT);
		scanf("%d", &count);
		if ((count <= 0) || (COUNT < count))
		{
			printf("입력범위를 벗어났습니다. 다시입력하시오.\n");
		}
		else
			break;

	} while(1);
	
	return count;
}

void input_score(int* count, char (*np)[12],int* kp, int* ep, int* mp, int* tp, double* ap)
{
	int i;
	printf("이름, 국어, 영어, 수학 점수를 입력하세요!\n");
	for (i = 0; i < *count; i++)
	{
		scanf("%s", np[i]);
		if (strcmp(np[i], "quit") == 0)
			break;
///		scanf("%d%d%d", &kp[i], &ep[i],  &mp[i]);
		scanf("%d%d%d", kp + i, ep + i, mp + i);
		tp[i] = kp[i] + ep[i] + mp[i];
		ap[i] = (double)tp[i] / 3.0;
	}
	*count = i;

	return;
}

void calc_grade(int count, double* avg, char* grade)
{
	int i;

	for (i = 0; i < count; i++)
	{
		switch ((int)avg[i] / 10)
		{
		case 10:
		case 9:
			grade[i] = 'A';
			break;
		case 8:
			grade[i] = 'B';
			break;
		case 7:
			grade[i] = 'C';
			break;
		case 6:
			grade[i] = 'D';
			break;
		default:
			grade[i] = 'F';
			break;
		}
	}
	return;
}

void print_score(int count, char(*name)[12], int* kor, int* eng, int* mat, int* tot, double* avg, char* grade)
{
	int i;

	system("cls");
	printf("--------------------------------------------------------\n");
	printf(":%-13s:%6s:%6s:%6s:%6s:%6s:%6s\n", " 이름 ", " 국어 ", " 영어 ", " 수학 ", " 총점 ", " 평균 ", " 학점 ");
	printf("--------------------------------------------------------\n");
	for (i = 0; i < count; i++)
	{
		printf(": %-12s:%5d :%5d :%5d :%5d :%5.1lf :%5c \n", name[i], kor[i], eng[i], mat[i], tot[i], avg[i], grade[i]);
	}
	printf("--------------------------------------------------------\n");

	return;
}
