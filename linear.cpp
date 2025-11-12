#include<iostream>
using namespace std;
int main()
{
    int a[5],num,index=-1;
    int i;
        cout<<"enter 5 number:";
        for(i = 0;i < 5;i++){
         cin>>a[i];
        }
cout<<"enter the number for which want to search:";
cin>>num;
for(i = 0; i < 5; i++){
       if(a[i] == num){
        index=i;
       break;
    }
    }
    if(index != -1)
    cout<<"\n found at index number:"<<index<<endl;
    else
    cout<<"\n number not found:"<<endl;
    return 0;
}
