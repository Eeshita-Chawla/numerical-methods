#include<iostream>
using namespace std;

/* Here n =4 */

int func(int x)
{
  int f = 10 - 3*x*x;
  return(f);
}

int main()
{
  int a = -1;
  int b = 3;
  int n = 4;
  float h = (b - a)/n;
  float i = h*(func(a) + func(b) + 4*func(a+h) + 2*func(a + 2*h)+ 4*func(a+3*h))/3;
  cout << "The integral is - " << i;
}
