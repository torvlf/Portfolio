#include <stdio.h>
#include <windows.h>
#define COUNT 10
int input_count(void);
void input_score(int* count, char(*np)[12], int(*socre)[4], double* ap);
void calc_grade(int count, double* avg, char* grade);
void print_score(int count, char(*name)[12], int(*score)[4], double* avg, char* grade);

int main()
{
	int score[COUNT][4] = { 0 };
	double avg[COUNT];
	char name[COUNT][12];  // [10][12]�� 12���� ���ڸ� COUNT  ������ŭ ����ڴٴ� �ǹ�
	int count;
	char grade[10];

	count = input_count();
	input_score(&count, name, score, avg);
	calc_grade(count, avg, grade);
	print_score(count, name, score, avg, grade);

	return 0;
}

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

	} while (1);

	return count;
}

void input_score(int* count, char(*np)[12], int(*score)[4], double* ap)
{
	int i, j;
	printf("�̸�, ����, ����, ���� ������ �Է��ϼ���!\n");
	for (i = 0; i < *count; i++)
	{
		scanf("%s", np[i]);
		if (strcmp(np[i], "quit") == 0)
			break;
		
		for (j = 0; j < 3; j++)
		{
			scanf("%d", &score[i][j]);  // scanf("%d", (*(*score +i)+j);
			score[i][3] += score[i][j];  // ������ �ִ°�
		}

		ap[i] = (double)score[i][3] / 3.0;
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

void print_score(int count, char(*name)[12], int(*score)[4], double* avg, char* grade)
{
	int i, j;

	system("cls");
	printf("--------------------------------------------------------\n");
	printf(":%-13s:%6s:%6s:%6s:%6s:%6s:%6s\n", " �̸� ", " ���� ", " ���� ", " ���� ", " ���� ", " ��� ", " ���� ");
	printf("--------------------------------------------------------\n");
	for (i = 0; i < count; i++)
	{
		printf(": %-12s", name[i]);
		for (j = 0; j < 4; j++);
		{
			printf("%5d", score[i][j]);
		}
		printf(":%5.1lf :%5c \n", avg[i], grade[i]);
	}
	printf("--------------------------------------------------------\n");

	return;
}