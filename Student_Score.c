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
	char name[COUNT][12];  // [10][12]�� 12���� ���ڸ� COUNT  ������ŭ ����ڴٴ� �ǹ�
	int count;
	char grade[10];

	count = input_count();
	input_score(&count, name, kor, eng, mat, tot, avg);
	calc_grade(count, avg, grade);
	print_score(count, name, kor, eng, mat, tot, avg, grade);

	

	return 0;
}

//�л� �� ���� �Լ�
int input_count(void)
{
	int count;

	do
	{
		printf("ó���� �л����� �Է��ϼ���(�ִ� �л���(%d)) : ", COUNT);
		scanf("%d", &count);
		if ((count <= 0) || (COUNT < count))
		{
			printf("�Է¹����� ������ϴ�. �ٽ��Է��Ͻÿ�.\n");
		}
		else
			break;

	} while(1);
	
	return count;
}

//�л��̸�, ���� ���� �Է� �Լ�
void input_score(int* count, char (*np)[12],int* kp, int* ep, int* mp, int* tp, double* ap)
{
	int i;
	printf("�̸�, ����, ����, ���� ������ �Է��ϼ���!\n");
	for (i = 0; i < *count; i++)
	{
		scanf("%s", np[i]);
		if (strcmp(np[i], "quit") == 0)
			break;
		scanf("%d%d%d", kp + i, ep + i, mp + i);
		tp[i] = kp[i] + ep[i] + mp[i];
		ap[i] = (double)tp[i] / 3.0;
	}
	*count = i;

	return;
}

//�л� ���� �Լ�
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

// �Է� ������ ����ؼ� �����ִ� �Լ�
void print_score(int count, char(*name)[12], int* kor, int* eng, int* mat, int* tot, double* avg, char* grade)
{
	int i;

	system("cls");
	printf("--------------------------------------------------------\n");
	printf(":%-13s:%6s:%6s:%6s:%6s:%6s:%6s\n", " �̸� ", " ���� ", " ���� ", " ���� ", " ���� ", " ��� ", " ���� ");
	printf("--------------------------------------------------------\n");
	for (i = 0; i < count; i++)
	{
		printf(": %-12s:%5d :%5d :%5d :%5d :%5.1lf :%5c \n", name[i], kor[i], eng[i], mat[i], tot[i], avg[i], grade[i]);
	}
	printf("--------------------------------------------------------\n");

	return;
}